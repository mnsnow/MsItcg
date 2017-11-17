import sys
import pygame

class Grid():
    """All grid information of all screens"""
    def __init__(self):


#------------------Battle Screen----------------------------------------------------
        #Battle Screen Grid Seperation System (1200*800 only)
        self.battle_screen_menu_grid_size = (800,30)
        self.battle_screen_menu_grid_position = (200,0)
        self.battle_screen_menu_grid = pygame.Surface(self.battle_screen_menu_grid_size)
        self.battle_screen_menu_grid.fill((123,163,48))
        self.battle_screen_menu_grid_rect = self.battle_screen_menu_grid.get_rect()
        self.battle_screen_menu_grid.blit(self.battle_screen_menu_grid, self.battle_screen_menu_grid_rect)
        self.battle_screen_menu_grid_rect.topleft = self.battle_screen_menu_grid_position

        self.battle_screen_monster_grid_size = (600,220)
        self.battle_screen_monster_grid_position = (0,580)
        self.battle_screen_monster_grid = pygame.Surface(self.battle_screen_monster_grid_size)
        self.battle_screen_monster_grid.fill((222,13,78))
        self.battle_screen_monster_grid_rect = self.battle_screen_monster_grid.get_rect()
        self.battle_screen_monster_grid.blit(self.battle_screen_monster_grid, self.battle_screen_monster_grid_rect)
        self.battle_screen_monster_grid_rect.topleft = self.battle_screen_monster_grid_position

        self.battle_screen_tactic_grid_size = (600,220)
        self.battle_screen_tactic_grid_position = (600,580)
        self.battle_screen_tactic_grid = pygame.Surface(self.battle_screen_tactic_grid_size)
        self.battle_screen_tactic_grid.fill((22,13,78))
        self.battle_screen_tactic_grid_rect = self.battle_screen_tactic_grid.get_rect()
        self.battle_screen_tactic_grid.blit(self.battle_screen_tactic_grid, self.battle_screen_tactic_grid_rect)
        self.battle_screen_tactic_grid_rect.topleft = self.battle_screen_tactic_grid_position

        self.battle_screen_character_1_grid_size = (200,580)
        self.battle_screen_character_1_grid_position = (0,0)
        self.battle_screen_character_1_grid = pygame.Surface(self.battle_screen_character_1_grid_size)
        self.battle_screen_character_1_grid.fill((92,13,78))
        self.battle_screen_character_1_grid_rect = self.battle_screen_character_1_grid.get_rect()
        self.battle_screen_character_1_grid.blit(self.battle_screen_character_1_grid, self.battle_screen_character_1_grid_rect)
        self.battle_screen_character_1_grid_rect.topleft = self.battle_screen_character_1_grid_position

        self.battle_screen_character_2_grid_size = (200,580)
        self.battle_screen_character_2_grid_position = (1000,0)
        self.battle_screen_character_2_grid = pygame.Surface(self.battle_screen_character_2_grid_size)
        self.battle_screen_character_2_grid.fill((92,13,78))
        self.battle_screen_character_2_grid_rect = self.battle_screen_character_2_grid.get_rect()
        self.battle_screen_character_2_grid.blit(self.battle_screen_character_2_grid, self.battle_screen_character_2_grid_rect)
        self.battle_screen_character_2_grid_rect.topleft = self.battle_screen_character_2_grid_position

        self.battle_screen_battle_1_grid_size = (400,550)
        self.battle_screen_battle_1_grid_position = (200,30)
        self.battle_screen_battle_1_grid = pygame.Surface(self.battle_screen_battle_1_grid_size)
        self.battle_screen_battle_1_grid.fill((100,3,3))
        self.battle_screen_battle_1_grid_rect = self.battle_screen_battle_1_grid.get_rect()
        self.battle_screen_battle_1_grid.blit(self.battle_screen_battle_1_grid, self.battle_screen_battle_1_grid_rect)
        self.battle_screen_battle_1_grid_rect.topleft = self.battle_screen_battle_1_grid_position

        self.battle_screen_battle_2_grid_size = (400,550)
        self.battle_screen_battle_2_grid_position = (600,30)
        self.battle_screen_battle_2_grid = pygame.Surface(self.battle_screen_battle_2_grid_size)
        self.battle_screen_battle_2_grid.fill((100,101,3))
        self.battle_screen_battle_2_grid_rect = self.battle_screen_battle_2_grid.get_rect()
        self.battle_screen_battle_2_grid.blit(self.battle_screen_battle_2_grid, self.battle_screen_battle_2_grid_rect)
        self.battle_screen_battle_2_grid_rect.topleft = self.battle_screen_battle_2_grid_position
