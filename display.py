import sys
import pygame




class Screen_status():
    """ Control active status of all screens"""
    def __init__(self):

        self.time_last = pygame.time.get_ticks() # For player2(AI) use only
        self.time_player2_cooldown = 3000

        self.welcome_screen_display = False
        self.prepare_screen_display = True
        self.build_deck_screen_display = False
        self.battle_screen_display = False

        self.welcome_screen_backend = True
        self.build_deck_screen_card_gallery_page_id = 1
        self.build_deck_screen_my_deck_page_id = 1


        self.battle_screen_my_hand_page_id = 1
        self.battle_screen_action_indicator = 'stage-0'

        self.battle_screen_player2_action_display_indicator = False





class Button_status():
    """ Control active status of all buttons"""
    def __init__(self):

        self.prepare_screen_end_screen_warning_button_display = ''

        self.build_deck_screen_stable_button_backend = True
        self.build_deck_screen_card_gallery_button_backend = True
        self.build_deck_screen_my_deck_button_backend = True
        self.build_deck_screen_end_screen_warning_button_display = ''

        self.battle_screen_instruction_bar_text = 'Welcome to Maplestory Itcg Alpha!'
        self.battle_screen_instruction_bar_yes_display = True
        self.battle_screen_instruction_bar_yes_backend = True
        self.battle_screen_instruction_bar_skip_display = False
        self.battle_screen_instruction_bar_skip_backend = False
        self.battle_screen_instruction_bar_button_backend = True
        self.battle_screen_stable_button_backend = True
        self.battle_screen_my_hand_page_change_button_backend = True

        self.battle_screen_history_bar_detail_display = False
        self.battle_screen_history_bar_text_dict = {
            '1' : '',
            '2' : '',
            '3' : '',
            '4' : '',
            '5' : '',
            '6' : '',
            '7' : '',
            '8' : '',
            '9' : '',
            '10' : '',
            '11' : '',
            '12' : '',
            '13' : '',
            '14' : '',
            '15' : '',
        }


        self.battle_screen_my_hand_indicator_display = False
        self.battle_screen_my_hand_indicator_position = '1'

        self.battle_screen_player1_battleground_indicator_display = False
        self.battle_screen_player1_battleground_indicator_position = '1'
        self.battle_screen_player2_battleground_indicator_display = False
        self.battle_screen_player2_battleground_indicator_position = '1'


        self.card_zoom_active = False
        self.card_zoom_screen_indicator = 'build_deck_screen'
        self.card_zoom_part_indicator = ''
        self.card_zoom_position_indicator = '1'

        self.battle_screen_win_lost_indicator = ''






#--------------
