from classes.class_pokedex import Pokedex
from classes.sounds import Mixer, sounds
import pygame

from components.timer import Timer, Chronometer, get_best_time, get_average_time
from components.buttons import Button, Sticky, Textbox, Sticky_menu
from assets.colours.colours import colours

class Game():
    def __init__(self, pokedex:Pokedex, window:tuple):
        self.pokedex = pokedex
        self.WINDOW = window
        self.WINDOW_WIDTH = window[0]
        self.WINDOW_HEIGHT = window[1]

        self.music = Mixer()

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

        self.won_splash = pygame.image.load('assets/interface/ganaste.png')
        self.won_splash = pygame.transform.scale(self.won_splash, (self.WINDOW_HEIGHT, self.WINDOW_HEIGHT))

        self.window = pygame.display.set_mode(self.WINDOW)

        self.user_input = ""
        self.timer = Timer(2000)
        self.win_timer = Timer(2000)
        self.guess_time = Chronometer()
        self.loss_timer = Timer(2000)

        self.guessed_times = []
        self.best_time = [0,'']

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
        self.main_menu_quit = Button(self.window, (325, 300, 150, 50), self.music, background_colour=colours['WHITE'],  text="Salir", font_size=20, border_colour=colours["BLACK"], border_width=2, border_radius=8, sound=sounds["beep_sounds"][1])
        self.main_menu_continue = Button(self.window, (325, 225, 150, 50), self.music,background_colour=colours['WHITE'],  text="Jugar", font_size=20, border_colour=colours["BLACK"], border_width=2, border_radius=8, sound=sounds["beep_sounds"][0])

            # Configuration
        difficulty_labels = ['facil','medio','dificil','1','2','3','4']
        difficulties = []
        for difficulty in difficulty_labels:
            difficulties.append(Sticky(self.window,(30,50+(60*difficulty_labels.index(difficulty)), 150, 50),self.music, text=difficulty.title(), font_size=20, border_colour=colours["BLACK"], border_width=2, border_radius=8, sound = sounds["beep_sounds"][1]))
        self.difficulties = Sticky_menu(difficulties, self.pokedex, self.pokedex_copy)

        # Sound Bar
        self.volume_up = Button(self.window, (self.window.get_width() - 60, 30, 30, 30),self.music, text="+", font_size=20, border_colour=colours["BLACK"], border_width=2, border_radius=8, sound = sounds["beep_sounds"][1])
        self.volume_down = Button(self.window, (self.window.get_width() - 100, 30,30, 30), self.music,text="-", font_size=20, border_colour=colours["BLACK"], border_width=2, border_radius=8, sound = sounds["beep_sounds"][1])
        self.skip_song = Button(self.window, (self.window.get_width() - 140, 30,30, 30), self.music,text="⇄", font_size=20, border_colour=colours["BLACK"], border_width=2, border_radius=8, sound = sounds["beep_sounds"][1])
        self.stop_icon = "II"
        self.resume_icon = "▶️"
        self.stop_resume = Button(self.window, (self.window.get_width() - 180, 30,30, 30), self.music,text=self.stop_icon, font_size=20, border_colour=colours["BLACK"], border_width=2, border_radius=8, sound = sounds["beep_sounds"][1])

    
    #region Render game
    def render_game_menu(self):
        # Game Background
        self.game_background = pygame.image.load('assets/interface/background2.png')
        self.game_background = pygame.transform.scale(self.game_background, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # Game Buttons
        self.game_back = Button(self.window,(325,475, 150, 50), self.music,text="Atras", font_size=20, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound=sounds["beep_sounds"][1])
        self.game_continue = Button(self.window,(325,400, 150, 50), self.music,text="Enviar", font_size=20, border_colour=colours["BLACK"], border_width=2, border_radius=15, sound = sounds["no_sounds"][0])

        # Game Textbox
        self.game_text_box = Textbox(self.window, (300, 325, 200, 50), self.music,background_colour=colours['WHITE'], font_size=20, border_colour=colours["BLACK"], border_width=2, border_radius=8, placeholder="Escriba aqui")

        # Game Labels
        self.streak_label = Button(self.window, (40, 30, 150, 30),self.music, text=f'Racha: 0 / {self.max_streak}', font_size=20, border_colour=colours['BLACK'], border_width=2, border_radius=8)
        
        times = ['Ultimo', 'Promedio', 'Mejor', '']
        self.time_labels = []
        for time in times:
            text = '-'
            distance = 40*times.index(time) - 10
            if time != '':
                text = f'{time}:'
                distance = (40*times.index(time))
            self.time_labels.append(Button(self.window, (40, 75+distance, 150, 30),self.music, text=text, font_size=20, border_colour=colours['BLACK'], border_width=2, border_radius=8))
        

        self.idioms_label = Button(self.window, ((self.window.get_width()/2) - 300,(self.window.get_height()/2) - 30, 600, 50) ,self.music,text='', font_size=20, border_colour=colours['BLACK'], border_width=2, border_radius=8)

    #region Start
    def start(self):
        self.render_main_menu()

        self.render_game_menu()

    #region Show
    def show_menu(self):
        self.window.blit(self.main_menu_background, (0,0))
        self.difficulties.draw_menu()
        self.main_menu_quit.draw_button()
        self.main_menu_continue.draw_button()
        self.guessed_times = []
        self.time_labels[0].change_text('Ultimo:')
        self.time_labels[1].change_text('Promedio:')
        self.volume_up.draw_button()
        self.volume_down.draw_button()
        self.skip_song.draw_button()
        self.stop_resume.draw_button()
    
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
        self.loss_timer.update()
        self.win_timer.update()
        if not self.guess_time.active:
            self.guess_time.activate()

        if self.streak == self.max_streak:
            self.streak_label.change_text(f'Racha {self.streak} / {self.max_streak}')

            if self.win_timer.finished and not self.win_timer.active:
                self.main_menu = not self.main_menu
                self.game = not self.game
                self.streak = 0
                self.win_timer.reset()
            elif self.win_timer.active:
                self.window.blit(self.won_splash, (self.WINDOW_WIDTH/2 - self.won_splash.get_rect().right/2,0))
                
        elif self.timer.finished and not self.timer.active and self.streak != 10:
            self.pokemon_name, self.pokemon_images = self.pokedex_copy.get_random(self.WINDOW)
            self.guess_time.activate()
            self.pokemon_image = self.pokemon_images[0]
            self.pokemon_image_dark = self.pokemon_images[1]
            self.timer.reset()
            self.game_text_box.update_text("")
        elif self.timer.active or self.loss_timer.active:
            self.streak_label.change_text(f'Racha {self.streak} / {self.max_streak}')
            names = []
            for name in self.pokemon_name.get_names():
                repeated_flag = False
                for inside_name in names:
                    if name == inside_name:
                        repeated_flag = True
                if not repeated_flag:
                    names.append(name)

            names_string = ' - '.join(names)
            self.idioms_label.change_text(f'{names_string}')
            text_length = self.idioms_label.get_text_length() + 10
            self.idioms_label.resize((self.window.get_width()/2 - (text_length / 2) ,text_length))
            self.idioms_label.draw_button()

        if self.loss_timer.finished and not self.loss_timer.active:
            self.reset_game()

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
                self.streak_label.change_text(f'Racha {self.streak} / {self.max_streak}')

            
            elif self.volume_up.handle_event(event):
                self.music.change_volume(0.1)
            elif self.volume_down.handle_event(event):
                self.music.change_volume(-0.1)
            elif self.skip_song.handle_event(event):
                self.music.skip_song()
            elif self.stop_resume.handle_event(event):
                self.music.resume_stop_music()
                self.stop_icon, self.resume_icon = self.resume_icon, self.stop_icon
                self.stop_resume.change_text(self.stop_icon)

    def game_event(self, event):
        self.game_text_box.handle_event(event)
        
        for name in self.pokemon_name.get_names():
            if name == self.game_text_box.get_text().title():
                self.game_continue.change_sound(sounds["beep_sounds"][0])
                break
            else:
                self.game_continue.change_sound(sounds["no_sounds"][0])

        if self.game_back.handle_event(event):
            self.reset_game()

        
        if (self.game_continue.handle_event(event) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.game_text_box.texting)):

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.game_text_box.texting):
                self.game_continue.handle_event(pygame.MOUSEBUTTONDOWN)
            user_input = self.game_text_box.get_text()
            user_input = user_input.capitalize()

            self.pokemon_image_dark, self.pokemon_image = self.pokemon_image, self.pokemon_image_dark
            for name in self.pokemon_name.get_names():
                if name == user_input:
                    last_time = self.guess_time.reset()
                    self.guessed_times.append([self.pokemon_name.get_names()[0], last_time])
                    user_input = ""
                    self.timer.activate()
                    self.streak += 1
                    self.best_time = get_best_time(self.guessed_times[-1], self.best_time)
                    self.time_labels[0].change_text(f'Ultimo: {round(self.guessed_times[-1][1]/1000, 2)}')
                    self.time_labels[1].change_text(f'Promedio: {round(get_average_time(self.guessed_times)/1000, 2)}')
                    self.time_labels[2].change_text(f'Mejor: {round(self.best_time[0]/1000, 2)}')
                    self.time_labels[3].change_text(f'({self.best_time[1]})')
                    self.streak_label.change_text(f'Racha: {self.streak} / {self.max_streak}')
                    self.records[0] = str(self.best_time[0])
                    self.records[1] = self.best_time[1]
                    if self.streak == self.max_streak:
                        self.win_timer.activate()
                        self.music.play_sound(sounds['achieve_sound'])
                    break
                else:
                    self.loss_timer.activate()

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

    #region Reset Game
    def reset_game(self):
        self.main_menu = not self.main_menu
        self.game = not self.game
        self.timer.reset()
        self.guess_time.deactivate()
        self.game_text_box.update_text("")
        self.loss_timer.deactivate()
        self.loss_timer.reset()


    #region Run
    def run(self):

        self.start()
        
        while self.run_flag == True:
            self.music.play_random()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.quit_button:
                    self.exit()

                if self.main_menu:
                    self.menu_event(event)
                elif self.game:
                    self.game_event(event)

            if self.main_menu:
                self.show_menu()
            elif self.game:
                self.show_game()
            pygame.display.update()