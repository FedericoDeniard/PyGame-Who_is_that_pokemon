from pygame.time import get_ticks

class Timer:
    def __init__(self, duration, repeat = False):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.finish = False
        self.repeat = repeat

    def activate(self):
        self.active = True
        self.finish = False
        self.start_time = get_ticks()

    def deactivate(self):
        self.active = False
        self.finish = True
        self.start_time = 0 
        if self.repeat:
            self.activate()

    def update(self):
        if self.active:
            current_time = get_ticks()
            if current_time - self.start_time >= self.duration:
                self.deactivate()
    
    def is_finished(self):
        return self.finish

    def reset(self):
        self.finish = not self.finish

class Chronometer:
    def __init__(self):
        self.start_time = 0
        self.active = False
        self.finish = False
    def activate(self):
        self.active = True
        self.finish = False
        self.start_time = get_ticks()

    def deactivate(self):
        finish_time = get_ticks()
        duration = finish_time - self.start_time
        self.active = False
        self.finish = True
        self.start_time = 0
        return duration
    def reset(self):
        finish_time = get_ticks()
        duration = finish_time - self.start_time
        self.start_time = get_ticks()
        return duration    
    def is_finished(self):
        return self.finish