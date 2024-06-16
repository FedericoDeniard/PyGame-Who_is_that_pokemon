from assets.colours.main import colours
import pygame
class Button:
    def __init__(self, screen, position: tuple, background_colour = (255,255,255), border_radius=0, text="", font='Calibri', font_size=40, border_colour = None, border_width = 0, text_colour = (0,0,0), text_align = 'center'):
        self.screen = screen
        self.background_colour = background_colour
        self.position = position
        self.border_radius = border_radius
        self.text = text
        self.font = font
        self.font_size = font_size
        self.border_colour = border_colour
        self.border_width = border_width
        self.text_colour = text_colour
        self.hitbox = pygame.Rect(position)
        self.text_align = text_align
        self.text_rect = None

    def draw_button(self):
        if self.border_colour and self.border_width > 0:
            self.hitbox = pygame.draw.rect(self.screen, self.border_colour, self.position, border_radius=self.border_radius)
            inner_position = (
                self.position[0] + self.border_width,
                self.position[1] + self.border_width,
                self.position[2] - 2 * self.border_width,
                self.position[3] - 2 * self.border_width
            )
            border_radius = self.border_radius - self.border_width if self.border_radius > 0 and self.border_radius > self.border_width else 0
            pygame.draw.rect(self.screen, self.background_colour, inner_position, border_radius=border_radius)
        else:
            self.hitbox = pygame.draw.rect(self.screen, self.background_colour, self.position, border_radius = self.border_radius)

        if self.text:
            myFont = pygame.font.SysFont(self.font, self.font_size)
            text_surface = myFont.render(self.text, True, self.text_colour)  # Text, Antialiasing, colour
            match self.text_align:
                case "center":
                    text_rect = text_surface.get_rect(center=(self.position[0] + self.position[2] // 2, self.position[1] + self.position[3] // 2))
                case "left":
                    text_rect = text_surface.get_rect(topleft=(self.position[0] + self.border_width + 2, self.position[1] + self.border_width + (self.position[3] - text_surface.get_height()) // 2))
            self.text_rect = text_rect
            self.screen.blit(text_surface, text_rect)

    def get_text_surface(self):
        return self.text_rect
    
    def get_hitbox(self):
         return self.hitbox
