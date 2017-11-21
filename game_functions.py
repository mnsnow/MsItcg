import sys
import random
import pygame
from pygame.locals import *
from settings import Settings
from button import Button
from display import Screen_status, Button_status
from grid import Grid
import card_database_functions as cdf




#-----------------------------Check events----------------------------------------------------
def check_events(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user):
    """Check mouse and keyboard events"""

    if screen_status.welcome_screen_display:
        check_events_welcome_screen(ai_settings, screen, buttons,screen_status, button_status)

    if screen_status.build_deck_screen_display:
        check_events_build_deck_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user)

    if screen_status.battle_screen_display:
        check_events_battle_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user)

def check_events_welcome_screen(ai_settings, screen, buttons,screen_status, button_status):
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

def check_events_build_deck_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user):
    """ Check all events on the build deck screen"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if Rect(100,130,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('1',screen, screen_status,card_database_filter, user)

            if Rect(245,130,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('2',screen, screen_status,card_database_filter, user)

            if Rect(390,130,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('3',screen, screen_status,card_database_filter, user)

            if Rect(535,130,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('4',screen, screen_status,card_database_filter, user)

            if Rect(680,130,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('5',screen, screen_status,card_database_filter, user)

            if Rect(825,130,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('6',screen, screen_status,card_database_filter, user)

            if Rect(970,130,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('7',screen, screen_status,card_database_filter, user)

            if Rect(100,330,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('8',screen, screen_status,card_database_filter, user)

            if Rect(245,330,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('9',screen, screen_status,card_database_filter, user)

            if Rect(390,330,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('10',screen, screen_status,card_database_filter, user)

            if Rect(535,330,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('11',screen, screen_status,card_database_filter, user)

            if Rect(680,330,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('12',screen, screen_status,card_database_filter, user)

            if Rect(825,330,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('13',screen, screen_status,card_database_filter, user)

            if Rect(970,330,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_add_card_to_deck('14',screen, screen_status,card_database_filter, user)

            if Rect(245,600,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_remove_card_from_deck('1',screen, screen_status,card_database_filter, user)

            if Rect(390,600,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_remove_card_from_deck('2',screen, screen_status,card_database_filter, user)

            if Rect(535,600,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_remove_card_from_deck('3',screen, screen_status,card_database_filter, user)

            if Rect(680,600,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_remove_card_from_deck('4',screen, screen_status,card_database_filter, user)

            if Rect(825,600,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_remove_card_from_deck('5',screen, screen_status,card_database_filter, user)

            if Rect(970,600,130,180).collidepoint(pygame.mouse.get_pos()):
                build_deck_screen_remove_card_from_deck('6',screen, screen_status,card_database_filter, user)



            elif rect_union(buttons).collidepoint(pygame.mouse.get_pos()):
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):

                        if button.text == 'Next':
                            if screen_status.build_deck_screen_to_battle_screen_all_clear:
                                screen_status.welcome_screen_display = False
                                screen_status.build_deck_screen_display = False
                                screen_status.battle_screen_display = True
                            else:
                                build_deck_screen_to_battle_screen_error_display(screen,user)
                        elif button.text == 'Back':
                            screen_status.welcome_screen_display = True
                            screen_status.build_deck_screen_display = False
                            screen_status.battle_screen_display = False
                        elif button.text == '>>':
                            screen_status.build_deck_screen_card_gallery_page_id += 1
                        elif button.text == '<<':
                            screen_status.build_deck_screen_card_gallery_page_id -= 1
                        elif button.text == 'Character':
                            card_database_filter.character = not card_database_filter.character
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
                        elif button.text == '>':
                            screen_status.build_deck_screen_my_deck_page_id += 1
                        elif button.text == '<':
                            screen_status.build_deck_screen_my_deck_page_id -= 1





        # elif event.type == pygame.MOUSEMOTION:
        #     print(pygame.mouse.get_pos())


        elif event.type == pygame.MOUSEBUTTONUP:
            pass

def check_events_battle_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user):
    """ Check all evetns on the battle screen"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:

            if Rect(100,610,130,180).collidepoint(pygame.mouse.get_pos()):
                battle_screen_card_click_action('1',screen, screen_status,card_database_filter, user)

            if Rect(245,610,130,180).collidepoint(pygame.mouse.get_pos()):
                battle_screen_card_click_action('2',screen, screen_status,card_database_filter, user)

            if Rect(390,610,130,180).collidepoint(pygame.mouse.get_pos()):
                battle_screen_card_click_action('3',screen, screen_status,card_database_filter, user)

            if Rect(535,610,130,180).collidepoint(pygame.mouse.get_pos()):
                battle_screen_card_click_action('4',screen, screen_status,card_database_filter, user)

            if Rect(680,610,130,180).collidepoint(pygame.mouse.get_pos()):
                battle_screen_card_click_action('5',screen, screen_status,card_database_filter, user)

            if Rect(825,610,130,180).collidepoint(pygame.mouse.get_pos()):
                battle_screen_card_click_action('6',screen, screen_status,card_database_filter, user)

            if Rect(970,610,130,180).collidepoint(pygame.mouse.get_pos()):
                battle_screen_card_click_action('7',screen, screen_status,card_database_filter, user)

            elif rect_union(buttons).collidepoint(pygame.mouse.get_pos()):
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):

                        if button.text == 'Back':
                            screen_status.welcome_screen_display = False
                            screen_status.build_deck_screen_display = True
                            screen_status.battle_screen_display = False
                        elif button.text == '>':
                            screen_status.battle_screen_my_hand_page_id += 1
                        elif button.text == '<':
                            screen_status.battle_screen_my_hand_page_id -= 1



        elif event.type == pygame.MOUSEMOTION:
            pass

        elif event.type == pygame.MOUSEBUTTONUP:
            pass




