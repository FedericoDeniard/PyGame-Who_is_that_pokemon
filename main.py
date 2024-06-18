from classes.class_pokedex import Pokedex
import pygame
import json

from assets.colours.colours import colours
from components.buttons import Button, Textbox

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

text_box = Textbox(window, (525, 425, 200, 50), background_colour=colours['WHITE'], font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, placeholder="Escriba aqui")

run_flag = True
while run_flag == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False

        run_flag = button.handle_event(event) if run_flag == True else False
        text_box.handle_event(event)

    window.blit(backround, (0,0))

    button.draw_button()
    text_box.draw_button()
    
    pygame.display.update()