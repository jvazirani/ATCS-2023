# food.py
import pygame

class Food:
    # Each food has a name, a cooking time range, and three images
    def __init__(self, name, cooking_time_range, raw_image, cooked_image, burned_image):
        self.name = name
        self.cooking_time_range = cooking_time_range
        self.cook_time = 0
        self.image_raw = pygame.image.load(raw_image)  
        self.image_cooked = pygame.image.load(cooked_image)  
        self.image_burned = pygame.image.load(burned_image)  
        self.image = self.image_raw

    # Keeps track of current time cooking
    def update_cook_time(self, elapsed_time):
        self.cook_time += elapsed_time
        
    def reset_cook_time(self):
        self.cook_time = 0
    # Checks if the food is cooked, burned, or raw based on if it is in the range of the cooking time
    def is_cooked(self):
        print(self.cook_time)
        print(self.cooking_time_range)
        return self.cook_time >= self.cooking_time_range[0] and self.cook_time <= self.cooking_time_range[1]

    def is_burned(self):
        return self.cook_time > self.cooking_time_range[1]

    def is_raw(self):
        return self.cook_time < self.cooking_time_range[0]

    def draw(self, screen, x, y):
        screen.blit(self.image, (x + 50, y)) 

    def draw_raw(self, screen, x, y):
        screen.blit(self.image_raw, (x - 50, y))  # Adjust the offset (-50) based on your preference

    def draw_cooked(self, screen, x, y):
        screen.blit(self.image_cooked, (x - 50, y))  # Adjust the offset (-50) based on your preference

    def draw_burned(self, screen, x, y):
        screen.blit(self.image_burned, (x - 50, y))  # Adjust the offset (-50) based on your preference

        

