import sys
import pygame
from card_database import *

class User():
    """Contains informations of user's customatic informations"""
    def __init__(self, deck_list = [
    card_01_05, card_01_06, card_01_08,
    card_01_11, card_01_13, card_01_14, card_01_16,
    card_01_21, card_01_23, card_01_27,
    card_01_31, card_01_34, card_01_37,
    card_01_40, card_01_44,
    card_01_53, card_01_59,
    card_01_60, card_01_61, card_01_64, card_01_65, card_01_66, card_01_69,
    card_01_70, card_01_71, card_01_76, card_01_77,
    card_01_81, card_01_86, card_01_87, card_01_89,
    card_01_90, card_01_91, card_01_93, card_01_95, card_01_96,
    ], character_card = '', hand_list = []):

        self.deck_list = deck_list
        self.character_card = character_card
        self.hand_list = hand_list
