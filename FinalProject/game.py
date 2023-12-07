import pygame
import sys
class Game:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        pass 

    def check_win(self):
        pass 

    def check_fail(self): 
        # should probably take in food item and time cooking for 
        pass 

    def play_game(self):
        while self.check_fail != True:
            #draw screen
            if self.check_win():
                print(" wins!")
                #draw win screen
                break

    def run(self):
        # Main game loop
        running = True

        # Draw the initial screen
        self.screen.fill(self.BACKGROUND_COLOR)
        self.blocks.draw(self.screen)
        self.mango.draw(self.screen)
        
        while running:
            # Set fps to 120
            self.dt += self.clock.tick(120)

            # Handle closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Only update every 120 fps
            if self.dt > 120:
                self.dt = 0
                self.mango.update()

                # Draw to the screen
                self.screen.fill(self.BACKGROUND_COLOR)
                self.blocks.draw(self.screen)
                self.mango.draw(self.screen)

            # Update the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        sys.exit()
            

