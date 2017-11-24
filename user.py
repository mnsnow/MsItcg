import sys
import pygame
from card_database import *
from card import Monster, Character

class User():
    """Contains informations of user's customatic informations"""
    def __init__(self):

        self.deck_list = [
            card_01_05, card_01_06, card_01_08,
            card_01_11, card_01_13, card_01_14,
            card_01_23, card_01_27,
            card_01_31, card_01_34,
            card_01_40,
            card_01_53,
            card_01_60, card_01_61, card_01_65, card_01_66, card_01_69,
            card_01_70, card_01_71, card_01_76, card_01_77,
            card_01_81, card_01_86, card_01_87,
            card_01_90, card_01_93, card_01_95, card_01_96,]

        self.character_card = card_01_16
        self.hand_list = []
        self.monster_in_play_dict = {
            '1' : '',
            '2' : '',
            '3' : '',
            '4' : '',
            '5' : '',
            '6' : '',
        }

        self.character_under_card_by_level = {
            '10' : '',
            '20' : '',
            '30' : '',
            '40' : '',
            '50' : '',
            '60' : '',
            '70' : '',
            '80' : '',
            '90' : '',
            '100' : '',
            '110' : '',
            '120' : '',
            '130' : '',
            '140' : '',
            '150' : '',
        }
        self.stage_2_other_card_usable_list = []


    def get_stage_2_other_card_usable_list(self):
        """ Get list available at stage-2-other-actions at a given player level"""
        stage_2_other_card_complete_list = [
            self.character_under_card_by_level['10'],
            self.character_under_card_by_level['20'],
            self.character_under_card_by_level['30'],
            self.character_under_card_by_level['40'],
            self.character_under_card_by_level['50'],
            self.character_under_card_by_level['60'],
            self.character_under_card_by_level['70'],
            self.character_under_card_by_level['80'],
            self.character_under_card_by_level['90'],
            self.character_under_card_by_level['100'],
            self.character_under_card_by_level['110'],
            self.character_under_card_by_level['120'],
            self.character_under_card_by_level['130'],
            self.character_under_card_by_level['140'],
            self.character_under_card_by_level['150'],
        ]

        stage_2_other_card_usable_list = []

        for card in stage_2_other_card_complete_list:
            if card != '':
                if int(card.lv_active_level) <= int(self.character_card.level):
                    stage_2_other_card_usable_list.append(card)

        return stage_2_other_card_usable_list








#---
