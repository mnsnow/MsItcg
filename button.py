import sys
import pygame

class Button():

    def __init__(self, text, color=(0, 0, 0), x=0, y=0, width=100, height=50):



        self.text = text
        self.color = color

        self.image_normal = pygame.Surface((width, height))
        self.image_normal.fill(color)

        self.image_hovered = pygame.Surface((width, height))
        self.image_hovered.fill((0,255,0)) #green

        self.image = self.image_normal
        self.rect = self.image.get_rect()

        font = pygame.font.Font('freesansbold.ttf', 17)
        text_image = font.render(text, True, (255,255,255))
        text_rect = text_image.get_rect(center = self.rect.center)

        self.image_normal.blit(text_image, text_rect)
        self.image_hovered.blit(text_image, text_rect)

        self.rect.topleft = (x, y)
        self.hovered = False

    def update(self):

        if self.hovered:
            self.image = self.image_hovered
        else:
            self.image = self.image_normal

    def draw(self, screen):

        screen.blit(self.image, self.rect)

    def do_event(self):

        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                print('Clicked:', self.text)





class Button_status():
    """ Control active status of all buttons"""
    def __init__(self, monster_handaction=False, monster_battleaction=False, menu_rules=False):

        self.monster_handaction = monster_handaction
        self.monster_battleaction = monster_battleaction
        self.menu_rules = menu_rules


    def monster_handaction_active(self):
        self.monster_handaction = True

    def monster_handaction_deactive(self):
        self.monster_handaction = False


    def monster_battleaction_active(self):
        self.monster_battleaction = True

    def monster_battleaction_deactive(self):
        self.monster_battleaction = False

    def menu_rules_active(self):
        self.menu_rules = True

    def menu_rules_deactive(self):
        self.menu_rules = False




#--
