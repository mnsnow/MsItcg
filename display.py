import sys
import pygame




class Screen_status():
    """ Control active status of all screens"""
    def __init__(self, welcome_screen_display = False, build_deck_screen_display = False, battle_screen_display = True,  # Main screen settings
        # Other settings
        welcome_screen_backend = True,
        build_deck_screen_card_gallery_page_id = 1,build_deck_screen_my_deck_page_id = 1, build_deck_screen_to_battle_screen_all_clear = True,
        battle_screen_action_indicator = 'stage-0', battle_screen_my_hand_page_id = 1,):

        self.welcome_screen_display = welcome_screen_display
        self.welcome_screen_backend = welcome_screen_backend
        self.build_deck_screen_display = build_deck_screen_display
        self.build_deck_screen_card_gallery_page_id = build_deck_screen_card_gallery_page_id
        self.build_deck_screen_my_deck_page_id = build_deck_screen_my_deck_page_id
        self.build_deck_screen_to_battle_screen_all_clear = build_deck_screen_to_battle_screen_all_clear

        self.battle_screen_display = battle_screen_display
        self.battle_screen_my_hand_page_id = battle_screen_my_hand_page_id
        self.battle_screen_action_indicator = battle_screen_action_indicator # p1: level up




class Button_status():
    """ Control active status of all buttons"""
    def __init__(self,
    build_deck_screen_stable_button_backend = True,
    build_deck_screen_card_gallery_button_backend = True,
    build_deck_screen_my_deck_button_backend = True,
    battle_screen_instruction_bar_button_backend = True,
    battle_screen_stable_button_backend = True,
    battle_screen_my_hand_page_change_button_backend = True,
    battle_screen_handaction_display = False, battle_screen_handaction_display_position = '1',battle_screen_handaction_backend=True,
    battle_screen_battleaction_display=False,battle_screen_battleaction_backend=True,):

        self.build_deck_screen_stable_button_backend = build_deck_screen_stable_button_backend
        self.build_deck_screen_card_gallery_button_backend = build_deck_screen_card_gallery_button_backend
        self.build_deck_screen_my_deck_button_backend = build_deck_screen_my_deck_button_backend

        self.battle_screen_instruction_bar_button_backend = battle_screen_instruction_bar_button_backend
        self.battle_screen_stable_button_backend = battle_screen_stable_button_backend
        self.battle_screen_my_hand_page_change_button_backend = battle_screen_my_hand_page_change_button_backend

        self.battle_screen_handaction_display = battle_screen_handaction_display
        self.battle_screen_handaction_display_position = battle_screen_handaction_display_position
        self.battle_screen_handaction_backend = battle_screen_handaction_backend
        self.battle_screen_battleaction_display = battle_screen_battleaction_display
        self.battle_screen_battleaction_backend = battle_screen_battleaction_backend








#--------------
