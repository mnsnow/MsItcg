import sys
import pygame, pygame.mixer
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from button import Button
from display import Screen_status, Button_status
from grid import Grid
import card_database_filter as cdf
from user import User


class Action():
    """ Everything regarding stage two and stage 3 action"""
    def __init__(self):
        self.stage = '2'



    def stage_2_easy_shot(self, screen,buttons, screen_status, button_status, card_database_filter, user):
        """ Easy shot/Stab/"""
        screen_status.battle_screen_action_indicator = 'stage-2-action-detail-1-easy-shot'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = "Pick a target to deal 10 damage"


    def stage_2_spawn(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-action-detail-1-spawn'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a monster lv' + str(int(action_level)) + ' or less and click yes to play.'


    def stage_2_think_fast(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-action-detail-1-think-fast'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a tactic lv' + str(int(action_level)) + ' or less and click yes to play.'

    def stage_2_equip(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-action-detail-1-equip'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a item lv' + str(int(action_level)) + ' or less and click yes to play.'

    def stage_2_spawn_and_think_fast(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-action-detail-1-spawn-and-think-fast'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a monster/tactic lv' + str(int(action_level)) + ' or less and click yes to play.'

    def stage_2_spawn_and_equip(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-action-detail-1-spawn-and-equip'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a monster/item lv' + str(int(action_level)) + ' or less and click yes to play.'

    def stage_2_think_fast_and_equip(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-action-detail-1-think-fast-and-equip'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a tactic/item lv' + str(int(action_level)) + ' or less and click yes to play.'









#---





#---
