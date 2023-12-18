# pan.py
from fsm import FSM
import pygame

class Pan:

    PAN_WIDTH = 400 
    PAN_HEIGHT = 400
    COOKING = 'cooking'
    RAW = 'raw'
    DONE = 'done'
    BURNED = 'burned'
    START_RAW = 'started raw'

    # Inputs
    # issue: sometimes input is time, sometimes is timer up
    TIMER_EARLY = "tu"
    TIMER_GOOD = 'TG'
    TIMER_LATE = 'TL'
    START = 'start timer'
    RESTART = 'restart'

    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load("pan.png")  
        self.image = pygame.transform.scale(self.image, (self.PAN_WIDTH, self.PAN_HEIGHT))
        self.rect = self.image.get_rect()

        # Create the finite state machine with the initial state
        self.fsm = FSM(self.START_RAW)
        self.init_fsm()

    def init_fsm(self):
        self.fsm.add_transition(self.START, self.START_RAW, None, self.COOKING)
        self.fsm.add_transition(self.TIMER_EARLY, self.COOKING, None, self.DONE)
        self.fsm.add_transition(self.TIMER_GOOD, self.COOKING, None, self.BURNED)
        self.fsm.add_transition(self.TIMER_LATE, self.COOKING, None, self.RAW)
        self.fsm.add_transition(self.RESTART, self.BURNED, None, self.START_RAW)
        self.fsm.add_transition(self.RESTART, self.COOKING, None, self.START_RAW)
        self.fsm.add_transition(self.RESTART, self.DONE, None, self.START_RAW)
        self.fsm.add_transition(self.RESTART, self.RAW, None, self.START_RAW)


    def get_state(self):
        return self.fsm.current_state

    def update(self, input=None):
        self.fsm.process(input)
        print('proccessing')

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x + 100, self.rect.y + 100))

