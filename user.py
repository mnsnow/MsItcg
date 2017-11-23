import sys
import pygame
from card_database import *

class User():
    """Contains informations of user's customatic informations"""
    def __init__(self, deck_list = [
    card_01_05, card_01_06, card_01_08,
    card_01_11, card_01_13, card_01_14,
    card_01_23, card_01_27,
    card_01_31, card_01_34,
    card_01_40,
    card_01_53,
    card_01_60, card_01_61, card_01_65, card_01_66, card_01_69,
    card_01_70, card_01_71, card_01_76, card_01_77,
    card_01_81, card_01_86, card_01_87,
    card_01_90, card_01_93, card_01_95, card_01_96,
    ], character_card = card_01_16, hand_list = [],
    character_level_10_card = '',
    character_level_20_card = '',
    character_level_30_card = '',
    character_level_40_card = '',
    character_level_50_card = '',
    character_level_60_card = '',
    character_level_70_card = '',
    character_level_80_card = '',
    character_level_90_card = '',
    character_level_100_card = '',
    character_level_110_card = '',
    character_level_120_card = '',
    character_level_130_card = '',
    character_level_140_card = '',
    character_level_150_card = '',
    ):

        self.deck_list = deck_list
        self.character_card = character_card
        self.hand_list = hand_list
        self.character_level_10_card = character_level_10_card
        self.character_level_20_card = character_level_20_card
        self.character_level_30_card = character_level_30_card
        self.character_level_40_card = character_level_40_card
        self.character_level_50_card = character_level_50_card
        self.character_level_60_card = character_level_60_card
        self.character_level_70_card = character_level_70_card
        self.character_level_80_card = character_level_80_card
        self.character_level_90_card = character_level_90_card
        self.character_level_100_card = character_level_100_card
        self.character_level_110_card = character_level_110_card
        self.character_level_120_card = character_level_120_card
        self.character_level_130_card = character_level_130_card
        self.character_level_140_card = character_level_140_card
        self.character_level_150_card = character_level_150_card
