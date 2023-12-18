# game.py
from pan import Pan
from food import Food
from fsm import FSM
import pygame
import sys
from button import Button
from timer import Timer

class Game:
    def __init__(self):
        pygame.init()
        # Sets screen size
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Cooking Game")
        self.clock = pygame.time.Clock()

        self.pan = Pan(self)
        self.food = Food("Egg", (5000, 10000))  # Adjust cooking time range for Egg
        self.dt = 0
        self.timer = Timer(100, 200)
        
        self.is_down_arrow_pressed = False 
        self.users_time = 0

        self.start_button = Button(100, 100, 50, 50, 'start')
        self.end_button = Button(200, 100, 50, 50, 'stop')
        self.reset_button = Button(300, 100, 50, 50, 'reset')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if self.start_button.collidepoint(event.pos): 
                        self.start_timer()
                    elif self.end_button.collidepoint(event.pos): 
                        self.stop_timer()
                    elif self.reset_button.collidepoint(event.pos): 
                        self.reset_timer()
            self.update()
            self.draw()
            pygame.display.flip()

            self.dt = self.clock.tick(30)

    def get_elapsed_time(self):
        return self.dt

    def update(self):
        if self.pan.get_state() == Pan.COOKING: 
            self.food.update_cook_time(self.dt)

    def start_timer(self): 
        self.pan.update(Pan.START)
        self.timer.start()

    def stop_timer(self): 
        # if its raw cooked or burnt update accordingly
        self.timer.stop()
        if self.pan.get_state() == Pan.BURNED: 
            self.pan.update(Pan.TIMER_LATE)
        elif self.pan.get_state() == Pan.DONE: 
            self.pan.update(Pan.TIMER_GOOD)
        elif self.pan.get_state() == Pan.RAW: 
            self.pan.update(Pan.TIMER_EARLY)


    def reset_timer(self): 
        self.timer.reset()

    def draw(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, 800, 800))
        self.pan.draw(self.screen)
        if self.pan.get_state() == Pan.BURNED: 
            self.food.draw_burned(self.screen, 400, 300)  

        elif self.pan.get_state() == Pan.DONE: 
            self.food.draw_cooked(self.screen, 400, 300) 

        elif self.pan.get_state() == Pan.RAW: 
            self.food.draw_raw(self.screen, 400, 300)  
        else: 
            self.food.draw_raw(self.screen, 400, 300)  

        self.start_button.draw(self.screen)
        self.end_button.draw(self.screen)
        self.reset_button.draw(self.screen)
        self.timer.draw(self.screen)

if __name__ == "__main__":
    game = Game()
    game.run()










            

