from pygame.time import get_ticks

class Timer:
    def __init__(self, duration, repeat = False):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self._finish = False
        self.repeat = repeat

    def activate(self):
        self.active = True
        self._finish = False
        self.start_time = get_ticks()

    def deactivate(self):
        self.active = False
        self._finish = True
        self.start_time = 0 
        if self.repeat:
            self.activate()

    def update(self):
        if self.active:
            current_time = get_ticks()
            if current_time - self.start_time >= self.duration:
                self.deactivate()
    
    @property
    def finished(self):
        return self._finish

    def reset(self):
        self._finish = not self._finish

class Chronometer:
    def __init__(self):
        self.start_time = 0
        self.active = False
        self._finish = False

    def activate(self):
        self.active = True
        self._finish = False
        self.start_time = get_ticks()

    def deactivate(self):
        finish_time = get_ticks()
        duration = finish_time - self.start_time
        self.active = False
        self._finish = True
        self.start_time = 0
        return duration
    
    def reset(self):
        finish_time = get_ticks()
        duration = finish_time - self.start_time
        self.active = False
        return duration
    
    @property
    def finished(self):
        return self._finish

def get_best_time( last_time: int, best_pokemon: list):
    new_best_pokemon = [best_pokemon[0], best_pokemon[1]]
    best_time = best_pokemon[0]
    pokemon_name = best_pokemon[1]
    if best_time == 0 or last_time < best_time:
        new_best_pokemon = [last_time, pokemon_name]
    return new_best_pokemon

def get_average_time( guessed_times: list):
    times = 0
    for i in range(len(guessed_times)):
        times += guessed_times[i][1]
    average = times / len(guessed_times)
    return average