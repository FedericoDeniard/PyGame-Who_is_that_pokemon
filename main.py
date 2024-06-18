from classes.class_pokedex import Pokedex
import pygame
import json

from assets.colours.colours import colours
from components.buttons import Button, Textbox

config = 'config.json'
config_data = {}
pokemon_font = 'console'

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW = (WINDOW_WIDTH, WINDOW_HEIGHT)

with open(config, 'r') as file:
    config_data = json.load(file)

pokedex = Pokedex(config_data['pokemons'])

pygame.init()

window = pygame.display.set_mode(WINDOW)

#region Main Menu

main_menu_quit = Button(window, (500, 500, 250, 50), background_colour=colours['WHITE'],  text="Salir", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15)
main_menu_continue = Button(window, (500, 425, 250, 50), background_colour=colours['WHITE'],  text="Continuar", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15)

main_menu_backround = pygame.image.load('assets/interface/backround.jpg')
main_menu_backroundbackround = pygame.transform.scale(main_menu_backround, (WINDOW_WIDTH, WINDOW_HEIGHT))

main_menu = True

#region Game

game_background = pygame.image.load('assets/interface/background2.png')
game_background = pygame.transform.scale(game_background, (WINDOW_WIDTH, WINDOW_HEIGHT))

game_back = Button(window,( 525,675, 250, 50), text="Atras", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15)
game_continue = Button(window,( 525,600, 250, 50), text="Enviar", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15)
game_text_box = Textbox(window, (525, 525, 250, 50), background_colour=colours['WHITE'], font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, placeholder="Escriba aqui")
game = False

run_flag = True

while run_flag == True:
    #region Draw Main Menu
    if main_menu:
        window.blit(main_menu_backround, (0,0))
        main_menu_quit.draw_button()
        main_menu_continue.draw_button()
    #region Draw Game
    elif game:
        window.blit(game_background, (0,0))
        game_text_box.draw_button()
        game_back.draw_button()
        game_continue.draw_button()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    #region Events Main Menu 
        if main_menu:
            run_flag = not main_menu_quit.handle_event(event) if run_flag == True else False
            if main_menu_continue.handle_event(event):
                main_menu = not main_menu
                game = not game
    #region Events Game 
        elif game:
            game_text_box.handle_event(event)
            if game_back.handle_event(event):
                main_menu = not main_menu
                game = not game
            if game_continue.handle_event(event) and not game_text_box.isplaceholder:
                print(game_text_box.get_text())
    
    pygame.display.update()