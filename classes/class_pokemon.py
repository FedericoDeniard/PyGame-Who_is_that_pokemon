class Pokemon:
    def __init__(self, names:dict, image_path:str, gen:int, diffculty:str):
        self.spa_name = names['spa']
        self.eng_name = names['eng']
        self.fr_name = names['fr']
        self.it_name = names['it']
        self.deu_name = names['deu']

        self.image_path = image_path # TODO convertir a objeto pygame

        self.gen = gen

        self.difficulty = diffculty
        
    def get_names(self):
        names = [self.spa_name, self.eng_name, self.fr_name, self.it_name, self.deu_name]
        return names
    
    def get_names_dict(self):
        names = {
            'spa'
        }

    def get_generation(self):
        return self.gen

    def get_difficulty(self):
        return self.difficulty
    
    def check_name(self, name:str) -> bool:
        exists = False
        for pokemon_name in self.get_names():
            if name == pokemon_name:
                exists = True
                break
        return exists