#-----------------------------Update screens----------------------------------------------------
def update_screen(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user):
    """ Update images on the screen and flip to the new screen"""

    if screen_status.welcome_screen_display:
        welcome_screen_update(ai_settings,screen, buttons, screen_status)

    if screen_status.build_deck_screen_display:
        build_deck_screen_update(ai_settings, grid, screen, buttons, screen_status, button_status, card_database_filter, user)

    if screen_status.battle_screen_display:
        battle_screen_update(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user)


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

def build_deck_screen_update(ai_settings, grid, screen, buttons, screen_status, button_status, card_database_filter, user):
    """ Build deck screen update"""
    screen.fill(ai_settings.bg_color)

    build_deck_screen_grid_display(grid, screen)

    build_deck_screen_stable_button_display(screen, buttons,screen_status, button_status)

    build_deck_screen_card_gallery_display(screen,buttons, screen_status, button_status, card_database_filter)

    build_deck_screen_my_deck_display(screen,buttons, screen_status, button_status, card_database_filter, user)

def battle_screen_update(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user):
    """ Battle screen update"""
    screen.fill(ai_settings.bg_color)

    battle_screen_grid_display(grid, screen)

    battle_screen_stable_button_display(screen, buttons,screen_status, button_status)

    battle_screen_my_deck_card_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    battle_screen_my_hand_button_display(screen,buttons, screen_status, button_status, card_database_filter, user)




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
    button1.update()
    button1.draw(screen)
    button2 = Button('Next','build_deck_screen', (0,0,0),1150, 0, 50, 50)
    button2.update()
    button2.draw(screen)
    button3 = Button('Build your deck by picking 40 cards below: ', 'build_deck_screen', (0,0,0),300, 0, 600, 50)
    button3.update()
    button3.draw(screen)
    if button_status.build_deck_screen_stable_button_backend:
        buttons.extend((button1, button2, button3))
        button_status.build_deck_screen_stable_button_backend = False

def build_deck_screen_to_battle_screen_error_display(screen,user):
    """ Display error message when entering battle screen with incomplete deck"""
    button4 = Button('why?','', (0,0,0),510,350, 300, 300)
    button4.update()
    button4.draw(screen)
    print('what!!!!')


# - - - - - - - - - - - - -

def build_deck_screen_card_gallery_display(screen, buttons, screen_status, button_status, card_database_filter):
    """Display Card Gallery"""
    build_deck_screen_card_gallery_button_display(screen, buttons, screen_status, button_status, card_database_filter)
    build_deck_screen_card_gallery_card_display(screen, buttons, screen_status, button_status, card_database_filter)

