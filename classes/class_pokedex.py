from classes.class_pokemon import Pokemon
from random import randint
from PIL import Image
import pygame

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
    
    def get_random(self, window: tuple, pokemons:list[Pokemon] = False):
        pokemon_list = pokemons if pokemons else self.pokemons
        rand = randint(0, len(pokemon_list)-1)
        random_pokemon = pokemon_list.pop(rand)
        generation = random_pokemon.get_generation()
        pokemon_image = self.get_pokemon_image(generation, window)
        return random_pokemon, pokemon_image
    
    def get_pokemon_image(self, gen: int, window: tuple):
        image_path = f"assets/pokemons/pokemons_{gen}.png"
        image = Image.open(image_path)

        axis_x, axis_y = 0, 0
        crop_area = (256*axis_x, 256*axis_y, 256*(axis_x+1), 256*(axis_y+1))
        axis_x += 7
        axis_y += 7
        crop_area = (256*axis_x, 256*axis_y, 256*(axis_x+1), 256*(axis_y+1))

        cropped_image = image.crop(crop_area)
        data = cropped_image.getdata()
        new_data = []
        for item in data:
            new_data.append((0,0,0, item[3]))
        cropped_image.putdata(new_data)
        cropped_image.save('assets/pokemons/pokemon_temp.png')
        cropped_image = pygame.image.load('assets/pokemons/pokemon_temp.png')
        cropped_image = pygame.transform.scale(cropped_image, (window[0]/3, window[1]/2))

        return cropped_image