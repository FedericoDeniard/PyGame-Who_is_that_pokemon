class Pokemon:
    def __init__(self, names:dict, image_path:str, gen:int):
        self.spa_name = names['spa']
        self.eng_name = names['eng']
        self.fr_name = names['fr']
        self.it_name = names['it']
        self.deu_name = names['deu']

        self.image_path = image_path # TODO convertir a objeto pygame

        self.gen = gen
        
    def get_names(self):
        names = [self.spa_name, self.eng_name, self.fr_name, self.it_name, self.deu_name]
        return names