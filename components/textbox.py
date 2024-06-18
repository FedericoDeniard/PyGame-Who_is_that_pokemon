import pygame
from components.button import Button
from assets.colours.colours import colours

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

    def get_text(self):
        return self.text
    
    def draw_line(self):
        start_pos = (self.position[0] + 10, self.position[1] + self.position[3] - 10)
        end_pos = (self.position[0] + self.position[2] - 10, self.position[1] + self.position[3] - 10)
        pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos, width=2)

    
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
                    self.update_text('')
                elif event.key == pygame.K_BACKSPACE:
                    text = self.get_text()
                    self.update_text(text[:-1])
                else:
                    text = self.get_text() + event.unicode
                    self.update_text(text)
        else:
            self.background_colour = self.copy_background_colour    # TODO Esto estaría bueno cambiarlo por un swap, detectando el cambio de estado