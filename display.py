import sys
import pygame




class Screen_status():
    """ Control active status of all screens"""
    def __init__(self):

        self.welcome_screen_display = False
        self.build_deck_screen_display = False
        self.battle_screen_display = True

        self.welcome_screen_backend = True
        self.build_deck_screen_card_gallery_page_id = 1
        self.build_deck_screen_my_deck_page_id = 1
        self.build_deck_screen_to_battle_screen_all_clear = True

        self.battle_screen_my_hand_page_id = 1
        self.battle_screen_action_indicator = 'stage-0'




class Button_status():
    """ Control active status of all buttons"""
    def __init__(self):

        self.build_deck_screen_stable_button_backend = True
        self.build_deck_screen_card_gallery_button_backend = True
        self.build_deck_screen_my_deck_button_backend = True

        self.battle_screen_instruction_bar_text = 'Welcome to Maplestory Itcg Alpha!'
        self.battle_screen_instruction_bar_yes_display = True
        self.battle_screen_instruction_bar_yes_backend = True
        self.battle_screen_instruction_bar_skip_display = False
        self.battle_screen_instruction_bar_skip_backend = False
        self.battle_screen_instruction_bar_button_backend = True
        self.battle_screen_stable_button_backend = True
        self.battle_screen_my_hand_page_change_button_backend = True

        self.battle_screen_my_hand_indicator_display = False
        self.battle_screen_my_hand_indicator_position = '1'
        self.battle_screen_battleaction_display = False
        self.battle_screen_battleaction_backend = True








#--------------
