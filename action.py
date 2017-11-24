import sys
import pygame, pygame.mixer
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from button import Button
from display import Screen_status, Button_status
from grid import Grid
import card_database_functions as cdf
from user import User


class Action():
    """ Everything regarding stage two and stage 3 action"""
    def __init__(self):
        self.stage = '2'



    def stage_2_spawn(self, action_number, screen,buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-action-detail-1-spawn'
        button_status.battle_screen_instruction_bar_text = 'Pick a monster lv' + str(action_number) + ' or less and click yes to play.'









#---
