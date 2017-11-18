import sys
import pygame
from pygame.locals import *
from settings import Settings
from character import Character_1, Character_2
from monster import Monster
from tactic import Tactic
from button import Button
from display import Mouse_status, Screen_status, Button_status
from grid import Grid
from card import Card
import card_database_functions as cdf




#-----------------------------Check events----------------------------------------------------
def check_events(ai_settings,grid, screen, monster, menu_buttons, buttons,mouse_status,screen_status, button_status, card_database_filter):
    """Check mouse and keyboard events"""

    if screen_status.welcome_screen_display:
        check_events_welcome_screen(ai_settings, screen, monster, menu_buttons, buttons,mouse_status,screen_status, button_status)

    if screen_status.build_deck_screen_display:
        check_events_build_deck_screen(ai_settings, screen, monster, menu_buttons, buttons,mouse_status,screen_status, button_status, card_database_filter)

    if screen_status.battle_screen_display:
        check_events_battle_screen(ai_settings,grid, screen, monster, menu_buttons, buttons,mouse_status,screen_status, button_status)

def check_events_welcome_screen(ai_settings, screen, monster, menu_buttons, buttons,mouse_status,screen_status, button_status):
    """ Check all events on the welcome screen"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect_union(buttons).collidepoint(pygame.mouse.get_pos()):
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):

                        if button.text == 'Play':
                            welcome_screen_play(buttons, screen_status)
                        elif button.text == 'Quit':
                            welcome_screen_quit(buttons, screen_status)

def check_events_build_deck_screen(ai_settings, screen, monster, menu_buttons, buttons,mouse_status,screen_status, button_status, card_database_filter):
    """ Check all events on the build deck screen"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # if mouse_status.mousebuttondown_status:
            #     pass
            # else:
            #     mouse_status.mousebuttondown_status = True
                if rect_union(buttons).collidepoint(pygame.mouse.get_pos()):
                    for button in buttons:
                        if button.rect.collidepoint(pygame.mouse.get_pos()):

                            if button.text == 'Next':
                                screen_status.welcome_screen_display = False
                                screen_status.build_deck_screen_display = False
                                screen_status.battle_screen_display = True
                            elif button.text == 'Back':
                                screen_status.welcome_screen_display = True
                                screen_status.build_deck_screen_display = False
                                screen_status.battle_screen_display = False
                            elif button.text == '>>':
                                screen_status.build_deck_screen_card_gallery_page_id += 1
                            elif button.text == '<<':
                                screen_status.build_deck_screen_card_gallery_page_id -= 1
                            elif button.text == 'Bowman':
                                card_database_filter.bowman = not card_database_filter.bowman
                            elif button.text == 'Magician':
                                card_database_filter.magician = not card_database_filter.magician
                            elif button.text == 'Thief':
                                card_database_filter.thief = not card_database_filter.thief
                            elif button.text == 'Warrior':
                                card_database_filter.warrior = not card_database_filter.warrior
                            elif button.text == 'Jobless':
                                card_database_filter.jobless = not card_database_filter.jobless



        # elif event.type == pygame.MOUSEMOTION:
        #     print(pygame.mouse.get_pos())


        elif event.type == pygame.MOUSEBUTTONUP:
            if mouse_status.mousebuttondown_status == True:
                mouse_status.mousebuttondown_status = False

