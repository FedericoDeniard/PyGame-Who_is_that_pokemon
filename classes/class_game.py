from classes.class_pokedex import Pokedex
from classes.sounds import Sounds, sounds
import pygame

from components.buttons import Button, Sticky, Textbox, Sticky_menu
from assets.colours.colours import colours
from components.timer import Timer, Chronometer, get_best_time

class Game():
    def __init__(self, pokedex:Pokedex, window:tuple):
        self.pokedex = pokedex
        self.WINDOW = window
        self.WINDOW_WIDTH = window[0]
        self.WINDOW_HEIGHT = window[1]
    
    #region Initialize
    def initialize(self):
        self.music = Sounds()

        self.pokedex_copy = Pokedex(self.pokedex.get_pokemons())

        self.records = []
        self.record_titles = []

        with open('records.csv', 'r') as file:
            titles = True
            for line in file:
                if titles:
                    line = line.split('\n')[0]
                    for label in line.split(','):
                        self.record_titles.append(label)
                        titles = False
                else:
                    for label in line.split(','):
                        self.records.append(label)

        pygame.init()
        pygame.display.set_caption("Who's that pokemon")
        icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(icon)

        self.window = pygame.display.set_mode(self.WINDOW)

        self.user_input = ""
        self.timer = Timer(2000)
        self.win_timer = Timer(2000)
        self.guess_time = Chronometer()

        self.guessed_times = []
        self.best_time = get_best_time(self.guessed_times)

        self.max_streak = 10
        self.game = False
        self.main_menu = True
        self.run_flag = True
        self.quit_button = False

    #region Render Main
    def render_main_menu(self):
        # Menu Background
        self.main_menu_background = pygame.image.load('assets/interface/backround.jpg')
        self.main_menu_background = pygame.transform.scale(self.main_menu_background, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        
        # Menu Buttons
            # Basics
        self.main_menu_quit = Button(self.window, (475, 500, 250, 50), background_colour=colours['WHITE'],  text="Salir", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound=sounds["beep_sounds"][1])
        self.main_menu_continue = Button(self.window, (475, 425, 250, 50), background_colour=colours['WHITE'],  text="Continuar", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound=sounds["beep_sounds"][0])

            # Configuration
        difficulty_labels = ['easy','medium','hard','1','2','3','4']
        difficulties = []
        for difficulty in difficulty_labels:
            difficulties.append(Sticky(self.window,(50,100+(80*difficulty_labels.index(difficulty)), 150, 50), text=difficulty, font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound = sounds["beep_sounds"][1]))
        self.difficulties = Sticky_menu(difficulties, self.pokedex, self.pokedex_copy)

    #region Render game
    def render_game_menu(self):
        # Game Background
        self.game_background = pygame.image.load('assets/interface/background2.png')
        self.game_background = pygame.transform.scale(self.game_background, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # Game Buttons
        self.game_back = Button(self.window,(475,675, 250, 50), text="Atras", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound=sounds["beep_sounds"][1])
        self.game_continue = Button(self.window,(475,600, 250, 50), text="Enviar", font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound = sounds["no_sounds"][0])

        # Game Textbox
        self.game_text_box = Textbox(self.window, (475, 525, 250, 50), background_colour=colours['WHITE'], font_size=30, border_colour=colours["BLACK"], border_width=2, border_radius=15, placeholder="Escriba aqui")

        # Game Labels
        self.streak_label = Button(self.window, (50, 50, 200, 50), text='Racha: 0 / 10', font_size=30, border_colour=colours['BLACK'], border_width=2, border_radius=15)
        times = ['Ultimo', 'Mejor', 'Promedio']
        self.time_labels = []
        for time in times:
            self.time_labels.append(Button(self.window, (50, 150+(60*times.index(time)), 200, 50), text=f'{time}: ', font_size=30, border_colour=colours['BLACK'], border_width=2, border_radius=15))

    #region Start
    def start(self):
        self.initialize()
        
        self.render_main_menu()

        self.render_game_menu()

    #region Show
    def show_menu(self):
        self.window.blit(self.main_menu_background, (0,0))
        self.difficulties.draw_menu()
        self.main_menu_quit.draw_button()
        self.main_menu_continue.draw_button()
    
    def show_game(self):
        self.window.blit(self.game_background, (0,0))
        self.game_text_box.draw_button()
        self.game_back.draw_button()
        self.game_continue.draw_button()
        self.streak_label.draw_button()
        for time_label in self.time_labels:
            time_label: Button
            time_label.draw_button()
        self.window.blit(self.pokemon_image_dark,(((self.WINDOW_WIDTH/2) - (self.pokemon_image_dark.get_rect().right / 2)),0))
        self.timer.update()
        self.win_timer.update()
        if not self.guess_time.active:
            self.guess_time.activate()

        if self.streak == self.max_streak:
            self.streak_label.change_text(f'Racha {self.streak} / 10')

            # print(f"{win_timer.is_finished()},{win_timer.active}")
            if self.win_timer.is_finished() and not self.win_timer.active:
                self.main_menu = not self.main_menu
                self.game = not self.game
                self.streak = 0
                self.win_timer.reset()
        elif self.timer.is_finished() and not self.timer.active and self.streak != 10:
            self.pokemon_name, self.pokemon_images = self.pokedex_copy.get_random(self.WINDOW)
            self.pokemon_image = self.pokemon_images[0]
            self.pokemon_image_dark = self.pokemon_images[1]
            self.timer.reset()
            self.game_text_box.update_text("")
            self.streak_label.change_text(f'Racha {self.streak} / 10')
    
    #region Event
    def menu_event(self, event):
        if self.main_menu:
            self.quit_button = self.main_menu_quit.handle_event(event) if self.run_flag == True else False
            self.difficulties.handle_event(event)
            
            if self.main_menu_continue.handle_event(event):
                self.pokemon_name, self.pokemon_images = self.pokedex_copy.get_random(self.WINDOW)
                self.pokemon_image = self.pokemon_images[0]
                self.pokemon_image_dark = self.pokemon_images[1]
                self.main_menu = not self.main_menu
                self.game = not self.game
                self.streak = 0

    def game_event(self, event):
        self.game_text_box.handle_event(event)

        if self.game_back.handle_event(event):
            self.back()
        
        if self.game_text_box.get_text().title() in self.pokemon_name.get_names():
            self.game_continue.change_sound(sounds["beep_sounds"][0])
            # TODO al tocar enter no suena nada
        else:
            self.game_continue.change_sound(sounds["no_sounds"][0])
        
        if (self.game_continue.handle_event(event) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.game_text_box.texting)):

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.game_text_box.texting):
                self.game_continue.handle_event(pygame.MOUSEBUTTONDOWN)
            elif not self.game_text_box.isplaceholder and not self.timer.active:
                user_input = self.game_text_box.get_text()
                user_input = user_input.capitalize()

                if user_input in self.pokemon_name.get_names():
                    last_time = self.guess_time.reset()
                    self.guessed_times.append([self.pokemon_name.get_names()[0] , last_time])
                    self.best_time = get_best_time(self.guessed_times, last_time, self.best_time)
                    user_input = ""
                    self.timer.activate()
                    # guessed_times.append([self.pokemon_name.get_names()[0] , guess_time.reset()])
                    self.pokemon_image_dark, self.pokemon_image = self.pokemon_image, self.pokemon_image_dark
                    self.streak += 1
                    self.streak_label.change_text(f'Racha: {self.streak} / 10')
                    if self.streak == self.max_streak:
                        self.win_timer.activate()
                    if self.streak > int(self.records[0]):
                        self.records[0] = str(self.streak)
                    if 1 == 2: #TODO comprobar mejor tiempo
                        self.records[1] = '1' # TODO tiempo
                        self.records[2] = self.pokemon_name.get_names()[0]
                else:
                    self.back()

    #region Quit
    def exit(self):
        self.run_flag = False
        with open('records.csv', 'w') as file:
            titles = ''
            for label in self.record_titles:
                titles += f',{label}'
            titles = titles.replace(',', '', 1)
            titles += '\n'
            file.write(titles)
            record_text =''
            for record in self.records:
                record_text += f',{record}'
            record_text = record_text.replace(',', '', 1)
            file.write(record_text)

    def back(self):
        self.streak = 0
        self.main_menu = not self.main_menu
        self.game = not self.game
        self.pokemon_image = self.pokemon_images[0]
        self.pokemon_image_dark = self.pokemon_images[1]
        self.timer.reset()
        self.guess_time.deactivate()
        self.game_text_box.update_text("")

    #region Run
    def run(self):

        self.start()
        
        while self.run_flag == True:
            try:
                print(len(self.pokedex_copy.get_pokemons()))
            except:
                pass
            self.music.play_random()

            if self.main_menu:
                self.show_menu()
            elif self.game:
                self.show_game()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.quit_button:
                    self.exit()

            #region Events Main Menu 
                if self.main_menu:
                    self.menu_event(event)
            #region Events Game 
                elif self.game:
                    self.game_event(event)

            pygame.display.update()