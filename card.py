import sys
import pygame
from settings import Settings



class Card():

    def __init__(self, set_number, card_number, card_type, job, level,
    attack, health, lv_type, lv_active_level, special_effect,ai_settings = Settings(), duplicate = 1):

        self.set_number = set_number
        self.card_number = card_number
        self.card_type = card_type
        self.job = job
        self.level = level
        self.attack = attack
        self.health = health
        self.lv_type = lv_type
        self.lv_active_level = lv_active_level
        self.special_effect = special_effect
        self.duplicate = duplicate


        self.image = self.image_raw = pygame.image.load('static/images/monster/' + self.set_number + '_' + self.card_number + '.jpg')
        self.image = pygame.transform.scale(self.image_raw,(ai_settings.card_size_x, ai_settings.card_size_y))
        self.rect = self.image.get_rect()

    #   Comment out since we don't want to input screen into this class
    #     self.screen_rect = self.screen.get_rect()
    #
    # def blitme(self):
    #     self.screen.blit(self.image, self.rect)






#-----
