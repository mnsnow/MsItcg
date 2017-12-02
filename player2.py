import pygame
import sys
from card_database import *
from card import Monster, Character

class Player2():
    def __init__(self):

        self.deck_list = [
            # Set 1
            card_01_01, card_01_03, card_01_04, card_01_06,
            card_01_13,
            card_01_23, card_01_25, card_01_27, card_01_28, card_01_29,
            card_01_31, card_01_33, card_01_36,
            card_01_42,
            card_01_50, card_01_55, card_05_56, card_01_58,
            card_01_61, card_01_62,
            card_01_73, card_01_77, card_01_78,
            card_01_85, card_01_86, card_01_88,
            card_01_94, card_01_95,
            # Set 2
            card_02_11, card_02_18, card_02_19,
            card_02_20, card_02_24, card_02_25,
            card_02_30, card_02_31, card_02_35, card_02_38,
            # Set 3
            card_03_01, card_03_09,
            card_03_10,
            card_03_25, card_03_29,
            card_03_38,
            card_03_45,
            card_03_57, card_03_60,
            # Set 4
            card_04_04, card_04_05, card_04_06,
            card_04_10, card_04_12,
            card_04_23, card_04_26, card_04_29,
            card_04_38,
            card_04_41, card_04_42, card_04_44,
            card_04_51, card_04_59,
            # Set 5
            card_05_02,
            card_05_21, card_05_23, card_05_24,
            card_05_40,
            card_05_50, card_05_58,
            card_05_72, card_05_77, card_05_79,
            card_05_86,

            ]

        self.character_card = card_01_21

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
        self.item_in_play_dict = {
            '1' : '',
            '2' : '',
            '3' : '',
            '4' : '',
            '5' : '',
            '6' : '',
        }








# --
