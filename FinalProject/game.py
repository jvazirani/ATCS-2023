# import pygame
# from pan import Pan

# #screen dimensions 
# WIDTH, HEIGHT = 800, 600

# class Game:
#     def __init__(self):
#         self.reset_game()
#         background_image = pygame.image.load("background.png")
#         background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


#     def reset_game(self):
#         # state of pan goes to raw
#         pass

#     def check_win(self):
#         pass 

#     def check_fail(self): 
#         # should probably take in food item and time cooking for 
#         pass 

#     def play_game(self):
#         while self.check_fail != True:
#             #draw screen
#             if self.check_win():
#                 print(" wins!")
#                 #draw win screen
#                 break

#     def run(self):
#         # Main game loop
#         running = True

#         # Draw the initial screen
#         self.screen.fill()
#         self.blocks.draw(self.screen)
#         self.mango.draw(self.screen)
        
#         while running:
#             # Set fps to 120
#             self.dt += self.clock.tick(120)

#             # Handle closing the window
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
            
#             # Only update every 120 fps
#             if self.dt > 120:
#                 self.dt = 0
#                 self.mango.update()

#                 # Draw to the screen
#                 self.screen.fill(self.BACKGROUND_COLOR)
#                 self.blocks.draw(self.screen)
#                 self.mango.draw(self.screen)

#             # Update the display
#             pygame.display.flip()

#         # Quit Pygame
#         pygame.quit()
#         sys.exit()

# if __name__ == "__main__":
#     pm = Game()
#     pm.run()
# cooking_game.py
# game.py
from pan import Pan
from fsm import FSM
import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Cooking Game")
        self.clock = pygame.time.Clock()

        self.pan_width = 100
        self.pan_height = 100

        self.pan = Pan(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)

    def update(self):
        self.pan.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.pan.draw(self.screen)

    def start_cooking(self):
        print("Cooking has started...")

    def finish_cooking(self):
        cooking_time = 7  # Replace with your actual cooking time logic
        if 5 <= cooking_time <= 10:
            print("Food is cooked!")
            self.pan.fsm.process(self.pan.DONE)
        else:
            print("Oops! Food is burned.")
            self.pan.fsm.process(self.pan.BURNED)

if __name__ == "__main__":
    game = Game()
    game.run()










            

