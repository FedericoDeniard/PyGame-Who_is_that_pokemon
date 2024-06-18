from classes.class_pokedex import Pokedex
import pygame
import json

from assets.colours.colours import colours
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

button = Button(window, (500, 500, 250, 50), background_colour=colours['WHITE'],  text="Salir", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15,)
show_start = True
button_hitbox = button.get_hitbox()

placeholder_text = 'Nombre'
text_box = Textbox(window, (525, 425, 200, 50), background_colour=colours['WHITE'],  text=placeholder_text, font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, placeholder=placeholder_text)
show_text = True
text_box_hitbox = text_box.get_hitbox()

run_flag = True
while run_flag == True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_hitbox.collidepoint(event.pos):
                run_flag = False

        if show_text:
            text_box.handle_event(event)

    window.blit(backround, (0,0))
    
    if show_start:
        button.draw_button()
    if show_text:
        text_box.draw_button()
        text_box.draw_line() # TODO This line should be draw on draw_button()

    

    pygame.display.update()