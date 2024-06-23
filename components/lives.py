
class Lives:
    def __init__(self, max_lives, lives):
        self.lives = lives
        self.max_lives = max_lives
    
    def update_lives(self, lives):
        self.lives = lives
    
    def get_lives(self):
        return self.lives

    def is_alive(self):
        return True if self.lives > 0 else False
    
    def reset_lives(self):
        self.lives = self.max_lives