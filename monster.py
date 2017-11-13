import pygame
import sys

class Monster():

    def __init__(self, screen):

        self.screen = screen

        self.image_raw = pygame.image.load('static/images/character/monster_1.jpg')
        self.image_size_x = 220
        self.image_size_y = 300
        self.image = pygame.transform.scale(self.image_raw,(self.image_size_x, self.image_size_y))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = 500
        self.rect.y = 400

    def blitme(self, x, y):
        self.screen.blit(self.image, (x,y))
