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
        egg = Food("Egg", (5000, 10000,), 'raw.png', 'cooked.png', 'burned.png') 
        toast = Food("Toast", (5000, 10000,), 'bread.png', 'toast.png', 'burnedtoast.png')
        self.foods = (egg, toast)
        self.food = self.foods[0]
        self.level = 0
        self.dt = 0
        self.timer = Timer(100, 200)
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
        if self.pan.get_state() == Pan.START_RAW:
            self.pan.update(Pan.START)
            self.timer.start()
    def level_up(self): 
        self.level += 1

    def stop_timer(self): 
        # if its raw cooked or burnt update accordingly\
        if self.pan.get_state() == Pan.COOKING: 
            self.timer.stop()
            if self.food.is_burned():
                self.pan.update(Pan.TIMER_LATE)
                self.lose()
            elif self.food.is_cooked():
                self.pan.update(Pan.TIMER_GOOD)
                self.level_up()
            elif self.food.is_raw():
                self.pan.update(Pan.TIMER_EARLY)
                self.lose()
            print(self.pan.get_state())


    def lose(self): 
        self.level = 0

    def reset_timer(self): 
        if self.level == len(self.foods): 
            self.level = 0
        self.timer.reset()
        self.pan.update(Pan.RESTART)
        self.food = self.foods[self.level]
        self.food.reset_cook_time()

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
        if self.pan.get_state() == Pan.DONE: 
            if self.level == len(self.foods): 
                message = "win!"
            else: 
                message = 'level up'
            font = pygame.font.Font(None, 36)  # You can adjust the font size as needed
            text = font.render(message, True, (100, 200, 55))  # White text
            self.screen.blit(text, (500, 100))
        if self.pan.get_state() == Pan.BURNED or self.pan.get_state() == Pan.RAW: 
            font = pygame.font.Font(None, 36)  # You can adjust the font size as needed
            text = font.render('LOST', True, (200, 100, 50))  # White text
            self.screen.blit(text, (500, 100))

        self.start_button.draw(self.screen)
        self.end_button.draw(self.screen)
        self.reset_button.draw(self.screen)
        self.timer.draw(self.screen)

if __name__ == "__main__":
    game = Game()
    game.run()










            

