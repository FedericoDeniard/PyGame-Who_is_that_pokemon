from classes.class_pokedex import Pokedex
from classes.class_game import Game
import json

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW = (WINDOW_WIDTH, WINDOW_HEIGHT)

config = 'config.json'
config_data = {}
pokemon_font = 'console'

with open(config, 'r') as file:
    config_data = json.load(file)

pokedex = Pokedex(config_data['pokemons'])
pokedex_copy = Pokedex(pokedex.get_pokemons())

game = Game(pokedex, WINDOW)

game.run()