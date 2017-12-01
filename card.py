import sys
import pygame
from settings import Settings


class Character():

    def __init__(self, set_number, card_number, card_type, job, level,
    health, skill_1_lv, skill_1_type, skill_2_lv, skill_2_type, skill_3_lv, skill_3_type,
    ai_settings = Settings(), duplicate = 1 ):
        self.set_number = set_number
        self.card_number = card_number
        self.card_type = card_type
        self.job = job
        self.level = level
        self.health = health
        self.skill_1_lv = skill_1_lv
        self.skill_1_type = skill_1_type
        self.skill_2_lv = skill_2_lv
        self.skill_2_type = skill_2_type
        self.skill_3_lv = skill_3_lv
        self.skill_3_type = skill_3_type
        self.duplicate = duplicate


        self.image = self.image_raw = pygame.image.load('static/images/in_game/character/' + self.set_number + '_' + self.card_number + '.jpg')
        self.image = pygame.transform.scale(self.image_raw,(ai_settings.card_size_x, ai_settings.card_size_y))
        self.rect = self.image.get_rect()

class Monster():

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


        self.image_zoom = pygame.image.load('static/images/in_game_zoom/monster/' + self.set_number + '_' + self.card_number + '.jpg')

        self.rect_zoom = self.image_zoom.get_rect()

        self.image = self.image_raw = pygame.image.load('static/images/in_game/monster/' + self.set_number + '_' + self.card_number + '.jpg')
        self.image = pygame.transform.scale(self.image_raw,(ai_settings.card_size_x, ai_settings.card_size_y))
        self.rect = self.image.get_rect()

        self.bottom_image = self.image_raw = pygame.image.load('static/images/in_game/monster/monster_bottom/' + self.set_number + '_' + self.card_number + '.jpg')
        self.bottom_image = pygame.transform.scale(self.image_raw,(ai_settings.card_bottom_size_x, ai_settings.card_bottom_size_y))
        self.bottom_rect = self.bottom_image.get_rect()

        self.top_image = self.image_raw = pygame.image.load('static/images/in_game/monster/monster_top/' + self.set_number + '_' + self.card_number + '.jpg')
        self.top_image = pygame.transform.scale(self.image_raw,(ai_settings.card_top_size_x, ai_settings.card_top_size_y))
        self.top_rect = self.top_image.get_rect()


class Tactic():

    def __init__(self, set_number, card_number, card_type, job, level,
    lv_type, lv_active_level, special_effect,ai_settings = Settings(), duplicate = 1):

        self.set_number = set_number
        self.card_number = card_number
        self.card_type = card_type
        self.job = job
        self.level = level
        self.lv_type = lv_type
        self.lv_active_level = lv_active_level
        self.special_effect = special_effect
        self.duplicate = duplicate

        self.image_zoom = pygame.image.load('static/images/in_game_zoom/tactic/' + self.set_number + '_' + self.card_number + '.jpg')

        self.rect_zoom = self.image_zoom.get_rect()

        self.image = self.image_raw = pygame.image.load('static/images/in_game/tactic/' + self.set_number + '_' + self.card_number + '.jpg')
        self.image = pygame.transform.scale(self.image_raw,(ai_settings.card_size_x, ai_settings.card_size_y))
        self.rect = self.image.get_rect()

        self.bottom_image = self.image_raw = pygame.image.load('static/images/in_game/tactic/tactic_bottom/' + self.set_number + '_' + self.card_number + '.jpg')
        self.bottom_image = pygame.transform.scale(self.image_raw,(ai_settings.card_bottom_size_x, ai_settings.card_bottom_size_y))
        self.bottom_rect = self.bottom_image.get_rect()

class Item():

    def __init__(self, set_number, card_number, card_type, job, level,
    lv_type, lv_active_level, special_effect,ai_settings = Settings(), duplicate = 1):

        self.set_number = set_number
        self.card_number = card_number
        self.card_type = card_type
        self.job = job
        self.level = level
        self.lv_type = lv_type
        self.lv_active_level = lv_active_level
        self.special_effect = special_effect
        self.duplicate = duplicate

        self.image_zoom = pygame.image.load('static/images/in_game_zoom/item/' + self.set_number + '_' + self.card_number + '.jpg')

        self.rect_zoom = self.image_zoom.get_rect()

        self.image = self.image_raw = pygame.image.load('static/images/in_game/item/' + self.set_number + '_' + self.card_number + '.jpg')
        self.image = pygame.transform.scale(self.image_raw,(ai_settings.card_size_x, ai_settings.card_size_y))
        self.rect = self.image.get_rect()

        self.bottom_image = self.image_raw = pygame.image.load('static/images/in_game/item/item_bottom/' + self.set_number + '_' + self.card_number + '.jpg')
        self.bottom_image = pygame.transform.scale(self.image_raw,(ai_settings.card_bottom_size_x, ai_settings.card_bottom_size_y))
        self.bottom_rect = self.bottom_image.get_rect()

        self.top_image = self.image_raw = pygame.image.load('static/images/in_game/item/item_top/' + self.set_number + '_' + self.card_number + '.jpg')
        self.top_image = pygame.transform.scale(self.image_raw,(int(ai_settings.card_top_size_x * 0.80), int(ai_settings.card_top_size_y * 0.75)))
        self.top_rect = self.top_image.get_rect()





#-----
