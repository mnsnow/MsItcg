import pygame

class Character_1():

    def __init__(self, screen):

        self.screen = screen

        self.image_raw = pygame.image.load('static/images/character/character_1.jpg')
        self.image_size_x = 220
        self.image_size_y = 300
        self.image = pygame.transform.scale(self.image_raw,(self.image_size_x, self.image_size_y))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = 100
        self.rect.y = 60

    def blitme(self):
        self.screen.blit(self.image, self.rect)



class Character_2():

    def __init__(self, screen):

        self.screen = screen

        self.image_raw = pygame.image.load('static/images/character/character_2.jpg')
        self.image_size_x = 220
        self.image_size_y = 300
        self.image = pygame.transform.scale(self.image_raw,(self.image_size_x, self.image_size_y))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = 1100 - self.image_size_x
        self.rect.y = 60

    def blitme(self):
        self.screen.blit(self.image, self.rect)
