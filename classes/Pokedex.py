from Pokemon import Pokemon

class Pokedex:
    def __init__(self, pokemons:list[Pokemon]):
        self.pokemons = []
        for pokemon in pokemons:
            self.pokemons.append(Pokemon(pokemon['names'], pokemon['image_path'], pokemon['gen']))
    
    def get_all_names(self) -> list[str]:
        names = []
        for pokemon in self.pokemons:
            names.append(pokemon.get_names())
    
        return names
