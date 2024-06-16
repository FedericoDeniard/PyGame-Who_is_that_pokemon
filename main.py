from classes.class_pokedex import Pokedex
import pygame
import json

from assets.colours.main import colours
from components.button import Button
from components.textbox import Textbox


config = 'config.json'
config_data = {}

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW = (WINDOW_WIDTH, WINDOW_HEIGHT)

with open(config, 'r') as file:
    config_data = json.load(file)

pokedex = Pokedex(config_data['pokemons'])

pygame.init()

window = pygame.display.set_mode(WINDOW)

backround = pygame.image.load('assets/interface/backround.jpg')
backround = pygame.transform.scale(backround, (WINDOW_WIDTH, WINDOW_HEIGHT))

button = Button(window, (500, 500, 250, 50), background_colour=colours['WHITE'],  text="Mostrar Textbox", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15,)
show_start = True
button_hitbox = button.get_hitbox()


text_box = Textbox(window, (525, 425, 200, 50), background_colour=colours['WHITE'],  text="Hola", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15)
show_text = False

run_flag = True
while run_flag == True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_hitbox.collidepoint(event.pos):
                show_text = not show_text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                text_box.update_text('')
            elif event.key == pygame.K_BACKSPACE:
                text = text_box.get_text()
                text_box.update_text(text[:-1])
            else:
                text = text_box.get_text() + event.unicode
                text_box.update_text(text) 

    window.blit(backround, (0,0))
    
    if show_start:
        button.draw_button()
    if show_text:
        text_box.draw_button()
        text_box.draw_line() # TODO This line should be draw on draw_button()

    

    pygame.display.update()