def build_deck_screen_card_gallery_button_display(screen, buttons, screen_status, button_status, card_database_filter):
    """Display all buttons in the card gallery part"""
    # Page forward button
    button1 = Button('>>','build_deck_screen_card_gallery_stable', (0,0,0),1100, 300, 50, 50)
    # Edge cases when len() = 14,28,42 ...
    if len(cdf.request_card_list(card_database_filter)) % 14 == 0 and len(cdf.request_card_list(card_database_filter)) != 0:
        if screen_status.build_deck_screen_card_gallery_page_id != ((len(cdf.request_card_list(card_database_filter)))//14): # Make sure on the last page no foreward button shows up
            button1.update()
            button1.draw(screen)
    # Normal cases
    else:
        if screen_status.build_deck_screen_card_gallery_page_id != ((len(cdf.request_card_list(card_database_filter)))//14 + 1): # Make sure on the last page no foreward button shows up
            button1.update()
            button1.draw(screen)
    # Page backward button
    button2 = Button('<<', 'build_deck_screen_card_gallery_stable' ,(0,0,0),50, 300, 50, 50)
    if screen_status.build_deck_screen_card_gallery_page_id != 1: # Make sure on the first page no backward button shows up
        button2.update()
        button2.draw(screen)
    # button3: page button to display the current page number for card gallery
    button3 = Button('page: ' + str(screen_status.build_deck_screen_card_gallery_page_id), 'build_deck_screen_card_gallery_stable' ,(123,163,48),560, 510, 80, 40)
    button3.update()
    button3.draw(screen)
    # Class filter:
    button4 = Button('Filter: ','' ,(0,0,0),80, 70, 90, 50)
    button4.update()
    button4.draw(screen)
    # Character filter button
    if card_database_filter.character:
        button_character = Button('Character', '', (100,30,130),200,70,90,50)
    else:
        button_character = Button('Character', '', (0,0,0),200,70,90,50)
    button_character.update()
    button_character.draw(screen)
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
        buttons.extend((button1,button2,button3,button4,button_character, button_bowman,button_magician,button_thief,button_warrior,button_jobless))
        button_status.build_deck_screen_card_gallery_button_backend = False

def build_deck_screen_card_gallery_card_display(screen, buttons, screen_status, button_status, card_database_filter):
    """Display all cards on card gallery"""
    rect_position_x = 100 #local variables for rect position for the first card in the card gallery
    rect_position_y = 130
    row_number = 1 # local variable to help keep track of position of card
    # Check the page number to make sure if will not go negative or randomly large
    if screen_status.build_deck_screen_card_gallery_page_id <= 0:
        screen_status.build_deck_screen_card_gallery_page_id = 1
    # Edge cases when len() = 14, 28, 42...
    if len(cdf.request_card_list(card_database_filter)) % 14 == 0 and len(cdf.request_card_list(card_database_filter)) != 0:
        if screen_status.build_deck_screen_card_gallery_page_id >= (len(cdf.request_card_list(card_database_filter)))//14 + 1:
            screen_status.build_deck_screen_card_gallery_page_id = (len(cdf.request_card_list(card_database_filter)))//14 + 0

    else:
        if screen_status.build_deck_screen_card_gallery_page_id >= (len(cdf.request_card_list(card_database_filter)))//14 + 2:
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

# - - - - - - - - - - - - -

def build_deck_screen_my_deck_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """Display things on my deck portion"""

    build_deck_screen_my_deck_button_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    build_deck_screen_my_deck_card_display(screen,buttons, screen_status, button_status, card_database_filter, user)

def build_deck_screen_my_deck_button_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """Display buttons on my deck part of the screen"""
    local_store_list = build_deck_screen_my_deck_card_list_refine(user)
    #character number display
    if user.character_card == '':
        button1 = Button('Character: 0/1','' ,(122,113,178),50, 560, 150, 30, font_color = (255,60,60))
    else:
        button1 = Button('Character: 1/1','' ,(122,113,178),50, 560, 150, 30)
    button1.update()
    button1.draw(screen)
    #card number display
    if len(user.deck_list) >= 40:
        button2 = Button('Total: ' + str(len(user.deck_list)) + '/40','' ,(122,113,178),595, 560, 150, 30)
    else:
        button2 = Button('Total: ' + str(len(user.deck_list)) + '/40','' ,(122,113,178),595, 560, 150, 30, font_color = (255,60,60))
    button2.update()
    button2.draw(screen)

    # Page forward button
    button3 = Button('>','', (0,0,0),1110,650, 30, 30)
    # Edge cases when len() = 14,28,42 ...
    if len(local_store_list) % 6 == 0 and len(local_store_list) != 0:
        if screen_status.build_deck_screen_my_deck_page_id != ((len(local_store_list))//6): # Make sure on the last page no foreward button shows up
            button3.update()
            button3.draw(screen)
    # Normal cases
    else:
        if screen_status.build_deck_screen_my_deck_page_id != ((len(local_store_list))//6 + 1): # Make sure on the last page no foreward button shows up
            button3.update()
            button3.draw(screen)
    # Page backward button
    button4 = Button('<','', (0,0,0),210,650, 30, 30)
    if screen_status.build_deck_screen_my_deck_page_id != 1: # Make sure on the first page no backward button shows up
        button4.update()
        button4.draw(screen)

    if button_status.build_deck_screen_my_deck_button_backend:
        buttons.extend((button3,button4))
        button_status.build_deck_screen_my_deck_button_backend = False

def build_deck_screen_my_deck_card_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """Input user.deck_list, drawing the card list propperly"""
    # Draw the character card
    if user.character_card == '':
        pass
    else:
        user.character_card.rect.x = 65
        user.character_card.rect.y = 600
        screen.blit(user.character_card.image, user.character_card.rect)
    #Clear duplicate amount each frame and render the refined list
    for card_new in user.deck_list:
        card_new.duplicate = 1
    local_store_list = build_deck_screen_my_deck_card_list_refine(user)
    #use refined list to draw
    rect_position_x = 245 #local variables for rect position for the first card in the user deck
    rect_position_y = 600
    row_number = 1
    #Display cards in local_store_list:

    if screen_status.build_deck_screen_my_deck_page_id <= 0:
        screen_status.build_deck_screen_my_deck_page_id = 1
    # Edge cases when len() = 6,12,18....
    if len(local_store_list) % 6 == 0 and len(local_store_list) != 0:
        if screen_status.build_deck_screen_my_deck_page_id >= (len(local_store_list))//6 + 1:
            screen_status.build_deck_screen_my_deck_page_id = (len(local_store_list))//6 + 0

    else:
        if screen_status.build_deck_screen_my_deck_page_id >= (len(local_store_list))//6 + 2:
            screen_status.build_deck_screen_my_deck_page_id = (len(local_store_list))//6 + 1
    # Algorithm to draw all cards in local_store_list, 6 card per page.
    for card in local_store_list[6*(screen_status.build_deck_screen_my_deck_page_id - 1):6 * screen_status.build_deck_screen_my_deck_page_id]:
        if row_number <= 6:
            card.rect.x = rect_position_x
            card.rect.y = rect_position_y
            screen.blit(card.image, card.rect)
            rect_position_x += 145
            row_number += 1
            build_deck_screen_my_deck_duplicate_number_display(card, screen)
            if row_number >= 7:
                row_number = 1

def build_deck_screen_add_card_to_deck(card_gallery_position ,screen, screen_status,card_database_filter, user):
    """Add card from gallery to user.deck_list"""
    # Check to avoid errors when click on empty rect preventing adding card.
    if len(cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1):14 * screen_status.build_deck_screen_card_gallery_page_id]) >= int(card_gallery_position):
        if cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1)+(int(card_gallery_position)-1)].card_type == 'character':
            user.character_card = cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1)+(int(card_gallery_position)-1)]
        else:
            user.deck_list.append(cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1)+(int(card_gallery_position)-1)])
    else:
        pass

