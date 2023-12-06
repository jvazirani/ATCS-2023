import pygame
from fsm import FSM
class pan: 
    C = 'cooking'
    R = 'raw'
    D = 'done'
    def __init__(self, game, x , y):

        self.game = game

        # Load initial image
        self.background = pygame.image.load('insert image here')
        self.rect = self.image.get_rect()

        # Set rectangle that is the screen
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.centerx = x
        self.rect.centery = y

        # Create the finite state machine with initial state
        self.fsm = FSM(self.R)
        self.init_fsm()

    def init_fsm(self): 
        #add all transiitons 
        pass 

    def get_state(self):
        # TODO: Return the maze bot's current state
        return self.fsm.current_state
    
    def update(self):
        # TODO: Use the finite state machine to process input
        # print(self.get_state(), self.get_next_space())
        self.fsm.process(self.get_next_space())

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))
