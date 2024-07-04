from classes.class_pokemon import Pokemon
from Packages.Package_sort.bubblesort import bubble_sort
from random import randint
from PIL import Image
import pygame

class Pokedex:
    def __init__(self, pokemons:list[dict|Pokemon]):
        self.pokemons = []
        if type(pokemons[0]) == dict:
            for pokemon in pokemons:
                self.pokemons.append(Pokemon(pokemon['names'], pokemon['id'], pokemon['gen'], pokemon['difficulty']))
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
    
    def set_pokemons(self, new_pokemons: list):
        self.pokemons = new_pokemons

    def get_random(self, window:tuple, pokemons:list[Pokemon] = False):
        pokemon_list = pokemons if pokemons else self.pokemons
        rand = randint(0, len(pokemon_list)-1)
        random_pokemon = pokemon_list.pop(rand)
        generation = random_pokemon.get_generation()
        pokemon_id = random_pokemon.get_id()
        pokemon_image = self.get_pokemon_image(generation, window, pokemon_id)
        return random_pokemon, pokemon_image
    
    def get_pokemon_image(self, gen:int, window:tuple, pokemon_id):
        image_path = f"assets/pokemons/pokemons_{gen}.png"
        image = Image.open(image_path)
        match gen:
            case 1:
                repeated = [4, 14, 22, 23, 25, 26, 32, 34, 35, 37, 39, 49, 51, 55, 57, 60, 62, 68, 70, 72, 74, 86, 88, 98, 100, 102, 111, 113, 117, 119, 128, 135, 138, 145, 147, 154, 156, 161, 168, 170]
            case 2:
                pokemon_id -= 151
                repeated = [4, 16, 18, 31, 39, 41, 46, 51, 53, 57, 89, 96, 98, 103, 106, 108, 111, 116, 120, 126, 130]
                for i in range(60,88):
                    repeated.append(i)
            case 3:
                pokemon_id -= 251
                repeated = [5, 7, 9, 20, 23, 27, 30, 32, 65, 67, 75, 77, 79, 85, 87, 92, 93, 94, 95, 96, 97, 98, 99, 105, 124, 126, 127, 128, 148]
            case 4:
                pokemon_id -= 386
                repeated = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 32, 38, 39, 41, 42, 45, 48, 50, 52, 55, 57, 59, 61, 81, 83, 85, 90, 92, 96, 98, 101, 103, 106, 108, 110, 114, 116, 125, 132, 133, 134, 135, 136, 145]
        
        bubble_sort(repeated)
        for number in repeated:
            if pokemon_id >= number:
                pokemon_id += 1
        
        pokemon_id -= 1

        axis_x = pokemon_id % 15
        axis_y = pokemon_id // 15
        crop_area = (256*axis_x, 256*axis_y, 256*(axis_x+1), 256*(axis_y+1))

        cropped_image = image.crop(crop_area)
        cropped_image.save('assets/pokemons/pokemon_temp.png')

        data = cropped_image.getdata()
        new_data = []
        for item in data:
            new_data.append((0,0,0, item[3]))
        cropped_image.putdata(new_data)
        cropped_image.save('assets/pokemons/pokemon_temp_dark.png')

        cropped_image = pygame.image.load('assets/pokemons/pokemon_temp.png')
        cropped_image = pygame.transform.scale(cropped_image, (window[0]/3, window[1]/2))
        cropped_image_dark = pygame.image.load('assets/pokemons/pokemon_temp_dark.png')
        cropped_image_dark = pygame.transform.scale(cropped_image_dark, (window[0]/3, window[1]/2))

        return cropped_image, cropped_image_dark