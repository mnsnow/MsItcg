import sys
import pygame
from card import Card
from card_database import *

card_list = [
    card_01_13, card_01_23, card_01_27, card_01_31, card_01_40, card_01_65, card_01_69, card_01_70, card_01_77, card_01_86, card_01_90,
    card_02_01, card_02_02, card_02_25, card_02_29, card_02_47, card_02_49,
    card_03_43, card_03_56,
    card_04_08, card_04_20, card_04_27, card_04_34, card_04_55, card_04_60,
    card_05_23, card_05_25, card_05_52, card_05_77,
]

def card_all(input_list = card_list):
    """Return all card"""
    return input_list
