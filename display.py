import sys
import pygame

class Mouse_status():
    """ Control active status of mouse action"""
    def __init__(self, mousebuttondown_status = False):
        self.mousebuttondown_status = mousebuttondown_status



class Screen_status():
    """ Control active status of all screens"""
    def __init__(self, welcome_screen = False, build_deck_screen = False, battle_screen = True):

        self.welcome_screen = welcome_screen
        self.build_deck_screen = build_deck_screen
        self.battle_screen = battle_screen





class Button_status():
    """ Control active status of all buttons"""
    def __init__(self, monster_handaction_display=False,monster_handaction_backend=True,
    monster_battleaction_display=False,monster_battleaction_backend=True, menu_rules=False):

        self.monster_handaction_display = monster_handaction_display
        self.monster_handaction_backend = monster_handaction_backend
        self.monster_battleaction_display = monster_battleaction_display
        self.monster_battleaction_backend = monster_battleaction_backend
        self.menu_rules = menu_rules
