from assets.colours.colours import colours
import pygame
from typing import Literal
from classes.sounds import Sounds

#region Button

class Button:
    def __init__(self, screen, position: tuple, background_colour = (255,255,255), border_radius=0, text="", font='Calibri', font_size=40, border_colour = None, border_width = 0, text_active_colour = (0,0,0), text_align:Literal['left','center'] = 'center', sound = None, sticky = False):
        self.screen = screen
        self.background_colour = background_colour
        self.position = position
        self.border_radius = border_radius
        self.text = text
        self.font = font
        self.font_size = font_size
        self.border_colour = border_colour
        self.border_width = border_width
        self.text_active_colour = text_active_colour
        self.hitbox = pygame.Rect(position)
        self.text_align = text_align
        self.text_rect = None
        self.show_text = self.text
        self.sound = sound
        self.sounds = Sounds()
        self.sticky = sticky
        self.sticky_pressed = False

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

        if self.text != "":
            if self.sticky_pressed:
                myFont = pygame.font.SysFont(self.font, self.font_size, bold = True)
            else:
                myFont = pygame.font.SysFont(self.font, self.font_size, bold = False)
            text_surface = myFont.render(self.show_text, True, self.text_active_colour)  # Text, Antialiasing, colour
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

    def handle_event(self, event):
        clicked = False
        if event == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            if event == pygame.MOUSEBUTTONDOWN or self.get_hitbox().collidepoint(event.pos):
                clicked = True
                if self.sound is not None:
                    self.sounds.play_sound(self.sound)
                if self.sticky:
                    self.sticky_pressed = not self.sticky_pressed

        return clicked
    
    def change_sound(self, sound):
        self.sound = sound
    
    def change_text(self, text):
        self.show_text = text

    def reproduce_sound(self):
        self.sounds.play_sound(self.sound)

    def is_active(self):
        return self.sticky_pressed

#region Textbox
class Textbox(Button):
    def __init__(self, screen, position: tuple, background_colour=(255,255,255), border_radius=0, font='Calibri', font_size=40, border_colour=None, border_width=0, text_colour=(0,0,0), placeholder='Escriba aquí', background_active_colour = colours["LIGHT_GRAY"]):
        self.placeholder_colour = colours["GRAY"]
        self.background_active_colour = background_active_colour
        self.copy_background_colour = background_colour
        self.text_active_colour = self.placeholder_colour
        self.placeholder = placeholder
        self.isplaceholder = True

        super().__init__(screen, position, background_colour, border_radius, placeholder, font, font_size, border_colour, border_width, self.text_active_colour, text_align='left')
        self.text_colour = text_colour
        self.outside_letters = 0
        self.placeholder = placeholder
        self.texting = False
        self.draw_line() # TODO This line should be draw on draw_button()

    def update_text(self, text):
        self.text = text
        self.show_text = text
        text_rect = self.get_text_surface()
        text_right_top = text_rect.right
        button_hitbox = self.get_hitbox()

        if text_right_top > button_hitbox.right - 29:
            self.outside_letters += 1
        elif self.outside_letters > 0:
            self.outside_letters -= 1
        self.show_text = self.text[self.outside_letters:]

    def get_text(self) -> str:
        return self.text
    
    def draw_line(self):
        start_pos = (self.position[0] + 10, self.position[1] + self.position[3] - 10)
        end_pos = (self.position[0] + self.position[2] - 10, self.position[1] + self.position[3] - 10)
        pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos, width=2)

    def draw_button(self):
        super().draw_button()
        self.draw_line()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.get_hitbox().collidepoint(event.pos):
                self.texting = True
                if self.isplaceholder:
                    self.update_text('')
                    self.isplaceholder = False
                    self.text_active_colour = self.text_colour
            elif not(self.get_hitbox().collidepoint(event.pos)):
                self.texting = False
                if self.get_text() == '':
                    self.update_text(self.placeholder)
                    self.isplaceholder = True
                    self.text_active_colour = self.placeholder_colour

        if self.texting:
            self.text_active_colour = self.text_colour
            self.background_colour = self.background_active_colour
            if event.type == pygame.KEYDOWN and self.texting:
                self.isplaceholder = False
                if event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    text = self.get_text()
                    self.update_text(text[:-1])
                else:
                    text = self.get_text() + event.unicode
                    self.update_text(text)
        else:
            self.background_colour = self.copy_background_colour    # TODO Esto estaría bueno cambiarlo por un swap, detectando el cambio de estado

# endregion