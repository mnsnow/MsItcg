import pygame

def run_game():

    pygame.init()

    screen = pygame.display.set_mode((1200,800))

    while True:

        screen.fill((55,55,55))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())


        pygame.display.flip()


run_game()
