import pygame
from random import randint

soundtrack = ["assets/music/Ending.mp3","assets/music/Gym.mp3","assets/music/Opening.mp3","assets/music/Pallet_Town.mp3","assets/music/Pokemon_Center.mp3"]
last_music = None
sounds = {
    "win_sounds": ["assets/sounds/win1.wav", "assets/sounds/win2.wav", "assets/sounds/win3.wav", "assets/sounds/win4.wav", "assets/sounds/win5.wav"],
    "no_sounds": ["assets/sounds/no1.wav", "assets/sounds/no2.wav", "assets/sounds/no3.wav", "assets/sounds/no4.wav"],
    "start_sound": "assets/sounds/start.wav",
    "beep_sounds": ["assets/sounds/beep1.wav", "assets/sounds/beep2.wav", "assets/sounds/beep3.wav", "assets/sounds/beep4.wav"],
    "achieve_sound": "assets/sounds/achieve1.wav",
    "won_game" : "assets/sounds/won_game.wav"
}


class Mixer():
    def __init__(self, volume=.5):
        pygame.mixer.init()
        self.music = None
        self.last_music = None
        self.stopped = False
        self.volume = volume
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.volume)

    def play_random(self):
        self.soundtrack = soundtrack
        if not pygame.mixer.music.get_busy() and not self.stopped:
            random_number = randint(0,len(self.soundtrack) - 1)
            while self.last_music == random_number:
                random_number = randint(0,len(self.soundtrack) - 1)
            pygame.mixer.music.load(self.soundtrack[random_number])
            pygame.mixer.music.play()
            self.last_music = random_number
    
    def play_sound(self, sound_path):
        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(self.volume + 0.2)
        sound.play()


    def change_volume(self, value):
        # print(f'volumen anterior:{self.volume}')
        # print(f'volumen a restar: {value}')
        new_volume = self.volume + value
        if new_volume > 0.8:
            new_volume = 0.8
        elif new_volume < 0:
            new_volume = 0
        self.volume = new_volume
        pygame.mixer.music.set_volume(self.volume)
        # print(f'volumen nuevo:{self.volume}')

    def skip_song(self):
        pygame.mixer.music.stop()
        random_number = randint(0,len(self.soundtrack) - 1)
        while self.last_music == random_number:
            random_number = randint(0,len(self.soundtrack) - 1)
        pygame.mixer.music.load(self.soundtrack[random_number])
        if not self.stopped:
            pygame.mixer.music.play()
        self.last_music = random_number

    def resume_stop_music(self):
        print(pygame.mixer.music.get_busy())
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.stopped = True
        else:
            pygame.mixer.music.unpause()
            self.stopped = False