def build_deck_screen_remove_card_from_deck(my_deck_position ,screen, screen_status,card_database_filter, user):
    """ Input card position and user.deck_list, remove one instance of that card from the user.deck_list"""
    local_store_list = build_deck_screen_my_deck_card_list_refine(user)
    # Check to avoid errors when click on empty rect preventing removing card.
    if len(local_store_list[6*(screen_status.build_deck_screen_my_deck_page_id - 1):6 * screen_status.build_deck_screen_my_deck_page_id]) >= int(my_deck_position):
        user.deck_list.remove(local_store_list[6*(screen_status.build_deck_screen_my_deck_page_id - 1)+(int(my_deck_position)-1)])
    else:
        pass

def build_deck_screen_my_deck_card_list_refine(user):
    """Input user.deck_list, return a refined version without duplicate and save duplicate number in class instance"""
    local_store_list = []
    for card_new in user.deck_list:

        if len(local_store_list) == 0:
            local_store_list.append(card_new)
        else:

            if build_deck_screen_my_deck_check_duplicate(card_new, local_store_list):
                card_new.duplicate += 1
            else:
                local_store_list.append(card_new)

    return sorted(local_store_list, key = lambda card: int(card.level))

def build_deck_screen_my_deck_check_duplicate(card, local_store_list):
    """ Input a card and a list, check if that card is in the list"""
    for cd in local_store_list:
        if card.set_number == cd.set_number and card.card_number == cd.card_number:
            return True
            break
    return False

