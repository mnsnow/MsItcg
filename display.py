import sys
import pygame

class Screen_status():
    """ Control active status of all screens"""
    def __init__(self, welcome_screen = True, battle_screen = False,):

        self.welcome_screen = welcome_screen
        self.battle_screen = battle_screen



    def battle_screen_active(self):
        self.battle_screen = True

    def battle_screen_deactive(self):
        self.battle_screen = False


    def welcome_screen_active(self):
        self.welcome_screen = True

    def welcome_screen_deactive(self):
        self.welcome_screen = False





class Button_status():
    """ Control active status of all buttons"""
    def __init__(self, monster_handaction=False, monster_battleaction=False, menu_rules=False):

        self.monster_handaction = monster_handaction
        self.monster_battleaction = monster_battleaction
        self.menu_rules = menu_rules


    def monster_handaction_active(self):
        self.monster_handaction = True

    def monster_handaction_deactive(self):
        self.monster_handaction = False


    def monster_battleaction_active(self):
        self.monster_battleaction = True

    def monster_battleaction_deactive(self):
        self.monster_battleaction = False

    def menu_rules_active(self):
        self.menu_rules = True

    def menu_rules_deactive(self):
        self.menu_rules = False
