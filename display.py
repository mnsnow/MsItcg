import sys
import pygame

class Mouse_status():
    """ Control active status of mouse action"""
    def __init__(self, mousebuttondown_status = False):
        self.mousebuttondown_status = mousebuttondown_status

    def mousebuttondown_status_active(self):
        self.mousebuttondown_status = True

    def mousebuttondown_status_deactive(self):
        self.mousebuttondown_status = False


class Screen_status():
    """ Control active status of all screens"""
    def __init__(self, welcome_screen = False, build_deck_screen = False, battle_screen = True):

        self.welcome_screen = welcome_screen
        self.build_deck_screen = build_deck_screen
        self.battle_screen = battle_screen



    def battle_screen_active(self):
        self.battle_screen = True

    def battle_screen_deactive(self):
        self.battle_screen = False


    def build_deck_screen_active(self):
        self.build_deck_screen = True

    def build_deck_screen_deactive(self):
        self.build_deck_screen = False


    def welcome_screen_active(self):
        self.welcome_screen = True

    def welcome_screen_deactive(self):
        self.welcome_screen = False





class Button_status():
    """ Control active status of all buttons"""
    def __init__(self, monster_handaction_display=False,monster_handaction_backend=True, monster_battleaction_display=False, menu_rules=False):

        self.monster_handaction_display = monster_handaction_display
        self.monster_handaction_backend = monster_handaction_backend
        self.monster_battleaction_display = monster_battleaction_display
        self.menu_rules = menu_rules


    def monster_handaction_display_active(self):
        self.monster_handaction_display = True

    def monster_handaction_display_deactive(self):
        self.monster_handaction_display = False


    def monster_battleaction_display_active(self):
        self.monster_battleaction_display = True

    def monster_battleaction_display_deactive(self):
        self.monster_battleaction_display = False

    def menu_rules_active(self):
        self.menu_rules = True

    def menu_rules_deactive(self):
        self.menu_rules = False
