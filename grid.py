import sys
import pygame

class Grid():
    """All grid information of all screens"""
    def __init__(self):




#------------------Building deck Screen----------------------------------------------------
        self.build_deck_screen_card_gallery_grid_size = (1100,490)
        self.build_deck_screen_card_gallery_grid_position = (50,60)
        self.build_deck_screen_card_gallery_grid = pygame.Surface(self.build_deck_screen_card_gallery_grid_size)
        self.build_deck_screen_card_gallery_grid.fill((123,163,48))
        self.build_deck_screen_card_gallery_grid_rect = self.build_deck_screen_card_gallery_grid.get_rect()
        self.build_deck_screen_card_gallery_grid.blit(self.build_deck_screen_card_gallery_grid, self.build_deck_screen_card_gallery_grid_rect)
        self.build_deck_screen_card_gallery_grid_rect.topleft = self.build_deck_screen_card_gallery_grid_position

        self.build_deck_screen_deck_grid_size = (1100,230)
        self.build_deck_screen_deck_grid_position = (50,560)
        self.build_deck_screen_deck_grid = pygame.Surface(self.build_deck_screen_deck_grid_size)
        self.build_deck_screen_deck_grid.fill((122,113,178))
        self.build_deck_screen_deck_grid_rect = self.build_deck_screen_deck_grid.get_rect()
        self.build_deck_screen_deck_grid.blit(self.build_deck_screen_deck_grid, self.build_deck_screen_deck_grid_rect)
        self.build_deck_screen_deck_grid_rect.topleft = self.build_deck_screen_deck_grid_position




#------------------Battle Screen----------------------------------------------------
        #Battle Screen Grid Seperation System (1200*800 only)
        self.battle_screen_menu_grid_size = (800,30)
        self.battle_screen_menu_grid_position = (200,0)
        self.battle_screen_menu_grid = pygame.Surface(self.battle_screen_menu_grid_size)
        self.battle_screen_menu_grid.fill((123,163,48))
        self.battle_screen_menu_grid_rect = self.battle_screen_menu_grid.get_rect()
        self.battle_screen_menu_grid.blit(self.battle_screen_menu_grid, self.battle_screen_menu_grid_rect)
        self.battle_screen_menu_grid_rect.topleft = self.battle_screen_menu_grid_position

        self.battle_screen_deck_grid_size = (1200,220)
        self.battle_screen_deck_grid_position = (0,580)
        self.battle_screen_deck_grid = pygame.Surface(self.battle_screen_deck_grid_size)
        self.battle_screen_deck_grid.fill((222,13,78))
        self.battle_screen_deck_grid_rect = self.battle_screen_deck_grid.get_rect()
        self.battle_screen_deck_grid.blit(self.battle_screen_deck_grid, self.battle_screen_deck_grid_rect)
        self.battle_screen_deck_grid_rect.topleft = self.battle_screen_deck_grid_position

        self.battle_screen_character_1_grid_size = (200,580)
        self.battle_screen_character_1_grid_position = (1000,0)
        self.battle_screen_character_1_grid = pygame.Surface(self.battle_screen_character_1_grid_size)
        self.battle_screen_character_1_grid.fill((92,13,78))
        self.battle_screen_character_1_grid_rect = self.battle_screen_character_1_grid.get_rect()
        self.battle_screen_character_1_grid.blit(self.battle_screen_character_1_grid, self.battle_screen_character_1_grid_rect)
        self.battle_screen_character_1_grid_rect.topleft = self.battle_screen_character_1_grid_position

        self.battle_screen_character_2_grid_size = (200,580)
        self.battle_screen_character_2_grid_position = (0,0)
        self.battle_screen_character_2_grid = pygame.Surface(self.battle_screen_character_2_grid_size)
        self.battle_screen_character_2_grid.fill((92,13,78))
        self.battle_screen_character_2_grid_rect = self.battle_screen_character_2_grid.get_rect()
        self.battle_screen_character_2_grid.blit(self.battle_screen_character_2_grid, self.battle_screen_character_2_grid_rect)
        self.battle_screen_character_2_grid_rect.topleft = self.battle_screen_character_2_grid_position

        self.battle_screen_battle_1_grid_size = (400,520)
        self.battle_screen_battle_1_grid_position = (600,30)
        self.battle_screen_battle_1_grid = pygame.Surface(self.battle_screen_battle_1_grid_size)
        self.battle_screen_battle_1_grid.fill((100,3,3))
        self.battle_screen_battle_1_grid_rect = self.battle_screen_battle_1_grid.get_rect()
        self.battle_screen_battle_1_grid.blit(self.battle_screen_battle_1_grid, self.battle_screen_battle_1_grid_rect)
        self.battle_screen_battle_1_grid_rect.topleft = self.battle_screen_battle_1_grid_position

        self.battle_screen_battle_2_grid_size = (400,520)
        self.battle_screen_battle_2_grid_position = (200,30)
        self.battle_screen_battle_2_grid = pygame.Surface(self.battle_screen_battle_2_grid_size)
        self.battle_screen_battle_2_grid.fill((100,101,3))
        self.battle_screen_battle_2_grid_rect = self.battle_screen_battle_2_grid.get_rect()
        self.battle_screen_battle_2_grid.blit(self.battle_screen_battle_2_grid, self.battle_screen_battle_2_grid_rect)
        self.battle_screen_battle_2_grid_rect.topleft = self.battle_screen_battle_2_grid_position

        self.battle_screen_action_bar_grid_size = (800,30)
        self.battle_screen_action_bar_grid_position = (200,550)
        self.battle_screen_action_bar_grid = pygame.Surface(self.battle_screen_action_bar_grid_size)
        self.battle_screen_action_bar_grid.fill((0,0,0))
        self.battle_screen_action_bar_grid_rect = self.battle_screen_action_bar_grid.get_rect()
        self.battle_screen_action_bar_grid.blit(self.battle_screen_action_bar_grid, self.battle_screen_action_bar_grid_rect)
        self.battle_screen_action_bar_grid_rect.topleft = self.battle_screen_action_bar_grid_position








#-----