def build_deck_screen_my_deck_duplicate_number_display(card, screen):
    """Input Card instance, output how many copies of that card as a button above that card"""
    if card.duplicate <= 4:
        button_dup = Button(str(card.duplicate) + 'x','', (122,113,178),(card.rect.x + 50),(card.rect.y - 30) , 30, 30)
    else:
        button_dup = Button(str(card.duplicate) + 'x','', (122,113,178),(card.rect.x + 50),(card.rect.y - 30) , 30, 30, font_color = (255,60,60))
    button_dup.update()
    button_dup.draw(screen)




#-----------------------------Battle Screen actions-------------------------------------------------
def battle_screen_grid_display(grid, screen):
    """ Display grid system on battle screen"""
    screen.blit(grid.battle_screen_menu_grid, grid.battle_screen_menu_grid_rect)
    screen.blit(grid.battle_screen_deck_grid, grid.battle_screen_deck_grid_rect)
    screen.blit(grid.battle_screen_character_1_grid, grid.battle_screen_character_1_grid_rect)
    screen.blit(grid.battle_screen_character_2_grid, grid.battle_screen_character_2_grid_rect)
    screen.blit(grid.battle_screen_battle_1_grid, grid.battle_screen_battle_1_grid_rect)
    screen.blit(grid.battle_screen_battle_2_grid, grid.battle_screen_battle_2_grid_rect)
    screen.blit(grid.battle_screen_action_bar_grid, grid.battle_screen_action_bar_grid_rect)

def battle_screen_stable_button_display(screen, buttons,screen_status, button_status):
    """ Display all stable button on battle screen"""
    button_action_bar_text = 'Welcome!'
    if screen_status.battle_screen_action_indicator == 'p1':
        button_action_bar_text = 'Round:1, Phase:1 -- Pick a card to level up your character'
    if screen_status.battle_screen_action_indicator == 'p2':
        button_action_bar_text = 'Round:1, Phase:2 -- Character actions'
    if screen_status.battle_screen_action_indicator == 'p3':
        button_action_bar_text = 'Round:1, Phase:3 -- Monster battle actions'
    #
    button_action_bar = Button(button_action_bar_text,'', (0,0,0),200, 550, 800, 30)
    button_action_bar.update()
    button_action_bar.draw(screen)
    #
    button1 = Button('Back','', (0,0,0),200, 0, 50, 30)
    button1.update()
    button1.draw(screen)
    #
    button2 = Button('Rules','', (0,0,0),400, 0, 100, 30)
    button2.update()
    button2.draw(screen)
    #
    button3 = Button('Surrender', '', (0,0,0),900, 0, 100, 30)
    button3.update()
    button3.draw(screen)
    if button_status.battle_screen_stable_button_backend:
        buttons.extend((button1, button2, button3))
        button_status.battle_screen_stable_button_backend = False

