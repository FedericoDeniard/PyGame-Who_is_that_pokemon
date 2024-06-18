import pygame
from random import randint

soundtrack = ["assets/music/Ending.mp3","assets/music/Gym.mp3","assets/music/Opening.mp3","assets/music/Pallet_Town.mp3","assets/music/Pokemon_Center.mp3"]
last_music = None

class Play_random_music():
    def __init__(self):
        pygame.mixer.init()
        self.music = None
        self.soundtrack = soundtrack

    def play_random(self):
        if not pygame.mixer.music.get_busy():
            random_number = randint(0,len(self.soundtrack) - 1)
            while last_music == random_number:
                random_number = randint(0,len(self.soundtrack) - 1)
            pygame.mixer.init()
            pygame.mixer.music.load(self.soundtrack[random_number])
            pygame.mixer.music.set_volume(.2)
            pygame.mixer.music.play()