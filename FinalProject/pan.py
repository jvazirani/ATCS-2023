# pan.py
from fsm import FSM
import pygame

class Pan:
    COOKING = 'cooking'
    RAW = 'raw'
    DONE = 'done'
    BURNED = 'burned'

    # Inputs
    TIMER_UP = "tu"
    FINISH = 'finish'
    START  = 'start timer'
    RESTART = 'restart'

    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load("pan.png")
        self.image = pygame.transform.scale(self.image, (game.pan_width, game.pan_height))
        self.rect = self.image.get_rect()

        # Create the finite state machine with initial state
        self.fsm = FSM(self.RAW)
        self.init_fsm()

    def init_fsm(self):
        self.fsm.add_transition(self.START, self.RAW, None, self.COOKING)
        self.fsm.add_transition(self.TIMER_UP, self.COOKING, None, self.DONE)
        self.fsm.add_transition(self.TIMER_UP, self.DONE, None, self.BURNED)
        self.fsm.add_transition(self.BURNED, self.RESTART, None, self.RAW)
        self.fsm.add_transition(self.COOKING, self.RESTART, None, self.RAW)
        self.fsm.add_transition(self.DONE, self.RESTART, None, self.RAW)

    def get_state(self):
        return self.fsm.current_state
    
    def update(self):
        self.fsm.process(self.get_next_space())

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
