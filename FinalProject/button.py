import pygame

class Button(pygame.Rect): 
    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height)
        self.name = name

    def draw(self, screen):
        pygame.draw.rect(screen, 'Red', self)
        font = pygame.font.Font(None, 36)  # You can adjust the font size as needed
        text = font.render(self.name, True, (255, 255, 255))  # White text
        text_rect = text.get_rect(center=self.center)
        screen.blit(text, text_rect)
