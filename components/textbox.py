import pygame
from button import Button

class Textbox(Button):

    def __init__(self, screen, colour, position: tuple, border_radius=0, text="", font='Calibri', font_size=40, border_colour = None, border_width = 0, text_colour = (0,0,0)):

        super().__init__(self, screen, colour, position, border_radius, text, font, font_size, border_colour, border_width, text_colour)

    def update_text(self, text):
        self.text = text

'''
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si el usuario hace clic en la caja de texto
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = BLACK if self.active else GRAY

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font.render(self.text, True, BLACK)
'''