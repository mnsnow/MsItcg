import sys
import pygame

class Button():

    def __init__(self, text, group, color=(0, 0, 0), x=0, y=0, width=100, height=50):



        self.text = text
        self.color = color
        self.group = group

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









#--
