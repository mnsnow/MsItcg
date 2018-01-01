import pygame
import sys
import random
from card_database import *
from card import Monster, Character

class Player2():
    def __init__(self):

        self.identity = 'AI' #identify player2 is AI or a real person

        self.deck_list = [
            # # Set 1
            # card_01_01, card_01_03, card_01_04, card_01_06,
            # card_01_13,
            # card_01_23, card_01_25, card_01_27, card_01_28, card_01_29,
            # card_01_31, card_01_33, card_01_36,
            # card_01_42, card_01_43,
            # card_01_50, card_01_55, card_05_56, card_01_58,
            # card_01_61, card_01_62,
            # card_01_73, card_01_77, card_01_78,
            # card_01_85, card_01_86, card_01_88,
            # card_01_94, card_01_95,
            # # Set 2
            # card_02_11, card_02_18, card_02_19,
            # card_02_20, card_02_25,
            # card_02_30, card_02_31, card_02_35, card_02_38,
            # # Set 3
            # card_03_01, card_03_09,
            # card_03_10,
            # card_03_25, card_03_29,
            # card_03_38,
            # card_03_45,
            # card_03_57, card_03_60,
            # # Set 4
            # card_04_04, card_04_05, card_04_06,
            # card_04_10, card_04_12,
            # card_04_23, card_04_26, card_04_29,
            # card_04_38,
            # card_04_41, card_04_42, card_04_44,
            # card_04_51, card_04_59,
            # # Set 5
            # card_05_02,
            # card_05_21, card_05_23, card_05_24,
            # card_05_40,
            # card_05_50, card_05_58,
            # card_05_72, card_05_77, card_05_79,
            # card_05_86,

            ]

        self.NIXIE_DECK = str(['CARD_01_03', 'CARD_01_03', 'CARD_01_03', 'CARD_03_01', 'CARD_03_01', 'CARD_03_01', 'CARD_03_01', 'CARD_03_09', 'CARD_03_09', 'CARD_03_09', 'CARD_03_09', 'CARD_04_04', 'CARD_04_04', 'CARD_04_04', 'CARD_04_04', 'CARD_04_12', 'CARD_04_12', 'CARD_04_12', 'CARD_04_12', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61', 'CARD_03_38', 'CARD_03_38', 'CARD_03_38', 'CARD_03_38', 'CARD_04_41', 'CARD_04_41', 'CARD_04_41', 'CARD_04_41', 'CARD_01_03', 'CARD_05_77', 'CARD_05_77', 'CARD_05_77', 'CARD_05_77', 'CARD_04_51', 'CARD_04_51', 'CARD_04_51', 'CARD_04_51'])
        self.MAYA_DECK = str(['CARD_01_28', 'CARD_01_28', 'CARD_01_28', 'CARD_01_28', 'CARD_01_43', 'CARD_01_43', 'CARD_01_43', 'CARD_01_43', 'CARD_02_18', 'CARD_02_18', 'CARD_02_18', 'CARD_02_18', 'CARD_05_21', 'CARD_05_21', 'CARD_05_21', 'CARD_05_21', 'CARD_04_23', 'CARD_04_23', 'CARD_04_23', 'CARD_04_23', 'CARD_03_25', 'CARD_03_25', 'CARD_03_25', 'CARD_03_25', 'CARD_01_01', 'CARD_01_01', 'CARD_01_01', 'CARD_01_01', 'CARD_01_85', 'CARD_01_85', 'CARD_01_85', 'CARD_01_85', 'CARD_04_51', 'CARD_04_51', 'CARD_04_51', 'CARD_04_51', 'CARD_01_58', 'CARD_01_58', 'CARD_01_58', 'CARD_01_58'])
        self.IVAN_DECK = str(['CARD_01_58', 'CARD_01_58', 'CARD_01_58', 'CARD_01_58', 'CARD_01_62', 'CARD_01_62', 'CARD_01_62', 'CARD_01_62', 'CARD_02_38', 'CARD_02_38', 'CARD_02_38', 'CARD_02_38', 'CARD_03_38', 'CARD_03_38', 'CARD_03_38', 'CARD_03_38', 'CARD_04_41', 'CARD_04_41', 'CARD_04_41', 'CARD_01_03', 'CARD_01_03', 'CARD_01_03', 'CARD_01_03', 'CARD_03_01', 'CARD_03_01', 'CARD_03_01', 'CARD_03_01', 'CARD_04_41', 'CARD_03_57', 'CARD_03_57', 'CARD_03_57', 'CARD_03_57', 'CARD_04_51', 'CARD_04_51', 'CARD_04_51', 'CARD_04_51', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61'])
        self.MISTMOON_DECK = str(['CARD_01_23', 'CARD_01_23', 'CARD_01_23', 'CARD_01_23', 'CARD_01_55', 'CARD_01_55', 'CARD_01_55', 'CARD_01_55', 'CARD_01_43', 'CARD_01_43', 'CARD_01_43', 'CARD_01_43', 'CARD_01_85', 'CARD_01_85', 'CARD_01_85', 'CARD_01_85', 'CARD_03_25', 'CARD_03_25', 'CARD_03_25', 'CARD_03_25', 'CARD_03_38', 'CARD_03_38', 'CARD_03_38', 'CARD_03_38', 'CARD_03_57', 'CARD_03_57', 'CARD_03_57', 'CARD_03_57', 'CARD_04_42', 'CARD_04_42', 'CARD_04_42', 'CARD_04_42', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61', 'CARD_01_13', 'CARD_01_13', 'CARD_01_13', 'CARD_01_13'])
        self.SHERMAN_DECK = str(['CARD_01_78', 'CARD_01_78', 'CARD_01_78', 'CARD_01_78', 'CARD_01_86', 'CARD_01_86', 'CARD_01_86', 'CARD_01_86', 'CARD_01_77', 'CARD_01_77', 'CARD_01_77', 'CARD_01_77', 'CARD_01_95', 'CARD_01_95', 'CARD_01_95', 'CARD_01_95', 'CARD_05_56', 'CARD_05_56', 'CARD_05_56', 'CARD_05_56', 'CARD_05_77', 'CARD_05_77', 'CARD_05_77', 'CARD_05_77', 'CARD_01_13', 'CARD_01_13', 'CARD_01_13', 'CARD_01_23', 'CARD_01_23', 'CARD_01_23', 'CARD_01_23', 'CARD_01_13', 'CARD_01_27', 'CARD_01_27', 'CARD_01_27', 'CARD_01_27', 'CARD_01_31', 'CARD_01_31', 'CARD_01_31', 'CARD_01_31', 'CARD_02_20', 'CARD_02_20', 'CARD_04_59', 'CARD_04_59', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61', 'CARD_03_45', 'CARD_03_45', 'CARD_03_45', 'CARD_03_45', 'CARD_05_86', 'CARD_05_86'])
        self.MOBY_DECK = str(['CARD_01_13', 'CARD_01_13', 'CARD_01_13', 'CARD_01_13', 'CARD_01_23', 'CARD_01_23', 'CARD_01_23', 'CARD_01_23', 'CARD_01_27', 'CARD_01_27', 'CARD_01_27', 'CARD_01_27', 'CARD_01_31', 'CARD_01_31', 'CARD_01_31', 'CARD_01_31', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61', 'CARD_01_77', 'CARD_01_77', 'CARD_01_77', 'CARD_01_77', 'CARD_01_86', 'CARD_01_86', 'CARD_01_86', 'CARD_01_86', 'CARD_01_95', 'CARD_01_95', 'CARD_01_95', 'CARD_01_95', 'CARD_02_25', 'CARD_02_25', 'CARD_02_25', 'CARD_02_25', 'CARD_03_45', 'CARD_03_45', 'CARD_03_45', 'CARD_03_45', 'CARD_04_06', 'CARD_04_06', 'CARD_04_06', 'CARD_04_06', 'CARD_05_23', 'CARD_05_23', 'CARD_05_23', 'CARD_05_23', 'CARD_05_77', 'CARD_05_77', 'CARD_05_77', 'CARD_05_77'])
        self.MAHIBANG_DECK = str(['CARD_01_28', 'CARD_01_28', 'CARD_01_28', 'CARD_01_28', 'CARD_01_43', 'CARD_01_43', 'CARD_01_43', 'CARD_01_43', 'CARD_02_18', 'CARD_02_18', 'CARD_02_18', 'CARD_02_18', 'CARD_05_21', 'CARD_05_21', 'CARD_05_21', 'CARD_05_21', 'CARD_04_23', 'CARD_04_23', 'CARD_04_23', 'CARD_04_23', 'CARD_03_25', 'CARD_03_25', 'CARD_03_25', 'CARD_03_25', 'CARD_01_01', 'CARD_01_01', 'CARD_01_01', 'CARD_01_01', 'CARD_01_85', 'CARD_01_85', 'CARD_01_85', 'CARD_01_85', 'CARD_04_51', 'CARD_04_51', 'CARD_04_51', 'CARD_04_51', 'CARD_01_58', 'CARD_01_58', 'CARD_01_58', 'CARD_01_58'])
        self.FANGBLADE_DECK = str(['CARD_01_78', 'CARD_01_78', 'CARD_01_78', 'CARD_01_78', 'CARD_01_86', 'CARD_01_86', 'CARD_01_86', 'CARD_01_86', 'CARD_01_77', 'CARD_01_77', 'CARD_01_77', 'CARD_01_77', 'CARD_01_95', 'CARD_01_95', 'CARD_01_95', 'CARD_01_95', 'CARD_05_56', 'CARD_05_56', 'CARD_05_56', 'CARD_05_56', 'CARD_05_77', 'CARD_05_77', 'CARD_05_77', 'CARD_05_77', 'CARD_01_13', 'CARD_01_13', 'CARD_01_13', 'CARD_01_23', 'CARD_01_23', 'CARD_01_23', 'CARD_01_23', 'CARD_01_13', 'CARD_01_27', 'CARD_01_27', 'CARD_01_27', 'CARD_01_27', 'CARD_01_31', 'CARD_01_31', 'CARD_01_31', 'CARD_01_31', 'CARD_02_20', 'CARD_02_20', 'CARD_04_59', 'CARD_04_59', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61', 'CARD_01_61', 'CARD_03_45', 'CARD_03_45', 'CARD_03_45', 'CARD_03_45', 'CARD_05_86', 'CARD_05_86'])


        self.character_ai_index = '0'
        self.ai_difficulty_index = '0'

        self.character_card = card_01_16

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

        self.monster_in_play_dict = {
            '1' : '',
            '2' : '',
            '3' : '',
            '4' : '',
            '5' : '',
            '6' : '',
        }

        self.monster_in_play_length = '0'

        self.item_in_play_dict = {
            '1' : '',
            '2' : '',
            '3' : '',
            '4' : '',
            '5' : '',
            '6' : '',
        }
        self.item_in_play_length = '0'

        self.random_deck_list = random.sample(self.deck_list, len(self.deck_list))

        self.remain_deck_list = self.random_deck_list[6:]
        self.hand_list = self.random_deck_list[0:30]

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




# --