def check_events_battle_screen(ai_settings,grid, screen, monster, menu_buttons, buttons,mouse_status,screen_status, button_status):
    """ Check all evetns on the battle screen"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_status.mousebuttondown_status:
                pass
            else:
                mouse_status.mousebuttondown_status = True

                if monster.rect.collidepoint(pygame.mouse.get_pos()):
                    if grid.battle_screen_monster_grid_rect.collidepoint(pygame.mouse.get_pos()):
                        button_status.monster_handaction_display = True
                    elif grid.battle_screen_character_2_grid_rect.collidepoint(pygame.mouse.get_pos()):
                        print('level up action!')
                    elif grid.battle_screen_battle_2_grid_rect.collidepoint(pygame.mouse.get_pos()):
                        button_status.monster_battleaction_display = True
                        print('hit')

                elif rect_union(menu_buttons).collidepoint(pygame.mouse.get_pos()):
                    for menu_button in menu_buttons:
                        if menu_button.rect.collidepoint(pygame.mouse.get_pos()):
                            if menu_button.text == 'Surrender':
                                print('surrender')
                            elif menu_button.text == 'Rules':
                                button_status.menu_rules = True


                elif rect_union(buttons).collidepoint(pygame.mouse.get_pos()):
                    for button in buttons:
                        if button.rect.collidepoint(pygame.mouse.get_pos()):

                            if button.text == 'Play':
                                monster_play(monster,buttons,button_status)
                            elif button.text == 'Level up':
                                monster_levelup(monster,buttons,button_status)
                            elif button.text == 'Face!':
                                monster_face(monster,buttons,button_status)
                            elif button.text == 'Fight!':
                                monster_fight(monster,buttons,button_status)
                            elif button.text == 'Skip':
                                monster_skip(monster,buttons,button_status)

                            elif button.text == 'Back':     # we need to decide button back is in which menu.
                                if grid.battle_screen_monster_grid_rect.collidepoint(pygame.mouse.get_pos()):
                                    monster_handaction_back(buttons, button_status)


                                elif grid.battle_screen_battle_2_grid_rect.collidepoint(pygame.mouse.get_pos()):
                                    monster_battleaction_back(buttons, button_status)





        # elif event.type == pygame.MOUSEMOTION:
        #     print(pygame.mouse.get_pos())

        elif event.type == pygame.MOUSEBUTTONUP:
            if mouse_status.mousebuttondown_status == True:
                mouse_status.mousebuttondown_status = False





#-----------------------------Update screens----------------------------------------------------
def update_screen(ai_settings,grid, screen, character_1, character_2, monster, tactic, menu_buttons, buttons,mouse_status, screen_status, button_status, card_database_filter):
    """ Update images on the screen and flip to the new screen"""

    if screen_status.welcome_screen_display:
        welcome_screen_update(ai_settings,screen, buttons, screen_status)

    if screen_status.build_deck_screen_display:
        build_deck_screen_update(ai_settings, grid, screen, buttons,mouse_status, screen_status, button_status, card_database_filter)

    if screen_status.battle_screen_display:
        battle_screen_update(ai_settings,grid, screen, character_1, character_2, monster, tactic, menu_buttons, buttons, screen_status, button_status)


    pygame.display.flip()

def welcome_screen_update(ai_settings,screen, buttons, screen_status):
    """ welcome screen update"""
    screen.fill(ai_settings.bg_color)
    button1 = Button('Welcome to Maplestory Itcg - Alpha', 'welcome_screen', (0,0,0),300, 100, 550, 200)
    button2 = Button('Play','', (0,0,0),300, 350, 250, 100)
    button3 = Button('Quit','', (0,0,0),600, 350, 250, 100)
    button1.update()
    button2.update()
    button3.update()
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    if screen_status.welcome_screen_backend:
        buttons.extend((button1, button2, button3))
        screen_status.welcome_screen_backend = False

def build_deck_screen_update(ai_settings, grid, screen, buttons,mouse_status, screen_status, button_status, card_database_filter):
    """ Build deck screen update"""
    screen.fill(ai_settings.bg_color)

    build_deck_screen_grid_display(grid, screen)

    build_deck_screen_stable_button_display(screen, buttons,screen_status, button_status)

    build_deck_screen_card_gallery_display(screen,buttons, screen_status, button_status, card_database_filter)

def battle_screen_update(ai_settings,grid, screen, character_1, character_2, monster, tactic, menu_buttons, buttons, screen_status, button_status):
    """ Battle screen update"""
    # BG COLOR
    screen.fill(ai_settings.bg_color)

    # Draw Grid system
    screen.blit(grid.battle_screen_menu_grid, grid.battle_screen_menu_grid_rect)
    screen.blit(grid.battle_screen_monster_grid, grid.battle_screen_monster_grid_rect)
    screen.blit(grid.battle_screen_tactic_grid, grid.battle_screen_tactic_grid_rect)
    screen.blit(grid.battle_screen_character_1_grid, grid.battle_screen_character_1_grid_rect)
    screen.blit(grid.battle_screen_character_2_grid, grid.battle_screen_character_2_grid_rect)
    screen.blit(grid.battle_screen_battle_1_grid, grid.battle_screen_battle_1_grid_rect)
    screen.blit(grid.battle_screen_battle_2_grid, grid.battle_screen_battle_2_grid_rect)

    # Draw other stuff
    character_1.blitme()
    character_2.blitme()
    monster.blitme()
    tactic.blitme()

    for menu_button in menu_buttons:
        menu_button.update()
        menu_button.draw(screen)

    if button_status.monster_handaction_display:
        monster_button_handaction_display(screen, buttons, button_status)
    if button_status.monster_battleaction_display:
        monster_button_battleaction_display(screen, buttons, button_status)
    if button_status.menu_rules:
        menu_rules_display(screen)




#-----------------------------Welcome screen actions----------------------------------------------------
def welcome_screen_play(buttons, screen_status):
    """ What happen after click play button"""
    screen_status.welcome_screen_display = False
    screen_status.build_deck_screen_display = True
    screen_status.battle_screen_display = False
    bts = []
    for button in buttons:
        if button.group == 'welcome_screen':
            bts.append(button)
    for bt in bts:
        buttons.remove(bt)
    screen_status.welcome_screen_backend = True

def welcome_screen_quit(buttons, screen_status):
    print('quit!!!!')




#-----------------------------Build deck screen actions----------------------------------------------------
def build_deck_screen_grid_display(grid, screen):
    """ Display grid system for build deck screen"""
    screen.blit(grid.build_deck_screen_card_gallery_grid, grid.build_deck_screen_card_gallery_grid_rect)
    screen.blit(grid.build_deck_screen_deck_grid, grid.build_deck_screen_deck_grid_rect)

def build_deck_screen_stable_button_display(screen, buttons,screen_status,button_status):
    """ Display all stable buttons for build deck screen"""
    button1 = Button('Back','build_deck_screen', (0,0,0),0, 0, 50, 50)
    button2 = Button('Next','build_deck_screen', (0,0,0),1150, 0, 50, 50)
    button3 = Button('Build your deck by picking 40 cards below: ', 'build_deck_screen', (0,0,0),300, 0, 600, 50)
    button4 = Button('lll', 'build_deck_screen', (0,0,0),100, 650, 100, 50)
    button1.update()
    button2.update()
    button3.update()
    button4.update()
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)
    if button_status.build_deck_screen_stable_button_backend:
        buttons.extend((button1, button2, button3, button4))
        button_status.build_deck_screen_stable_button_backend = False

def build_deck_screen_card_gallery_display(screen, buttons, screen_status, button_status, card_database_filter):
    """Display Card Gallery"""
    build_deck_screen_card_gallery_button_display(screen, buttons, screen_status, button_status, card_database_filter)
    build_deck_screen_card_gallery_card_display(screen, buttons, screen_status, button_status, card_database_filter)



def build_deck_screen_card_gallery_button_display(screen, buttons, screen_status, button_status, card_database_filter):
    """Display all buttons in the card gallery part"""
    # Page forward button
    button1 = Button('>>','build_deck_screen_card_gallery_stable', (0,0,0),1100, 300, 50, 50)
    if screen_status.build_deck_screen_card_gallery_page_id != ((len(cdf.request_card_list(card_database_filter)))//14) + 1: # Make sure on the last page no foreward button shows up
        button1.update()
        button1.draw(screen)
    # Page backward button
    button2 = Button('<<', 'build_deck_screen_card_gallery_stable' ,(0,0,0),50, 300, 50, 50)
    if screen_status.build_deck_screen_card_gallery_page_id != 1: # Make sure on the first page no backward button shows up
        button1.update()
        button2.update()
        button2.draw(screen)
    # button3: page button to display the current page number for card gallery
    button3 = Button('page: ' + str(screen_status.build_deck_screen_card_gallery_page_id), 'build_deck_screen_card_gallery_stable' ,(0,0,0),560, 510, 80, 40)
    button3.update()
    button3.draw(screen)
    # Class filter:
    button4 = Button('Class filter: ','' ,(0,0,0),100, 70, 150, 50)
    button4.update()
    button4.draw(screen)
    # Bowman filter button
    if card_database_filter.bowman:
        button_bowman = Button('Bowman', '', (100,30,130),300,70,90,50)
    else:
        button_bowman = Button('Bowman', '', (0,0,0),300,70,90,50)
    button_bowman.update()
    button_bowman.draw(screen)
    # Magician filter button
    if card_database_filter.magician:
        button_magician = Button('Magician', '', (100,30,130),400,70,90,50)
    else:
        button_magician = Button('Magician', '', (0,0,0),400,70,90,50)
    button_magician.update()
    button_magician.draw(screen)
    # Thief filter button
    if card_database_filter.thief:
        button_thief = Button('Thief', '', (100,30,130),500,70,90,50)
    else:
        button_thief = Button('Thief', '', (0,0,0),500,70,90,50)
    button_thief.update()
    button_thief.draw(screen)
    # Warrior filter button
    if card_database_filter.warrior:
        button_warrior = Button('Warrior', '', (100,30,130),600,70,90,50)
    else:
        button_warrior = Button('Warrior', '', (0,0,0),600,70,90,50)
    button_warrior.update()
    button_warrior.draw(screen)
    # Jobless filter button
    if card_database_filter.jobless:
        button_jobless = Button('Jobless', '', (100,30,130),700,70,90,50)
    else:
        button_jobless = Button('Jobless', '', (0,0,0),700,70,90,50)
    button_jobless.update()
    button_jobless.draw(screen)
    # Add all buttons to buttons list so that check_events function can detect mouse click on those buttons.
    if button_status.build_deck_screen_card_gallery_button_backend:
        buttons.extend((button1,button2,button3,button4,button_bowman,button_magician,button_thief,button_warrior,button_jobless))
        button_status.build_deck_screen_card_gallery_button_backend = False

def build_deck_screen_card_gallery_card_display(screen, buttons, screen_status, button_status, card_database_filter):
    """Display all cards on card gallery"""
    rect_position_x = 100 #local variables for rect position for the first card in the card gallery
    rect_position_y = 130
    row_number = 1
    # Check the page number to make sure if will not go negative or randomly large
    if screen_status.build_deck_screen_card_gallery_page_id <= 0:
        screen_status.build_deck_screen_card_gallery_page_id = 1
    if screen_status.build_deck_screen_card_gallery_page_id >= ((len(cdf.request_card_list(card_database_filter)))//14) + 2:
        screen_status.build_deck_screen_card_gallery_page_id = (len(cdf.request_card_list(card_database_filter)))//14 + 1
    # Algorithm to draw all cards in request_card_list, 14 card per page.
    for card in cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1):14 * screen_status.build_deck_screen_card_gallery_page_id]:
        if row_number <= 7:
            card.rect.x = rect_position_x
            card.rect.y = rect_position_y
            screen.blit(card.image, card.rect)
            rect_position_x += 145
            row_number += 1
        elif row_number <= 14:
            card.rect.x = rect_position_x - 1015
            card.rect.y = rect_position_y + 200
            screen.blit(card.image, card.rect)
            rect_position_x += 145
            row_number += 1
            if row_number >= 15:
                row_number = 1



#-----------------------------Monster handaction----------------------------------------------------
def monster_button_handaction_display(screen, buttons, button_status):
    """Display monster handaction button"""
    button1 = Button('Play','monster_handaction', (0,0,0),50, 600, 100, 50)
    button2 = Button('Level up', 'monster_handaction' ,(0,0,0),50, 650, 100, 50)
    button3 = Button('Back', 'monster_handaction' ,(0,0,0),50, 700, 100, 50)
    button1.update()
    button2.update()
    button3.update()
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    if button_status.monster_handaction_backend:
        buttons.extend((button1, button2, button3))
        button_status.monster_handaction_backend = False

def monster_play(monster,buttons,button_status):
    monster.rect.x = 700
    monster.rect.y = 200
    button_status.monster_handaction_display = False
    bts = []
    for button in buttons:
        if button.group == 'monster_handaction':
            bts.append(button)
    for bt in bts:
        buttons.remove(bt)
    button_status.monster_handaction_backend = True

def monster_levelup(monster,buttons,button_status):
    monster.rect.x = 1050
    monster.rect.y = 250
    button_status.monster_handaction_display = False
    bts = []
    for button in buttons:
        if button.group == 'monster_handaction':
            bts.append(button)
    for bt in bts:
        buttons.remove(bt)
    button_status.monster_handaction_backend = True

def monster_handaction_back(buttons, button_status):
    button_status.monster_handaction_display = False
    bts = []
    for button in buttons:
        if button.group == 'monster_handaction':
            bts.append(button)
    for bt in bts:
        buttons.remove(bt)
    button_status.monster_handaction_backend = True




#-----------------------------Monster battle action----------------------------------------------------
def monster_button_battleaction_display(screen, buttons, button_status):
    """Display monster battle action button"""
    button1 = Button('Face!','monster_battleaction', (0,0,0),600, 200, 100, 50)
    button2 = Button('Fight!', 'monster_battleaction', (0,0,0),600, 250, 100, 50)
    button3 = Button('Skip', 'monster_battleaction',(0,0,0),600, 300, 100, 50)
    button4 = Button('Back','monster_battleaction', (0,0,0),600, 350, 100, 50)
    button1.update()
    button2.update()
    button3.update()
    button4.update()
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)
    if button_status.monster_battleaction_backend:
        buttons.extend((button1, button2, button3, button4))
        button_status.monster_battleaction_backend = False

def monster_face(monster,buttons, button_status):
    button_status.monster_battleaction_display = False
    bts = []
    for button in buttons:
        if button.group == 'monster_battleaction':
            bts.append(button)
    for bt in bts:
        buttons.remove(bt)
    button_status.monster_battleaction_backend = True
    print('face!!!')

def monster_fight(monster,buttons,button_status):
    button_status.monster_battleaction_display = False
    bts = []
    for button in buttons:
        if button.group == 'monster_battleaction':
            bts.append(button)
    for bt in bts:
        buttons.remove(bt)
    button_status.monster_battleaction_backend = True
    print('fight!!')

def monster_skip(monster,buttons,button_status):
    button_status.monster_battleaction_display = False
    bts = []
    for button in buttons:
        if button.group == 'monster_battleaction':
            bts.append(button)
    for bt in bts:
        buttons.remove(bt)
    button_status.monster_battleaction_backend = True
    print('skip turn')

def monster_battleaction_back(buttons, button_status):
    button_status.monster_battleaction_display = False
    bts = []
    for button in buttons:
        if button.group == 'monster_battleaction':
            bts.append(button)
    for bt in bts:
        buttons.remove(bt)
    button_status.monster_battleaction_backend = True




#-----------------------------Rules menu----------------------------------------------------
def menu_rules_display(screen):
    """What gonna happen after click on rules buttion in the menu bar"""
    button = pygame.Surface((600,400))
    button.fill((34,87,139))
    screen.blit(button,Rect(100,300,600,400))




#-----------------------------Tools----------------------------------------------------
def rect_union(class_list):
    """Input a list of class objects, return a union of rects of those classes"""
    if len(class_list) >= 1:
        rect_list = []
        for class_object in class_list:
            rect_list.append(class_object.rect)
        return rect_list[0].unionall(rect_list[1:])
    else:
        return Rect(0,0,0,0)















#--
