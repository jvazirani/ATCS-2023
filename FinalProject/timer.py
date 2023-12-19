import pygame
class Timer(): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y
        self.started = False
        self.last_time = 0
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
    def start(self): 
        self.started = True
        self.start_time = pygame.time.get_ticks()
    def reset(self):
        self.started = False
        self.last_time = 0
    def stop(self): 
        self.started = False
        self.last_time = pygame.time.get_ticks() - self.start_time

    def draw(self, screen):
        if self.started: 
            # Need to subtract because first term is time since window opened and second term is time since button pressed
            self.last_time = pygame.time.get_ticks() - self.start_time
        shown_time = (self.last_time / 1000)
        timer_text = self.font.render('Timer: ' + str(shown_time), True, 'Black')
        screen.blit(timer_text, (self.x, self.y))

