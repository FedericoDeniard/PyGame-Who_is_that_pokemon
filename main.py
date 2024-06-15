from classes.class_pokedex import Pokedex
import pygame
import json

config = 'config.json'
config_data = {}
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW = (WINDOW_WIDTH, WINDOW_HEIGHT)

with open(config, 'r') as file:
    config_data = json.load(file)


pokedex = Pokedex(config_data['pokemons'])

# print(pokedex.check_name("pikachu"))
# print(pokedex.check_name("Bulbasaur"))
# print(pokedex.check_name("Bisasam"))
# print(pokedex.check_name("Ivysaur"))

easy_level = pokedex.get_difficulty('easy')

pygame.init()

window = pygame.display.set_mode(WINDOW)

backround = pygame.image.load('assets/interface/backround.jpg')
backround = pygame.transform.scale(backround, (WINDOW_WIDTH, WINDOW_HEIGHT))
window.blit(backround, (0,0))

text_box = pygame.rect()

run_flag = True
while run_flag == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            window.blit()

    pygame.display.update()