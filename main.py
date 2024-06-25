from classes.class_pokedex import Pokedex
import pygame
import json
from random import randint
from classes.sounds import Sounds, sounds

from assets.colours.colours import colours
from components.buttons import Button, Sticky, Textbox, Sticky_menu
from components.timer import Timer

config = 'config.json'
config_data = {}
pokemon_font = 'console'

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW = (WINDOW_WIDTH, WINDOW_HEIGHT)

music = Sounds()

with open(config, 'r') as file:
    config_data = json.load(file)

pokedex = Pokedex(config_data['pokemons'])

pygame.init()
pygame.display.set_caption("Who's that pokemon")
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

window = pygame.display.set_mode(WINDOW)

#region Main Menu

main_menu_quit = Button(window, (475, 500, 250, 50), background_colour=colours['WHITE'],  text="Salir", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound=sounds["beep_sounds"][1])
main_menu_continue = Button(window, (475, 425, 250, 50), background_colour=colours['WHITE'],  text="Continuar", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound=sounds["beep_sounds"][0])

main_menu_backround = pygame.image.load('assets/interface/backround.jpg')
main_menu_backroundbackround = pygame.transform.scale(main_menu_backround, (WINDOW_WIDTH, WINDOW_HEIGHT))

main_menu = True

#region Game

game_background = pygame.image.load('assets/interface/background2.png')
game_background = pygame.transform.scale(game_background, (WINDOW_WIDTH, WINDOW_HEIGHT))

game_back = Button(window,(475,675, 250, 50), text="Atras", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound=sounds["beep_sounds"][1])
game_continue = Button(window,(475,600, 250, 50), text="Enviar", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound = sounds["no_sounds"][0])
game_text_box = Textbox(window, (475, 525, 250, 50), background_colour=colours['WHITE'], font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, placeholder="Escriba aqui")
user_input = ""

difficulty_labels = ['easy', 'medium', 'hard']
difficulties = []

for difficulty in difficulty_labels:
    difficulties.append(Sticky(window,(50,100+(80*difficulty_labels.index(difficulty)), 250, 50), text=difficulty.capitalize(), font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound = sounds["beep_sounds"][1]))

difficulties = Sticky_menu(difficulties)

pokemon_name, pokemon_images = pokedex.get_random(WINDOW)
pokemon_image = pokemon_images[0]
pokemon_image_dark = pokemon_images[1]

timer = Timer(2000)

game = False

run_flag = True

while run_flag == True:
    music.play_random()
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
        difficulties.draw_menu()
        window.blit(pokemon_image_dark,(((WINDOW_WIDTH/2) - (pokemon_image_dark.get_rect().right / 2)),0))
        timer.update()

        if timer.is_finished() and not timer.active:
            pokemon_name, pokemon_images = pokedex.get_random(WINDOW, 'easy', [1])
            pokemon_image = pokemon_images[0]
            pokemon_image_dark = pokemon_images[1]
            timer.reset()
            game_text_box.update_text("")
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    #region Events Main Menu 
        if main_menu:
            run_flag = not main_menu_quit.handle_event(event) if run_flag == True else False
            if main_menu_continue.handle_event(event):
                main_menu = not main_menu
                game = not game
                strike = 0
    #region Events Game 
        elif game:
            game_text_box.handle_event(event)
            difficulties.handle_event(event)
            if game_back.handle_event(event):
                main_menu = not main_menu
                game = not game
            
            if game_text_box.get_text().title() in pokemon_name.get_names():
                game_continue.change_sound(sounds["beep_sounds"][0])
                # TODO al tocar enter no suena nada
            else:
                game_continue.change_sound(sounds["no_sounds"][0])
            
            if (game_continue.handle_event(event) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and game_text_box.texting)):
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and game_text_box.texting):
                    game_continue.handle_event(pygame.MOUSEBUTTONDOWN)
                elif not game_text_box.isplaceholder and not timer.active:
                    user_input = game_text_box.get_text()
                    user_input = user_input.capitalize()

                    if user_input in pokemon_name.get_names():
                        user_input = ""
                        timer.activate()
                        pokemon_image_dark, pokemon_image = pokemon_image, pokemon_image_dark
                        strike += 1
                        print(strike)
                    else:
                        main_menu = not main_menu
                        game = not game
                        pokemon_image = pokemon_images[0]
                        pokemon_image_dark = pokemon_images[1]
                        timer.reset()
                        game_text_box.update_text("")

    pygame.display.update()