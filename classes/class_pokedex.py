from classes.class_pokemon import Pokemon
from random import randint

class Pokedex:
    def __init__(self, pokemons:list[dict|Pokemon]):
        self.pokemons = []
        if type(pokemons[0]) == dict:
            for pokemon in pokemons:
                self.pokemons.append(Pokemon(pokemon['names'], pokemon['image_path'], pokemon['gen'], pokemon['difficulty']))
        elif type(pokemons[0]) == Pokemon:
            self.pokemons = pokemons

    def get_pokemons(self):
        return self.pokemons
        
    def get_generation(self, generation: int):
        pokemons = []
        for pokemon in self.pokemons:
            if pokemon.get_gen() == generation:
                pokemons.append(pokemon)
        return pokemons

    def get_difficulty(self, difficulty:str):
        pokemons = []
        for pokemon in self.pokemons:
            if pokemon.get_difficulty() == difficulty:
                pokemons.append(pokemon)
        
        return pokemons
    
    def get_random(self, pokemons:list[Pokemon] = False) -> Pokemon:
        pokemon_list = pokemons if pokemons else self.pokemons
        
        rand = randint(0, len(pokemon_list)-1)
        random_pokemon = pokemon_list.pop(rand)
        return random_pokemon