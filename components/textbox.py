import pygame
from components.button import Button

class Textbox(Button):

    def __init__(self, screen, position: tuple, background_colour=(255,255,255), border_radius=0, text="", font='Calibri', font_size=40, border_colour=None, border_width=0, text_colour=(0,0,0)):
        super().__init__(screen, position, background_colour, border_radius, text, font, font_size, border_colour, border_width, text_colour, text_align='left')

    def update_text(self, text):
        self.text = text
        self.draw_button()
        text_rect = self.get_text_surface()
        text_right_top = text_rect.right
        button_hitbox = self.get_hitbox()
        if text_right_top > button_hitbox.right:
            self.background_colour = (255,0,0)

    def get_text(self):
        return self.text
    
    def draw_line(self):
        start_pos = (self.position[0] + 10, self.position[1] + self.position[3] - 10)
        end_pos = (self.position[0] + self.position[2] - 10, self.position[1] + self.position[3] - 10)
        pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos, width=2)

    

    # def handle_event(self, event):
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         # Si el usuario hace clic en la caja de texto
    #         if self.rect.collidepoint(event.pos):
    #             self.active = not self.active
    #         else:
    #             self.active = False
    #         self.color = BLACK if self.active else GRAY

    #     if event.type == pygame.KEYDOWN:
    #         if self.active:
    #             if event.key == pygame.K_RETURN:
    #                 print(self.text)
    #                 self.text = ''
    #             elif event.key == pygame.K_BACKSPACE:
    #                 self.text = self.text[:-1]
    #             else:
    #                 self.text += event.unicode
    #             self.txt_surface = font.render(self.text, True, BLACK)