def battle_screen_my_deck_card_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display my deck on battle screen"""
    rect_position_x = 100
    rect_position_y = 610
    row_number = 1
    print(screen_status.battle_screen_my_hand_page_id)
    if screen_status.battle_screen_action_indicator == 'p0':
        user.deck_list = random.sample(user.deck_list, len(user.deck_list))
        user.hand_list = user.deck_list[0:15]
        for card_hand in user.hand_list:
            card_hand.rect.x = rect_position_x
            card_hand.rect.y = rect_position_y
            screen.blit(card_hand.image, card_hand.rect)
            rect_position_x += 145
            screen_status.battle_screen_action_indicator = 'p1'

    if screen_status.battle_screen_action_indicator == 'p1':
        if screen_status.battle_screen_my_hand_page_id <= 0:
            screen_status.battle_screen_my_hand_page_id = 1
        # Edge cases when len() = 6,12,18....
        if len(user.hand_list) % 7 == 0 and len(user.hand_list) != 0:
            if screen_status.battle_screen_my_hand_page_id >= (len(user.hand_list))//7 + 1:
                screen_status.battle_screen_my_hand_page_id = (len(user.hand_list))//7 + 0

        else:
            if screen_status.battle_screen_my_hand_page_id >= (len(user.hand_list))//7 + 2:
                screen_status.battle_screen_my_hand_page_id = (len(user.hand_list))//7 + 1
        # Algorithm to draw all cards in local_store_list, 6 card per page.
        for card in user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]:
            if row_number <= 7:
                card.rect.x = rect_position_x
                card.rect.y = rect_position_y
                screen.blit(card.image, card.rect)
                rect_position_x += 145
                row_number += 1
                if row_number >= 8:
                    row_number = 1

    if screen_status.battle_screen_action_indicator == 'p2':
        for card_hand in user.hand_list:
            card_hand.rect.x = rect_position_x
            card_hand.rect.y = rect_position_y
            screen.blit(card_hand.image, card_hand.rect)
            rect_position_x += 145

    if screen_status.battle_screen_action_indicator == 'p3':
        for card_hand in user.hand_list:
            card_hand.rect.x = rect_position_x
            card_hand.rect.y = rect_position_y
            screen.blit(card_hand.image, card_hand.rect)
            rect_position_x += 145

def battle_screen_my_hand_button_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display buttons in my hand on battle screen"""
    # Page forward button
    button1 = Button('>','', (0,0,0),1100, 660, 50, 50)
    # Edge cases when len() = 14,28,42 ...
    if len(user.hand_list) % 7 == 0 and len(user.hand_list) != 0:
        if screen_status.battle_screen_my_hand_page_id != ((len(user.hand_list))//7): # Make sure on the last page no foreward button shows up
            button1.update()
            button1.draw(screen)
    # Normal cases
    else:
        if screen_status.battle_screen_my_hand_page_id != ((len(user.hand_list))//7 + 1): # Make sure on the last page no foreward button shows up
            button1.update()
            button1.draw(screen)
    # Page backward button
    button2 = Button('<', '' ,(0,0,0),50, 660, 50, 50)
    if screen_status.battle_screen_my_hand_page_id != 1: # Make sure on the first page no backward button shows up
        button2.update()
        button2.draw(screen)

    if button_status.battle_screen_my_hand_page_change_button_backend:
        buttons.extend((button1,button2))
        button_status.battle_screen_my_hand_page_change_button_backend = False


def battle_screen_card_click_action(hand_position,screen, screen_status,card_database_filter, user):
    """ determind actions after click on card in hand"""
    pass


#-----------------------------Hand handaction----------------------------------------------------
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


def monster_handaction_back(buttons, button_status):
    button_status.monster_handaction_display = False
    bts = []
    for button in buttons:
        if button.group == 'monster_handaction':
            bts.append(button)
    for bt in bts:
        buttons.remove(bt)
    button_status.monster_handaction_backend = True




#----------------------------- Battle action----------------------------------------------------
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

def monster_battleaction_back(buttons, button_status):
    button_status.monster_battleaction_display = False
    bts = []
    for button in buttons:
        if button.group == 'monster_battleaction':
            bts.append(button)
    for bt in bts:
        buttons.remove(bt)
    button_status.monster_battleaction_backend = True




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
