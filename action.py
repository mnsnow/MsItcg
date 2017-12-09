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



    def stage_2_easy_shot(self, caster_type, screen,buttons, screen_status, button_status, card_database_filter, user, under_position = '1'):
        """ Easy shot/Stab/"""
        if caster_type == 'character':
            screen_status.battle_screen_action_indicator = 'stage-2-character-action-' + under_position + '-detail-easy-shot'
        elif caster_type == 'other':
            screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-easy-shot'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = "Pick a target to deal 10 damage"

    def stage_2_tricky_shot(self, caster_type, screen,buttons, screen_status, button_status, card_database_filter, user, under_position = '1'):
        """ Tricky shot"""
        if caster_type == 'character':
            screen_status.battle_screen_action_indicator = 'stage-2-character-action-' + under_position + '-detail-tricky-shot'
        elif caster_type == 'other':
            screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-tricky-shot'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = "Pick a target to deal 20 damage"

    def stage_2_quest(self, screen,buttons, screen_status, button_status, card_database_filter, user):
        """ Quest"""
        user.hand_list.append(user.remain_deck_list[0])
        del user.remain_deck_list[0]



    def stage_2_spawn(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-spawn'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a monster lv' + str(int(action_level)) + ' or less and click yes to play.'


    def stage_2_think_fast(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-think-fast'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a tactic lv' + str(int(action_level)) + ' or less and click yes to play.'

    def stage_2_equip(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-equip'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a item lv' + str(int(action_level)) + ' or less and click yes to play.'

    def stage_2_spawn_and_think_fast(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-spawn-and-think-fast'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a monster/tactic lv' + str(int(action_level)) + ' or less and click yes to play.'

    def stage_2_spawn_and_equip(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-spawn-and-equip'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a monster/item lv' + str(int(action_level)) + ' or less and click yes to play.'

    def stage_2_think_fast_and_equip(self, under_position,  action_level, screen, buttons, screen_status, button_status, card_database_filter, user):
        """ input spawn number, output spawn action"""
        screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-think-fast-and-equip'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_text = 'Pick a tactic/item lv' + str(int(action_level)) + ' or less and click yes to play.'









#---





#---
