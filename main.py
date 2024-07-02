from classes.class_pokedex import Pokedex
from classes.class_game import Game
import json

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW = (WINDOW_WIDTH, WINDOW_HEIGHT)

config = 'config.json'
config_data = {}
pokemon_font = 'console'

with open(config, 'r') as file:
    config_data = json.load(file)

pokedex = Pokedex(config_data['pokemons'])

game = Game(pokedex, WINDOW)

game.run()