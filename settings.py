import sys
import pygame

class Settings():

    def __init__(self):

        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100,3,3)

        self.sound_indicator = True
        self.music_indicator = True

        self.theme_indicator = 'Lith Harbor'

        self.AI_speed_indicator = '2000'# fast = 1000, normal = 2000, slow = 3000

        #Cards Settings
        self.card_size_x = 130
        self.card_size_y = 180

        self.card_bottom_size_x = 130
        self.card_bottom_size_y = 23

        self.card_top_size_x = 130
        self.card_top_size_y = 80
