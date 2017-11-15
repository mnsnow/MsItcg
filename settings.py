import sys
import pygame

class Settings():

    def __init__(self):

        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100,3,3)

        #Screen Grid Seperation System (1200*800 only)
        self.monster_grid_size = (600,320)
        self.monster_grid_position = (0,480)
        self.monster_grid = pygame.Surface(self.monster_grid_size)
        self.monster_grid.fill((222,13,78))
        self.monster_grid_rect = self.monster_grid.get_rect()
        self.monster_grid.blit(self.monster_grid, self.monster_grid_rect)
        self.monster_grid_rect.topleft = self.monster_grid_position


        self.tactic_grid_size = (600,320)
        self.tactic_grid_position = (600,480)
        self.tactic_grid = pygame.Surface(self.tactic_grid_size)
        self.tactic_grid.fill((22,13,78))
        self.tactic_grid_rect = self.tactic_grid.get_rect()
        self.tactic_grid.blit(self.tactic_grid, self.tactic_grid_rect)
        self.tactic_grid_rect.topleft = self.tactic_grid_position


        self.character_1_grid_size = (300,480)
        self.character_1_grid_position = (0,0)
        self.character_1_grid = pygame.Surface(self.character_1_grid_size)
        self.character_1_grid.fill((92,13,78))
        self.character_1_grid_rect = self.character_1_grid.get_rect()
        self.character_1_grid.blit(self.character_1_grid, self.character_1_grid_rect)
        self.character_1_grid_rect.topleft = self.character_1_grid_position


        self.character_2_grid_size = (300,480)
        self.character_2_grid_position = (900,0)
        self.character_2_grid = pygame.Surface(self.character_2_grid_size)
        self.character_2_grid.fill((92,13,78))
        self.character_2_grid_rect = self.character_2_grid.get_rect()
        self.character_2_grid.blit(self.character_2_grid, self.character_2_grid_rect)
        self.character_2_grid_rect.topleft = self.character_2_grid_position


        self.battle_1_grid_size = (300,480)
        self.battle_1_grid_position = (300,0)
        self.battle_1_grid = pygame.Surface(self.battle_1_grid_size)
        self.battle_1_grid.fill((100,3,3))
        self.battle_1_grid_rect = self.battle_1_grid.get_rect()
        self.battle_1_grid.blit(self.battle_1_grid, self.battle_1_grid_rect)
        self.battle_1_grid_rect.topleft = self.battle_1_grid_position


        self.battle_2_grid_size = (300,480)
        self.battle_2_grid_position = (600,0)
        self.battle_2_grid = pygame.Surface(self.battle_2_grid_size)
        self.battle_2_grid.fill((100,101,3))
        self.battle_2_grid_rect = self.battle_2_grid.get_rect()
        self.battle_2_grid.blit(self.battle_2_grid, self.battle_2_grid_rect)
        self.battle_2_grid_rect.topleft = self.battle_2_grid_position



        #Cards Settings
        self.card_size_x = 180
        self.card_size_y = 250
