import pygame
import sys

class Tactic():

    def __init__(self, screen, ai_settings):

        self.screen = screen

        self.image_raw = pygame.image.load('static/images/character/tactic_01.jpg')
        self.image_size_x = ai_settings.card_size_x
        self.image_size_y = ai_settings.card_size_y
        self.image = pygame.transform.scale(self.image_raw,(self.image_size_x, self.image_size_y))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = 800
        self.rect.y = 500

    def blitme(self):
        self.screen.blit(self.image, self.rect)
