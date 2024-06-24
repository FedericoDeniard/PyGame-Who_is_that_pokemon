import pygame
from random import randint

soundtrack = ["assets/music/Ending.mp3","assets/music/Gym.mp3","assets/music/Opening.mp3","assets/music/Pallet_Town.mp3","assets/music/Pokemon_Center.mp3"]
last_music = None
sounds = {
    "win_sounds": ["assets/sounds/win1.wav", "assets/sounds/win2.wav", "assets/sounds/win3.wav", "assets/sounds/win4.wav", "assets/sounds/win5.wav"],
    "no_sounds": ["assets/sounds/no1.wav", "assets/sounds/no2.wav", "assets/sounds/no3.wav", "assets/sounds/no4.wav"],
    "start_sound": "assets/sounds/start.wav",
    "beep_sounds": ["assets/sounds/beep1.wav", "assets/sounds/beep2.wav", "assets/sounds/beep3.wav", "assets/sounds/beep4.wav"],
    "achieve_sound": "assets/sounds/achieve1.wav"
}


class Sounds():
    def __init__(self):
        pygame.mixer.init()
        self.music = None
        self.last_music = None

    def play_random(self):
        self.soundtrack = soundtrack
        if not pygame.mixer.music.get_busy():
            random_number = randint(0,len(self.soundtrack) - 1)
            while self.last_music == random_number:
                random_number = randint(0,len(self.soundtrack) - 1)
            pygame.mixer.init()
            pygame.mixer.music.load(self.soundtrack[random_number])
            pygame.mixer.music.set_volume(.1)
            pygame.mixer.music.play()
            self.last_music = random_number
    
    def play_sound(self, sound_path):
        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(.1)
        sound.play()