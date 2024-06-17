import pygame
from components.button import Button
from assets.colours.main import colours

class Textbox(Button):

    def __init__(self, screen, position: tuple, background_colour=(255,255,255), border_radius=0, text="", font='Calibri', font_size=40, border_colour=None, border_width=0, text_colour=(0,0,0), placeholder=True):
        self.placeholder_colour = colours["GRAY"]
        passed_colour = self.placeholder_colour if placeholder else text_colour
        super().__init__(screen, position, background_colour, border_radius, text, font, font_size, border_colour, border_width, passed_colour, text_align='left')
        self.outside_letters = 0
        self.placeholder = placeholder
        self.placeholder_text = text
        self.perm_colour = text_colour
        self.texting = False

    def update_text(self, text, placeholder):
        self.text = text
        self.show_text = text
        self.draw_button()
        text_rect = self.get_text_surface()
        text_right_top = text_rect.right
        button_hitbox = self.get_hitbox()

        if text_right_top > button_hitbox.right - 5:
            self.outside_letters += 1
        elif self.outside_letters > 0:
            self.outside_letters -= 1
        self.show_text = self.text[self.outside_letters:]

        if placeholder:
            self.text_colour=self.placeholder_colour
        else:
            self.text_colour=self.perm_colour

        print(self.outside_letters)
        print(self.text)
        print(self.show_text)

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
                if self.get_text() == self.placeholder_text:
                    self.update_text('', True)
            elif not(self.get_hitbox().collidepoint(event.pos)):
                self.texting = False
                if self.get_text() == '':
                    self.update_text(self.placeholder_text, True)

        if self.texting:
            if event.type == pygame.KEYDOWN and self.texting:
                if event.key == pygame.K_RETURN:
                    self.update_text('', False)
                elif event.key == pygame.K_BACKSPACE:
                    text = self.get_text()
                    self.update_text(text[:-1], False)
                else:
                    text = self.get_text() + event.unicode
                    self.update_text(text, False)