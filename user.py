import sys
import pygame

class User():
    """Contains informations of user's customatic informations"""
    def __init__(self, card_list = [], character_list = []):

        self.card_list = card_list
        self.character_list = character_list
