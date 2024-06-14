from classes.class_pokedex import Pokedex
import json

config = 'config.json'
config_data = {}

with open(config, 'r') as file:
    config_data = json.load(file)


pokedex = Pokedex(config_data['pokemons'])

# print(pokedex.check_name("pikachu"))
# print(pokedex.check_name("Bulbasaur"))
# print(pokedex.check_name("Bisasam"))
# print(pokedex.check_name("Ivysaur"))

easy_level = pokedex.get_difficulty('easy')
print(pokedex.check_name('Ivysaur', easy_level))