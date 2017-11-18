import sys
import pygame

class Mouse_status():
    """ Control active status of mouse action"""
    def __init__(self, mousebuttondown_status = False):
        self.mousebuttondown_status = mousebuttondown_status



class Screen_status():
    """ Control active status of all screens"""
    def __init__(self, welcome_screen_display = False,  build_deck_screen_display = True, battle_screen_display = False,
        build_deck_screen_card_gallery_page_id = 1, welcome_screen_backend = True):

        self.welcome_screen_display = welcome_screen_display
        self.welcome_screen_backend = welcome_screen_backend
        self.build_deck_screen_display = build_deck_screen_display
        self.build_deck_screen_card_gallery_page_id = build_deck_screen_card_gallery_page_id
        self.battle_screen_display = battle_screen_display

    # def build_deck_screen_card_gallery_switch_page(self, build_deck_screen_card_gallery_page_id):
    #     """ Control pages switching on card gallery part"""
    #     self.build_deck_screen_card_gallery_page_id = build_deck_screen_card_gallery_page_id







class Button_status():
    """ Control active status of all buttons"""
    def __init__(self, monster_handaction_display=False,monster_handaction_backend=True,
    monster_battleaction_display=False,monster_battleaction_backend=True, menu_rules=False):

        self.monster_handaction_display = monster_handaction_display
        self.monster_handaction_backend = monster_handaction_backend
        self.monster_battleaction_display = monster_battleaction_display
        self.monster_battleaction_backend = monster_battleaction_backend
        self.menu_rules = menu_rules
