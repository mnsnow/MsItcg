import sys
import random
import pygame
from pygame.locals import *
from settings import Settings
from button import Button
from display import Screen_status, Button_status
from grid import Grid
import card_database_filter as cdf
from action import Action
from builtins import any
import time




#-----------------------------Check events----------------------------------------------------
def check_events(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user,action, player2):
    """Check mouse and keyboard events"""

    if screen_status.welcome_screen_display:
        check_events_welcome_screen(ai_settings, screen, buttons,screen_status, button_status)

    if screen_status.build_deck_screen_display:
        check_events_build_deck_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user)

    if screen_status.battle_screen_display:
        check_events_battle_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)

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

def check_events_battle_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ Check all evetns on the battle screen"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            #check click on cards in hand
            for i in range(1,8):
                if Rect((100+145*(i-1)),610,130,180).collidepoint(pygame.mouse.get_pos()):
                    battle_screen_hand_click_action('hand',screen,buttons, screen_status, button_status, card_database_filter, user,player2, position = str(i))
                    break

            for i in range(1,4):
                if Rect(420,(220 + 110*(i-1)),130,80).collidepoint(pygame.mouse.get_pos()):
                    battle_screen_battleground_click_action('player2-monster',screen,buttons, screen_status, button_status, card_database_filter, user, player2, position = str(i))
                    break

            for i in range(4,7):
                if Rect(245, (220 + 110*(i-4)),130,80).collidepoint(pygame.mouse.get_pos()):
                    battle_screen_battleground_click_action('player2-monster',screen,buttons, screen_status, button_status, card_database_filter, user, player2, position = str(i))
                    break



            if Rect(20,40,130,180).collidepoint(pygame.mouse.get_pos()):
                battle_screen_battleground_click_action('player2-character',screen,buttons, screen_status, button_status, card_database_filter, user, player2)



            elif rect_union(buttons).collidepoint(pygame.mouse.get_pos()):
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        if button.text == 'Back':
                            screen_status.welcome_screen_display = False
                            screen_status.build_deck_screen_display = True
                            screen_status.battle_screen_display = False
                        elif button.text == '>':
                            screen_status.battle_screen_my_hand_page_id += 1
                            button_status.battle_screen_my_hand_indicator_display = False # Turn off display of buttons when change page

                            if (screen_status.battle_screen_action_indicator == 'stage-1-level-up'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-think-fast'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-equip'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast-and-equip'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-equip'
                            ):
                                button_status.battle_screen_instruction_bar_yes_display = False
                                button_status.battle_screen_instruction_bar_yes_backend = False

                        elif button.text == '<':
                            screen_status.battle_screen_my_hand_page_id -= 1
                            button_status.battle_screen_my_hand_indicator_display = False

                            if (screen_status.battle_screen_action_indicator == 'stage-1-level-up'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-think-fast'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-equip'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast-and-equip'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-equip'
                            ):
                                button_status.battle_screen_instruction_bar_yes_display = False
                                button_status.battle_screen_instruction_bar_yes_backend = False

                        elif button.text == 'level up':
                            battle_screen_hand_click_action('level up',screen,buttons, screen_status, button_status, card_database_filter, user, player2)
                        elif button.text == 'Yes':
                            battle_screen_instruction_bar_yes_action(screen,buttons, screen_status, button_status, card_database_filter, user,action,player2)
                        elif button.text == 'Skip':
                            battle_screen_instruction_bar_skip_action(screen,buttons, screen_status, button_status, card_database_filter, user)


        elif event.type == pygame.MOUSEMOTION: # Mostly for zoom in
            x = 0 # indicator helps remove zoom in.
            for i in range(1,8):
                if Rect((100+145*(i-1)),610,130,180).collidepoint(pygame.mouse.get_pos()):
                    button_status.card_zoom_active = True
                    button_status.card_zoom_screen_indicator = 'battle_screen'
                    button_status.card_zoom_part_indicator = 'hand'
                    button_status.card_zoom_position_indicator = str(i)
                    x = 1

            for i in range(1,16):
                if Rect(1050,(220 + 23 * (i-1)),130,23).collidepoint(pygame.mouse.get_pos()):
                    button_status.card_zoom_active = True
                    button_status.card_zoom_screen_indicator = 'battle_screen'
                    button_status.card_zoom_part_indicator = 'character 1 under'
                    button_status.card_zoom_position_indicator = str(i)
                    x = 1

            for i in range(1,16):
                if Rect(20,(220 + 23 * (i-1)),130,23).collidepoint(pygame.mouse.get_pos()):
                    button_status.card_zoom_active = True
                    button_status.card_zoom_screen_indicator = 'battle_screen'
                    button_status.card_zoom_part_indicator = 'character 2 under'
                    button_status.card_zoom_position_indicator = str(i)
                    x = 1


            if Rect(1050,40,130,180).collidepoint(pygame.mouse.get_pos()):
                button_status.card_zoom_active = True
                button_status.card_zoom_screen_indicator = 'battle_screen'
                button_status.card_zoom_part_indicator = 'character 1'
                x = 1

            if Rect(20,40,130,180).collidepoint(pygame.mouse.get_pos()):
                button_status.card_zoom_active = True
                button_status.card_zoom_screen_indicator = 'battle_screen'
                button_status.card_zoom_part_indicator = 'character 2'
                x = 1

            if x == 0:
                button_status.card_zoom_active = False



        elif event.type == pygame.MOUSEBUTTONUP:
            pass




#-----------------------------Update screens----------------------------------------------------
def update_screen(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user, player2):
    """ Update images on the screen and flip to the new screen"""

    if screen_status.welcome_screen_display:
        welcome_screen_update(ai_settings,screen, buttons, screen_status)

    if screen_status.build_deck_screen_display:
        build_deck_screen_update(ai_settings, grid, screen, buttons, screen_status, button_status, card_database_filter, user)

    if screen_status.battle_screen_display:
        battle_screen_update(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user, player2)

    # Display zoom in affect at the end to cover previous draw when zoom in
    card_zoom_update(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

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

def battle_screen_update(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user, player2):
    """ Battle screen update"""
    screen.fill(ai_settings.bg_color)

    battle_screen_grid_display(grid, screen)

    battle_screen_instruction_bar_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    battle_screen_stable_button_display(screen, buttons,screen_status, button_status)

    battle_screen_my_hand_card_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    battle_screen_my_hand_button_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    battle_screen_character_1_card_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    battle_screen_character_1_button_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    battle_screen_battleground_card_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    # Display informations of player2
    battle_screen_player2_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    battle_screen_battleground_button_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
    # Update result in each cycle
    battle_screen_result_update(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

def card_zoom_update(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ display card details (zoom in) any card"""
    if screen_status.battle_screen_action_indicator != 'stage-0':
        if button_status.card_zoom_active:
            if button_status.card_zoom_screen_indicator == 'battle_screen':
                if button_status.card_zoom_part_indicator == 'hand':
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.card_zoom_position_indicator)-1)]
                    located_card.rect_zoom.x = located_card.rect.x - 85
                    located_card.rect_zoom.y = located_card.rect.y - 210
                    screen.blit(located_card.image_zoom, located_card.rect_zoom)

                elif button_status.card_zoom_part_indicator == 'character 1':
                    located_card = user.character_card
                    located_card.rect_zoom.x = located_card.rect.x - 305
                    located_card.rect_zoom.y = located_card.rect.y
                    screen.blit(located_card.image_zoom, located_card.rect_zoom)

                elif button_status.card_zoom_part_indicator == 'character 2':
                    located_card = player2.character_card
                    located_card.rect_zoom.x = located_card.rect.x + 135
                    located_card.rect_zoom.y = located_card.rect.y
                    screen.blit(located_card.image_zoom, located_card.rect_zoom)

                elif button_status.card_zoom_part_indicator == 'character 1 under':
                    if user.character_under_card_by_level[str(int(button_status.card_zoom_position_indicator)*10)] != '':
                        located_card = user.character_under_card_by_level[str(int(button_status.card_zoom_position_indicator)*10)]
                        located_card.bottom_rect_zoom.x = 880
                        located_card.bottom_rect_zoom.y = 220 + 23 * (int(button_status.card_zoom_position_indicator)-1)
                        screen.blit(located_card.bottom_image_zoom, located_card.bottom_rect_zoom)
                    else:
                        pass

                elif button_status.card_zoom_part_indicator == 'character 2 under':
                    if player2.character_under_card_by_level[str(int(button_status.card_zoom_position_indicator)*10)] != '':
                        located_card = player2.character_under_card_by_level[str(int(button_status.card_zoom_position_indicator)*10)]
                        located_card.bottom_rect_zoom.x = 20
                        located_card.bottom_rect_zoom.y = 220 + 23 * (int(button_status.card_zoom_position_indicator)-1)
                        screen.blit(located_card.bottom_image_zoom, located_card.bottom_rect_zoom)
                    else:
                        pass




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




#-----------------------------Battle Screen displays-------------------------------------------------
def battle_screen_grid_display(grid, screen):
    """ Display grid system on battle screen"""
    screen.blit(grid.battle_screen_menu_grid, grid.battle_screen_menu_grid_rect)
    screen.blit(grid.battle_screen_deck_grid, grid.battle_screen_deck_grid_rect)
    screen.blit(grid.battle_screen_character_1_grid, grid.battle_screen_character_1_grid_rect)
    screen.blit(grid.battle_screen_character_2_grid, grid.battle_screen_character_2_grid_rect)
    screen.blit(grid.battle_screen_battle_1_grid, grid.battle_screen_battle_1_grid_rect)
    screen.blit(grid.battle_screen_battle_2_grid, grid.battle_screen_battle_2_grid_rect)
    screen.blit(grid.battle_screen_item_1_grid, grid.battle_screen_item_1_grid_rect)
    screen.blit(grid.battle_screen_item_2_grid, grid.battle_screen_item_2_grid_rect)
    screen.blit(grid.battle_screen_instruction_bar_grid, grid.battle_screen_instruction_bar_grid_rect)

def battle_screen_instruction_bar_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display instruction bar
    Stage List:
    stage-0
    stage-1
    stage-1-pick-a-card-to-level-up
    stage-2-character-action-1
    stage-2-character-action-2
    stage-2-character-action-3
    stage-2-other-action-1
    stage-2-other-action-2
    stage-2-other-action-3
    ...
    stage-2-other-action-detail-spawn-under-10
    stage-2-other-action-detail-2
    stage-2-other-action-detail-3
    ...
    stage-3-monster-1-action
    stage-3-monster-2-action
    stage-3-monster-3-action
    ...
    stage-4-end-turn
    stage-4-wait-for-opponent
    """
    # Instruction bar text

    if screen_status.battle_screen_action_indicator == 'stage-0':
        button_status.battle_screen_instruction_bar_text = 'p1-s0 -- Do you want play?'
    elif screen_status.battle_screen_action_indicator == 'stage-1':
        button_status.battle_screen_instruction_bar_text = 'p1-s1 -- Do you want to level up this turn?'
    elif screen_status.battle_screen_action_indicator == 'stage-1-level-up':
        button_status.battle_screen_instruction_bar_text = 'p1-s1 -- Pick a card and click yes to level up'
    elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-1':
        button_status.battle_screen_instruction_bar_text = 'p1-s2 -- Character action 1: Do you want to use: ' + user.character_card.skill_1_type + ' ?'
    elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-2':
        button_status.battle_screen_instruction_bar_text = 'p1-s2 -- Character action 2: Do you want to use: ' + user.character_card.skill_2_type + ' ?'
    elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-3':
        button_status.battle_screen_instruction_bar_text = 'p1-s2 -- Character action 3: Do you want to use: ' + user.character_card.skill_3_type + ' ?'
    # stage-2-other-action-10-150
    elif (('stage-2-other-action-' in screen_status.battle_screen_action_indicator)
        and (screen_status.battle_screen_player2_action_display_indicator == False)
        and 'detail' not in screen_status.battle_screen_action_indicator):
        x = screen_status.battle_screen_action_indicator.replace('stage-2-other-action-','')
        button_status.battle_screen_instruction_bar_text = 'p1-s2 -- Other action: Do you want to use: ' + user.character_under_card_by_level[x].lv_type

    # elif screen_status.battle_screen_action_indicator == 'stage-3-monster-1-action':
    #     button_status.battle_screen_instruction_bar_text = 'p1-s3 -- monster action 1'

    elif screen_status.battle_screen_action_indicator == 'stage-4-end-turn':
        button_status.battle_screen_instruction_bar_text = 'p1-s4 -- Your turn has end'


    # instruction bar draw
    button_instruction_bar = Button(button_status.battle_screen_instruction_bar_text,'battle_screen_instruction_bar_text', (0,0,0),200, 550, 640, 30)

    if 1: # Display
        button_instruction_bar.update()
        button_instruction_bar.draw(screen)
    if 0:# Backend
        x = 0
        for button in buttons:
            if button_instruction_bar.group == button.group:
                x = 1
                break
            else:
                pass
        if x == 0:
            buttons.append(button_instruction_bar)
        else:
            pass

    # yes button
    button_yes = Button('Yes','battle_screen_instruction_bar_yes', (43,93,67),920, 554, 60, 22)

    if button_status.battle_screen_instruction_bar_yes_display == True: # Display
        button_yes.update()
        button_yes.draw(screen)
    if button_status.battle_screen_instruction_bar_yes_backend == True: # Backend
        x = 0
        for button in buttons:
            if button_yes.group == button.group:
                x = 1
                break
            else:
                pass
        if x == 0:
            buttons.append(button_yes)
        else:
            pass
    elif button_status.battle_screen_instruction_bar_yes_backend == False:
        bt = ''
        for button in buttons:
            if button.group == button_yes.group:
                bt = button
        if bt == '':
            pass
        else:
            buttons.remove(bt)

    # Skip button
    button_skip = Button('Skip','battle_screen_instruction_bar_skip', (200,70,70),840, 554, 60, 22)

    if button_status.battle_screen_instruction_bar_skip_display == True: # Display
        button_skip.update()
        button_skip.draw(screen)
    if button_status.battle_screen_instruction_bar_skip_backend == True: # Backend
        x = 0
        for button in buttons:
            if button_skip.group == button.group:
                x = 1
                break
            else:
                pass
        if x == 0:
            buttons.append(button_skip)
        else:
            pass
    elif button_status.battle_screen_instruction_bar_skip_backend == False:
        bt = ''
        for button in buttons:
            if button.group == button_skip.group:
                bt = button
        if bt == '':
            pass
        else:
            buttons.remove(bt)

def battle_screen_stable_button_display(screen, buttons,screen_status, button_status):
    """ Display all stable button on battle screen"""

    #
    button1 = Button('Back','', (0,0,0),300, 0, 50, 30)
    button1.update()
    button1.draw(screen)
    #
    button2 = Button('Rules','', (0,0,0),400, 0, 100, 30)
    button2.update()
    button2.draw(screen)
    #
    button3 = Button('Surrender', '', (0,0,0),800, 0, 100, 30)
    button3.update()
    button3.draw(screen)
    if button_status.battle_screen_stable_button_backend:
        buttons.extend((button1, button2, button3))
        button_status.battle_screen_stable_button_backend = False

def battle_screen_my_hand_card_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display my deck on battle screen"""
    rect_position_x = 100
    rect_position_y = 610
    row_number = 1
    if screen_status.battle_screen_action_indicator == 'stage-0':
        pass
    else :

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

def battle_screen_my_hand_button_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display buttons in my hand on battle screen"""
    if screen_status.battle_screen_action_indicator != 'stage-0':
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
        #
        if button_status.battle_screen_my_hand_page_change_button_backend:
            buttons.extend((button1,button2))
            button_status.battle_screen_my_hand_page_change_button_backend = False
    if (screen_status.battle_screen_action_indicator == 'stage-1-level-up'
        or 'stage-2-other-action-detail-spawn' in screen_status.battle_screen_action_indicator
        or 'stage-2-other-action-detail-spawn' in screen_status.battle_screen_action_indicator
        or 'stage-2-other-action-detail-spawn' in screen_status.battle_screen_action_indicator
        ):
        if button_status.battle_screen_my_hand_indicator_display == True:
            located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
            button_level_up = Button('***','battle_screen_handaction_****', (70,70,150),located_card.rect.x+10, located_card.rect.y - 27, 115, 27)
            button_level_up.update()
            button_level_up.draw(screen)

def battle_screen_character_1_card_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display character 1 card layout"""
    user.character_card.rect.x = 1050
    user.character_card.rect.y = 40
    screen.blit(user.character_card.image, user.character_card.rect)
    #
    for i in range(1,16):
        if int(user.character_card.level) >= 10 * i:
            user.character_under_card_by_level[str(10 * i)].bottom_rect.x = 1050
            user.character_under_card_by_level[str(10 * i)].bottom_rect.y = 220 + 23 * (i-1)
            screen.blit(user.character_under_card_by_level[str(10 * i)].bottom_image, user.character_under_card_by_level[str(10 * i)].bottom_rect)

    #

def battle_screen_character_1_button_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display character 1 buttons"""
    button_basic_info = Button('Lv: ' + user.character_card.level + '  HP: ' + user.character_card.health + '  Card #: ' + str(len(user.hand_list)),'', (0,0,0),1000, 5, 200, 30)
    button_basic_info.update()
    button_basic_info.draw(screen)

    if screen_status.battle_screen_action_indicator == 'stage-2-character-action-1':
        button_action_pointer = Button('>>','',(92,13,78),1000,132,50,23)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-2':
        button_action_pointer = Button('>>','',(92,13,78),1000,155,50,23)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-3':
        button_action_pointer = Button('>>','',(92,13,78),1000,178,50,23)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif ('stage-2-other-action-' in screen_status.battle_screen_action_indicator
        and screen_status.battle_screen_player2_action_display_indicator == False
        and 'detail' not in screen_status.battle_screen_action_indicator):
        x = screen_status.battle_screen_action_indicator.replace('stage-2-other-action-','')
        button_action_pointer = Button('>>','',(92,13,78),1000,220+23*(int(x)/10-1),50,23)
        button_action_pointer.update()
        button_action_pointer.draw(screen)

def battle_screen_battleground_card_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display cards on battleground """
    # Monsters
    for i in range(1,4):
        if user.monster_in_play_dict[str(i)] != '' and int(user.monster_in_play_dict[str(i)].health) > 0:
            user.monster_in_play_dict[str(i)].top_rect.x = 650
            user.monster_in_play_dict[str(i)].top_rect.y = 220 + 110*(i-1)
            screen.blit(user.monster_in_play_dict[str(i)].top_image, user.monster_in_play_dict[str(i)].top_rect)

            button_monster_info_hp = Button('HP:  ' + user.monster_in_play_dict[str(i)].health,'',(0,0,0),650,220 + 110*(i-1),40,20, font_size = 10)
            button_monster_info_hp.update()
            button_monster_info_hp.draw(screen)

            button_monster_info_attack = Button('ATT: ' + user.monster_in_play_dict[str(i)].attack,'',(0,0,0),650,240 + 110*(i-1),40,20, font_size = 10)
            button_monster_info_attack.update()
            button_monster_info_attack.draw(screen)

    for i in range(4,7):
        if user.monster_in_play_dict[str(i)] != '' and int(user.monster_in_play_dict[str(i)].health) > 0:
            user.monster_in_play_dict[str(i)].top_rect.x = 825
            user.monster_in_play_dict[str(i)].top_rect.y = 220 + 110*(i-4)
            screen.blit(user.monster_in_play_dict[str(i)].top_image, user.monster_in_play_dict[str(i)].top_rect)

            button_monster_info_hp = Button('HP:  ' + user.monster_in_play_dict[str(i)].health,'',(0,0,0),825,220 + 110*(i-4),40,20, font_size = 10)
            button_monster_info_hp.update()
            button_monster_info_hp.draw(screen)

            button_monster_info_attack = Button('ATT: ' + user.monster_in_play_dict[str(i)].attack,'',(0,0,0),825,240 + 110*(i-4),40,20, font_size = 10)
            button_monster_info_attack.update()
            button_monster_info_attack.draw(screen)
    # Items
    for i in range(1,4):
        if user.item_in_play_dict[str(i)] != '':
            user.item_in_play_dict[str(i)].top_rect.x = 620 + 130*(i-1)
            user.item_in_play_dict[str(i)].top_rect.y = 40
            screen.blit(user.item_in_play_dict[str(i)].top_image, user.item_in_play_dict[str(i)].top_rect)
    for i in range(4,7):
        if user.item_in_play_dict[str(i)] != '':
            user.item_in_play_dict[str(i)].top_rect.x = 620 + 130*(i-4)
            user.item_in_play_dict[str(i)].top_rect.y = 110
            screen.blit(user.item_in_play_dict[str(i)].top_image, user.item_in_play_dict[str(i)].top_rect)

def battle_screen_player2_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Display informations of player2"""
    # Display Character card
    player2.character_card.rect.x = 20
    player2.character_card.rect.y = 40
    screen.blit(player2.character_card.image, player2.character_card.rect)

    # Info bar above character_card
    button_basic_info = Button('Lv: ' + player2.character_card.level + '  HP: ' + player2.character_card.health + '  Card #: ' + str(len(player2.hand_list)),'', (0,0,0),0, 5, 200, 30)
    button_basic_info.update()
    button_basic_info.draw(screen)

    # Display cards under character card
    for i in range(1,16):
        if int(player2.character_card.level) >= 10 * i:
            player2.character_under_card_by_level[str(10 * i)].bottom_rect.x = 20
            player2.character_under_card_by_level[str(10 * i)].bottom_rect.y = 220 + 23 * (i-1)
            screen.blit(player2.character_under_card_by_level[str(10 * i)].bottom_image, player2.character_under_card_by_level[str(10 * i)].bottom_rect)

    # Display the arrow when doing actions
    if screen_status.battle_screen_action_indicator == 'player2-stage-2-character-action-1':
        button_action_pointer = Button('<<','',(92,13,78),150,132,50,23)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif screen_status.battle_screen_action_indicator == 'player2-stage-2-character-action-2':
        button_action_pointer = Button('<<','',(92,13,78),150,155,50,23)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif screen_status.battle_screen_action_indicator == 'player2-stage-2-character-action-3':
        button_action_pointer = Button('<<','',(92,13,78),150,178,50,23)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif 'player2-stage-2-other-action-' in screen_status.battle_screen_action_indicator:
        if len(screen_status.battle_screen_action_indicator.replace('player2-stage-2-other-action-','')) <= 2:
            x = screen_status.battle_screen_action_indicator.replace('player2-stage-2-other-action-','')[:2]
            button_action_pointer = Button('<<','',(92,13,78),150,220+23*(int(x)/10-1),50,23)
            button_action_pointer.update()
            button_action_pointer.draw(screen)
        elif len(screen_status.battle_screen_action_indicator.replace('player2-stage-2-other-action-','')) <= 3:
            x = screen_status.battle_screen_action_indicator.replace('player2-stage-2-other-action-','')[:3]
            button_action_pointer = Button('<<','',(92,13,78),150,220+23*(int(x)/10-1),50,23)
            button_action_pointer.update()
            button_action_pointer.draw(screen)
        else:
            pass



    # Display Monsters
    for i in range(1,4):
        if player2.monster_in_play_dict[str(i)] != '' and int(player2.monster_in_play_dict[str(i)].health) > 0:
            player2.monster_in_play_dict[str(i)].top_rect.x = 420
            player2.monster_in_play_dict[str(i)].top_rect.y = 220 + 110*(i-1)
            screen.blit(player2.monster_in_play_dict[str(i)].top_image, player2.monster_in_play_dict[str(i)].top_rect)

            button_monster_info_hp = Button('HP:  ' + player2.monster_in_play_dict[str(i)].health,'',(0,0,0),420,220 + 110*(i-1),40,20, font_size = 10)
            button_monster_info_hp.update()
            button_monster_info_hp.draw(screen)

            button_monster_info_attack = Button('ATT: ' + player2.monster_in_play_dict[str(i)].attack,'',(0,0,0),420,240 + 110*(i-1),40,20, font_size = 10)
            button_monster_info_attack.update()
            button_monster_info_attack.draw(screen)

    for i in range(4,7):
        if player2.monster_in_play_dict[str(i)] != '' and int(player2.monster_in_play_dict[str(i)].health) > 0:
            player2.monster_in_play_dict[str(i)].top_rect.x = 245
            player2.monster_in_play_dict[str(i)].top_rect.y = 220 + 110*(i-4)
            screen.blit(player2.monster_in_play_dict[str(i)].top_image, player2.monster_in_play_dict[str(i)].top_rect)

            button_monster_info_hp = Button('HP:  ' + player2.monster_in_play_dict[str(i)].health,'',(0,0,0),245,220 + 110*(i-4),40,20, font_size = 10)
            button_monster_info_hp.update()
            button_monster_info_hp.draw(screen)

            button_monster_info_attack = Button('ATT: ' + player2.monster_in_play_dict[str(i)].attack,'',(0,0,0),245,240 + 110*(i-4),40,20, font_size = 10)
            button_monster_info_attack.update()
            button_monster_info_attack.draw(screen)

    # Display Items
    for i in range(1,4):
        if player2.item_in_play_dict[str(i)] != '':
            player2.item_in_play_dict[str(i)].top_rect.x = 476 - 130*(i-1)
            player2.item_in_play_dict[str(i)].top_rect.y = 40
            screen.blit(player2.item_in_play_dict[str(i)].top_image, player2.item_in_play_dict[str(i)].top_rect)
    for i in range(4,7):
        if player2.item_in_play_dict[str(i)] != '':
            player2.item_in_play_dict[str(i)].top_rect.x = 476 - 130*(i-4)
            player2.item_in_play_dict[str(i)].top_rect.y = 110
            screen.blit(player2.item_in_play_dict[str(i)].top_image, player2.item_in_play_dict[str(i)].top_rect)

    # Display actions cooldown
    if screen_status.battle_screen_player2_action_display_indicator:
        now = pygame.time.get_ticks()
        cooldown = 1000
        if now - screen_status.time_last >= cooldown:
            screen_status.time_last = now
            battle_screen_player2_action(screen, buttons,screen_status, button_status, card_database_filter, user, player2)

def battle_screen_battleground_button_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Display buttons on battleground"""
    if ('stage-2-other-action-detail-tactic-1' in screen_status.battle_screen_action_indicator
        or 'stage-3-monster-' in screen_status.battle_screen_action_indicator
        or 'stage-2-other-action-detail-easy-shot' in screen_status.battle_screen_action_indicator
        or 'stage-2-other-action-detail-tricky-shot' in screen_status.battle_screen_action_indicator
        ):
        if button_status.battle_screen_player1_battleground_indicator_display == True:
            if int(button_status.battle_screen_player1_battleground_indicator_position) <= 3:
                i = int(button_status.battle_screen_player1_battleground_indicator_position)
                monster_rect_x = 650
                monster_rect_y = 220 + 110*(i-1)
                button = Button('***','', (70,70,150),monster_rect_x + 50, monster_rect_y - 27, 30, 27)
                button.update()
                button.draw(screen)
            elif int(button_status.battle_screen_player1_battleground_indicator_position) <= 6:
                i = int(button_status.battle_screen_player1_battleground_indicator_position)
                monster_rect_x = 825
                monster_rect_y = 220 + 110*(i-4)
                button = Button('***','', (70,70,150),monster_rect_x + 50, monster_rect_y - 27, 30, 27)
                button.update()
                button.draw(screen)

        if button_status.battle_screen_player2_battleground_indicator_display == True:
            if int(button_status.battle_screen_player2_battleground_indicator_position) <= 3:
                i = int(button_status.battle_screen_player1_battleground_indicator_position)
                monster_rect_x = 420
                monster_rect_y = 220 + 110*(i-1)
                button = Button('***','', (70,70,150),monster_rect_x + 50, monster_rect_y - 27, 30, 27)
                button.update()
                button.draw(screen)
            elif int(button_status.battle_screen_player2_battleground_indicator_position) <= 6:
                i = int(button_status.battle_screen_player1_battleground_indicator_position)
                monster_rect_x = 245
                monster_rect_y = 220 + 110*(i-4)
                button = Button('***','', (70,70,150),monster_rect_x + 50, monster_rect_y - 27, 30, 27)
                button.update()
                button.draw(screen)


def battle_screen_result_update(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ update result in each cycle"""
    # Monster list update
    for card in user.monster_in_play_dict.values():
        if card != '' and int(card.health) <= 0:
            card = ''

    for card in player2.monster_in_play_dict.values():
        if card != '' and int(card.health) <= 0:
            card = ''


    # Win/Lost situations
    if int(user.character_card.health) <= 0:
        print('You Lost!')
    if int(player2.character_card.health) <= 0:
        print('You Win!')




# -----------------------------Battle Screen Actions----------------------------------------


def battle_screen_hand_click_action(click_type,screen,buttons, screen_status, button_status, card_database_filter, user,player2, position = ''):
    """ Action after click on my hand part"""
    if click_type == 'hand':
        if screen_status.battle_screen_action_indicator == 'stage-1-level-up':
            if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                button_status.battle_screen_my_hand_indicator_position = position
                button_status.battle_screen_my_hand_indicator_display = True
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True

            else:
                pass
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-think-fast':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if ((located_card.card_type == 'monster' or located_card.card_type == 'tactic')
                        and (int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a monster/tactic lv','').replace(' or less and click yes to play.','')))):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass
        elif screen_status.battle_screen_action_indicator ==  'stage-2-other-action-detail-spawn-and-equip':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if ((located_card.card_type == 'monster' or located_card.card_type == 'item')
                        and (int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a monster/item lv','').replace(' or less and click yes to play.','')))):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast-and-equip':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if ((located_card.card_type == 'tactic' or located_card.card_type == 'item')
                    and (int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a tactic/item lv','').replace(' or less and click yes to play.','')))):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass
        elif screen_status.battle_screen_action_indicator ==  'stage-2-other-action-detail-spawn':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if located_card.card_type == 'monster' and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a monster lv','').replace(' or less and click yes to play.','')):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass
        elif screen_status.battle_screen_action_indicator ==  'stage-2-other-action-detail-think-fast':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if located_card.card_type == 'tactic' and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a tactic lv','').replace(' or less and click yes to play.','')):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-equip':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if located_card.card_type == 'item' and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a item lv','').replace(' or less and click yes to play.','')):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass

    elif click_type == 'level up':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        for i in range(1,16):
            if user.character_under_card_by_level[str(i*10)] == '':
                user.character_under_card_by_level[str(i*10)] = located_card
                break
        user.hand_list.remove(located_card)
        user.character_card.level = str(int(user.character_card.level) + 10)
        user.character_card.health = str(int(user.character_card.health) + 20)
        button_status.battle_screen_my_hand_indicator_display = False

    elif click_type == 'spawn':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        # Check if this card satisfied spawn requirement
        for i in range(1,7):
            if user.monster_in_play_dict[str(i)] == '':
                user.monster_in_play_dict[str(i)] = located_card
                break
        user.hand_list.remove(located_card)
        button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True

    elif click_type == 'think fast':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        x = located_card.special_effect
        if '/Quest' in x:
            user.hand_list.append(user.remain_deck_list[0])
            del user.remain_deck_list[0]
            x.replace('/Quest','')
            if 'Quest' in x:
                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]

                user.hand_list.remove(located_card)
                button_status.battle_screen_my_hand_indicator_display = False
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
            elif 'Heal' in x:
                user.character_card.health = str(int(user.character_card.health) + int(x[-3:]))
                user.hand_list.remove(located_card)
                button_status.battle_screen_my_hand_indicator_display = False
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True

        elif 'Dmg' in x:
            screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-tactic-1'
            button_status.battle_screen_instruction_bar_yes_display = False
            button_status.battle_screen_instruction_bar_yes_backend = False
            button_status.battle_screen_instruction_bar_text = "Pick a target to do " + x[-3:] + ' Damage'



    elif click_type == 'equip':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        # Check if this card satisfied item requirement

        for i in range(1,7):
            if user.item_in_play_dict[str(i)] == '':
                user.item_in_play_dict[str(i)] = located_card
                break
        user.hand_list.remove(located_card)
        button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True

    elif click_type == 'spawn/think fast':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        # Check if this card satisfied item requirement
        if located_card.card_type == 'monster':
            for i in range(1,7):
                if user.monster_in_play_dict[str(i)] == '':
                    user.monster_in_play_dict[str(i)] = located_card
                    break
            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True

        else:

            x = located_card.special_effect
            if '/Quest' in x:
                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]
                x.replace('/Quest','')
                if 'Quest' in x:
                    user.hand_list.append(user.remain_deck_list[0])
                    del user.remain_deck_list[0]

                    user.hand_list.remove(located_card)
                    button_status.battle_screen_my_hand_indicator_display = False
                    button_status.battle_screen_instruction_bar_yes_display = True
                    button_status.battle_screen_instruction_bar_yes_backend = True
                elif 'Heal' in x:
                    user.character_card.health = str(int(user.character_card.health) + int(x[-3:]))
                    user.hand_list.remove(located_card)
                    button_status.battle_screen_my_hand_indicator_display = False
                    button_status.battle_screen_instruction_bar_yes_display = True
                    button_status.battle_screen_instruction_bar_yes_backend = True

            elif 'Dmg' in x:
                screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-tactic-1'
                button_status.battle_screen_instruction_bar_yes_display = False
                button_status.battle_screen_instruction_bar_yes_backend = False
                button_status.battle_screen_instruction_bar_text = "Pick a target to do " + x[-3:] + ' Damage'

    elif click_type == 'spawn/equip':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        # Check if this card satisfied item requirement
        if located_card.card_type == 'monster':
            for i in range(1,7):
                if user.monster_in_play_dict[str(i)] == '':
                    user.monster_in_play_dict[str(i)] = located_card
                    break
        else:
            for i in range(1,7):
                if user.item_in_play_dict[str(i)] == '':
                    user.item_in_play_dict[str(i)] = located_card
                    break
        user.hand_list.remove(located_card)
        button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True

    elif click_type == 'think fast/equip':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        # Check if this card satisfied item requirement
        if located_card.card_type == 'tactic':

            x = located_card.special_effect
            if '/Quest' in x:
                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]
                x.replace('/Quest','')
                if 'Quest' in x:
                    user.hand_list.append(user.remain_deck_list[0])
                    del user.remain_deck_list[0]

                    user.hand_list.remove(located_card)
                    button_status.battle_screen_my_hand_indicator_display = False
                    button_status.battle_screen_instruction_bar_yes_display = True
                    button_status.battle_screen_instruction_bar_yes_backend = True
                elif 'Heal' in x:
                    user.character_card.health = str(int(user.character_card.health) + int(x[-3:]))
                    user.hand_list.remove(located_card)
                    button_status.battle_screen_my_hand_indicator_display = False
                    button_status.battle_screen_instruction_bar_yes_display = True
                    button_status.battle_screen_instruction_bar_yes_backend = True

            elif 'Dmg' in x:
                screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-tactic-1'
                button_status.battle_screen_instruction_bar_yes_display = False
                button_status.battle_screen_instruction_bar_yes_backend = False
                button_status.battle_screen_instruction_bar_text = "Pick a target to do " + x[-3:] + ' Damage'

        else:
            for i in range(1,7):
                if user.item_in_play_dict[str(i)] == '':
                    user.item_in_play_dict[str(i)] = located_card
                    break
            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True


    elif click_type == 'use tactic':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        dmg = located_card.special_effect[-3:]

        if "opponent's character" in button_status.battle_screen_instruction_bar_text:
            player2.character_card.health = str(int(player2.character_card.health)-int(dmg))
            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
        elif "opponent's monster" in button_status.battle_screen_instruction_bar_text:
            x = button_status.battle_screen_instruction_bar_text[-2:-1]
            player2.monster_in_play_dict[x].health = str(int(player2.monster_in_play_dict[x].health) - int(dmg))
            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
            button_status.battle_screen_player2_battleground_indicator_display = False
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True


def battle_screen_battleground_click_action(click_type,screen,buttons, screen_status, button_status, card_database_filter, user,player2, position = ''):
    """ battleground click action """
    # If click on player2's character
    if click_type == 'player2-character':
        if (('stage-2-character-action-' in screen_status.battle_screen_action_indicator
            and 'detail-easy-shot' in screen_status.battle_screen_action_indicator)

            or ('stage-2-other-action-' in screen_status.battle_screen_action_indicator
                and 'detail-easy-shot' in screen_status.battle_screen_action_indicator)

                ):
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            button_status.battle_screen_instruction_bar_text = "Do you want to deal 10 damage to opponent's character?"
        elif (('stage-2-character-action-' in screen_status.battle_screen_action_indicator
            and 'detail-tricky-shot' in screen_status.battle_screen_action_indicator)

            or ('stage-2-other-action-' in screen_status.battle_screen_action_indicator
                and 'detail-tricky-shot' in screen_status.battle_screen_action_indicator)

                ):
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            button_status.battle_screen_instruction_bar_text = "Do you want to deal 20 damage to opponent's character?"

        elif 'stage-2-other-action-detail-tactic-1' in screen_status.battle_screen_action_indicator:
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            button_status.battle_screen_instruction_bar_text = "Do you want do damage to opponent's character?"


        elif 'stage-3-monster-' in screen_status.battle_screen_action_indicator:
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            button_status.battle_screen_instruction_bar_text = "Do you want to attack opponent's character?"

    # If click on player2's monsters
    elif click_type == 'player2-monster':
        if player2.monster_in_play_dict[position] != '':
            if 'stage-3-monster-' in screen_status.battle_screen_action_indicator:
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                button_status.battle_screen_instruction_bar_text = "Do you want to attack opponent's monster: " + position + '?'
                button_status.battle_screen_player2_battleground_indicator_display = True
                button_status.battle_screen_player2_battleground_indicator_position = position

            elif (('stage-2-character-action-' in screen_status.battle_screen_action_indicator
                and 'detail-easy-shot' in screen_status.battle_screen_action_indicator)

                or ('stage-2-other-action-' in screen_status.battle_screen_action_indicator
                    and 'detail-easy-shot' in screen_status.battle_screen_action_indicator)

                    ):
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                button_status.battle_screen_instruction_bar_text = "Do you want to deal 10 damage to opponent's monster: " + position + '?'
                button_status.battle_screen_player2_battleground_indicator_display = True
                button_status.battle_screen_player2_battleground_indicator_position = position

            elif (('stage-2-character-action-' in screen_status.battle_screen_action_indicator
                and 'detail-tricky-shot' in screen_status.battle_screen_action_indicator)

                or ('stage-2-other-action-' in screen_status.battle_screen_action_indicator
                    and 'detail-tricky-shot' in screen_status.battle_screen_action_indicator)

                    ):
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                button_status.battle_screen_instruction_bar_text = "Do you want to deal 20 damage to opponent's monster: " + position + '?'
                button_status.battle_screen_player2_battleground_indicator_display = True
                button_status.battle_screen_player2_battleground_indicator_position = position


            elif 'stage-2-other-action-detail-tactic-1' in screen_status.battle_screen_action_indicator:
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                button_status.battle_screen_instruction_bar_text = "Do you want to do damage to opponent's monster: " + position + '?'
                button_status.battle_screen_player2_battleground_indicator_display = True
                button_status.battle_screen_player2_battleground_indicator_position = position

    # Action be sent from yes click
    elif click_type == 'easy shot':
        if "opponent's character" in button_status.battle_screen_instruction_bar_text:
            player2.character_card.health = str(int(player2.character_card.health)-10)
        elif "opponent's monster" in button_status.battle_screen_instruction_bar_text:
            x = button_status.battle_screen_instruction_bar_text.replace("Do you want to deal 10 damage to opponent's monster: ",'')[0]
            player2.monster_in_play_dict[x].health = str(int(player2.monster_in_play_dict[x].health) - 10)
            button_status.battle_screen_player2_battleground_indicator_display = False

    elif click_type == 'tricky shot':
        if "opponent's character" in button_status.battle_screen_instruction_bar_text:
            player2.character_card.health = str(int(player2.character_card.health)-20)
        elif "opponent's monster" in button_status.battle_screen_instruction_bar_text:
            x = button_status.battle_screen_instruction_bar_text.replace("Do you want to deal 20 damage to opponent's monster: ",'')[0]
            player2.monster_in_play_dict[x].health = str(int(player2.monster_in_play_dict[x].health) - 20)
            button_status.battle_screen_player2_battleground_indicator_display = False

    elif click_type == 'monster_attack_character':
        x = screen_status.battle_screen_action_indicator.replace('stage-3-monster-','')[0]
        monster_attacking = user.monster_in_play_dict[x]
        player2.character_card.health = str(int(player2.character_card.health) - int(monster_attacking.attack))
    elif click_type == 'monster_attack_monster':
        x = screen_status.battle_screen_action_indicator.replace('stage-3-monster-','')[0]
        monster_attacking = user.monster_in_play_dict[x]
        player2.monster_in_play_dict[position].health = str(int(player2.monster_in_play_dict[position].health) - int(monster_attacking.attack))
        button_status.battle_screen_player2_battleground_indicator_display = False

def battle_screen_instruction_bar_yes_action(screen,buttons, screen_status, button_status, card_database_filter, user,action,player2):
    """ change to different stages when click on yes on instruction bar"""

    # Which stage to go when user at stage-0
    if screen_status.battle_screen_action_indicator == 'stage-0':
        screen_status.battle_screen_action_indicator = 'stage-1'
        button_status.battle_screen_instruction_bar_skip_display = True
        button_status.battle_screen_instruction_bar_skip_backend = True


    # Which stage to go when user at stage-1
    elif screen_status.battle_screen_action_indicator == 'stage-1':
        # Prepare usable list for next stage/run once per player per turn
        user.stage_2_other_card_usable_list = user.get_stage_2_other_card_usable_list()
        screen_status.battle_screen_action_indicator = 'stage-1-level-up'
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False


    # Which stage to go when user at stage-1-pick-a-card-to-level-up
    elif screen_status.battle_screen_action_indicator == 'stage-1-level-up':
        battle_screen_hand_click_action('level up',screen,buttons, screen_status, button_status, card_database_filter, user,player2)
        # Prepare usable list for next stage/run once per player per turn
        user.stage_2_other_card_usable_list = user.get_stage_2_other_card_usable_list()
        if int(user.character_card.skill_1_lv) <= int(user.character_card.level):
            screen_status.battle_screen_action_indicator = 'stage-2-character-action-1'
        elif len(user.stage_2_other_card_usable_list) >= 1:
            for position, card in user.character_under_card_by_level.items():
                if card == user.stage_2_other_card_usable_list[0]:
                    screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
        else:
            if (user.monster_in_play_dict['1'] == ''
            and user.monster_in_play_dict['2'] == ''
            and user.monster_in_play_dict['3'] == ''
            and user.monster_in_play_dict['4'] == ''
            and user.monster_in_play_dict['5'] == ''
            and user.monster_in_play_dict['6'] == ''):
                screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
            else:
                battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'



    # Which stage to go when user at stage-2-character-action-detail-
    elif ('stage-2-character-action-' in screen_status.battle_screen_action_indicator
        and '-detail-' in screen_status.battle_screen_action_indicator):
        x = screen_status.battle_screen_action_indicator.replace('stage-2-character-action-','')[0]

        if screen_status.battle_screen_action_indicator == 'stage-2-character-action-' + x +'-detail-easy-shot':
            battle_screen_battleground_click_action('easy shot',screen,buttons, screen_status, button_status, card_database_filter, user, player2)

        elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-' + x +'-detail-tricky-shot':
            battle_screen_battleground_click_action('tricky shot',screen,buttons, screen_status, button_status, card_database_filter, user, player2)

        if int(x) <= 2:
            attribute_name = 'skill_' + str(int(x)+1) + '_lv'
            if int(getattr(user.character_card, attribute_name)) <= int(user.character_card.level):
                screen_status.battle_screen_action_indicator = 'stage-2-character-action-' + str(int(x)+1)
            elif len(user.stage_2_other_card_usable_list) >= 1:
                for position, card in user.character_under_card_by_level.items():
                    if card == user.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
            else:
                if (user.monster_in_play_dict['1'] == ''
                and user.monster_in_play_dict['2'] == ''
                and user.monster_in_play_dict['3'] == ''
                and user.monster_in_play_dict['4'] == ''
                and user.monster_in_play_dict['5'] == ''
                and user.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'
        else:
            if len(user.stage_2_other_card_usable_list) >= 1:
                for position, card in user.character_under_card_by_level.items():
                    if card == user.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
            else:
                if (user.monster_in_play_dict['1'] == ''
                and user.monster_in_play_dict['2'] == ''
                and user.monster_in_play_dict['3'] == ''
                and user.monster_in_play_dict['4'] == ''
                and user.monster_in_play_dict['5'] == ''
                and user.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'



    # Which stage to go when user at stage-2-character-action-1,2,3
    elif 'stage-2-character-action-' in screen_status.battle_screen_action_indicator:
        x = screen_status.battle_screen_action_indicator.replace('stage-2-character-action-','')
        battle_screen_stage_2_action(x, screen,buttons, screen_status, button_status, card_database_filter, user, action)
        if screen_status.battle_screen_action_indicator == 'stage-2-character-action-' + x:
            if int(x) <= 2:
                attribute_name = 'skill_' + str(int(x)+1) + '_lv'
                if int(getattr(user.character_card, attribute_name)) <= int(user.character_card.level):
                    screen_status.battle_screen_action_indicator = 'stage-2-character-action-' + str(int(x)+1)
                elif len(user.stage_2_other_card_usable_list) >= 1:
                    for position, card in user.character_under_card_by_level.items():
                        if card == user.stage_2_other_card_usable_list[0]:
                            screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                else:
                    if (user.monster_in_play_dict['1'] == ''
                    and user.monster_in_play_dict['2'] == ''
                    and user.monster_in_play_dict['3'] == ''
                    and user.monster_in_play_dict['4'] == ''
                    and user.monster_in_play_dict['5'] == ''
                    and user.monster_in_play_dict['6'] == ''):
                        screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                    else:
                        battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                        screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'
            else:
                if len(user.stage_2_other_card_usable_list) >= 1:
                    for position, card in user.character_under_card_by_level.items():
                        if card == user.stage_2_other_card_usable_list[0]:
                            screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                else:
                    if (user.monster_in_play_dict['1'] == ''
                    and user.monster_in_play_dict['2'] == ''
                    and user.monster_in_play_dict['3'] == ''
                    and user.monster_in_play_dict['4'] == ''
                    and user.monster_in_play_dict['5'] == ''
                    and user.monster_in_play_dict['6'] == ''):
                        screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                    else:
                        battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                        screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'
        else:
            pass



    # Which stage to go when user at stage-2-other-action-detail-
    elif 'stage-2-other-action-detail-' in screen_status.battle_screen_action_indicator:
        if screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-think-fast':
            battle_screen_hand_click_action('spawn/think fast',screen,buttons, screen_status, button_status, card_database_filter, user,player2)
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-equip':
            battle_screen_hand_click_action('spawn/equip',screen,buttons, screen_status, button_status, card_database_filter, user,player2)
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast-and-equip':
            battle_screen_hand_click_action('think fast/equip',screen,buttons, screen_status, button_status, card_database_filter, user, player2)
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn':
            battle_screen_hand_click_action('spawn',screen,buttons, screen_status, button_status, card_database_filter, user, player2)
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast':
            battle_screen_hand_click_action('think fast',screen,buttons, screen_status, button_status, card_database_filter, user, player2)
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-equip':
            battle_screen_hand_click_action('equip',screen,buttons, screen_status, button_status, card_database_filter, user, player2)
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-easy-shot':
            battle_screen_battleground_click_action('easy shot',screen,buttons, screen_status, button_status, card_database_filter, user, player2)
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-tricky-shot':
            battle_screen_battleground_click_action('tricky shot',screen,buttons, screen_status, button_status, card_database_filter, user, player2)

        if ('stage-2-other-action-detail-tactic-1' in screen_status.battle_screen_action_indicator
            and button_status.battle_screen_instruction_bar_yes_display == False):
            pass

        elif ('stage-2-other-action-detail-tactic-1' in screen_status.battle_screen_action_indicator
            and button_status.battle_screen_instruction_bar_yes_display == True):
            battle_screen_hand_click_action('use tactic',screen,buttons, screen_status, button_status, card_database_filter, user, player2)

            del user.stage_2_other_card_usable_list[0]
            if len(user.stage_2_other_card_usable_list) >= 1:
                for position, card in user.character_under_card_by_level.items():
                    if card == user.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
            else:
                if (user.monster_in_play_dict['1'] == ''
                and user.monster_in_play_dict['2'] == ''
                and user.monster_in_play_dict['3'] == ''
                and user.monster_in_play_dict['4'] == ''
                and user.monster_in_play_dict['5'] == ''
                and user.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'

        else:

            del user.stage_2_other_card_usable_list[0]
            if len(user.stage_2_other_card_usable_list) >= 1:
                for position, card in user.character_under_card_by_level.items():
                    if card == user.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
            else:
                if (user.monster_in_play_dict['1'] == ''
                and user.monster_in_play_dict['2'] == ''
                and user.monster_in_play_dict['3'] == ''
                and user.monster_in_play_dict['4'] == ''
                and user.monster_in_play_dict['5'] == ''
                and user.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'



    # Which stage to go when user at stage-2-other-action-10-150
    elif 'stage-2-other-action-' in screen_status.battle_screen_action_indicator:
        x = screen_status.battle_screen_action_indicator.replace('stage-2-other-action-','')
        battle_screen_stage_2_action(x, screen,buttons, screen_status, button_status, card_database_filter, user, action)
        if screen_status.battle_screen_action_indicator == 'stage-2-other-action-' + x:
            del user.stage_2_other_card_usable_list[0]
            if len(user.stage_2_other_card_usable_list) >= 1:
                for position, card in user.character_under_card_by_level.items():
                    if card == user.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
            else:
                if (user.monster_in_play_dict['1'] == ''
                and user.monster_in_play_dict['2'] == ''
                and user.monster_in_play_dict['3'] == ''
                and user.monster_in_play_dict['4'] == ''
                and user.monster_in_play_dict['5'] == ''
                and user.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'
        else:
            pass






    elif 'stage-3-monster-' in screen_status.battle_screen_action_indicator:
        x = screen_status.battle_screen_action_indicator.replace('stage-3-monster-','')[0]

        if button_status.battle_screen_instruction_bar_text == "Do you want to attack opponent's character?":
            battle_screen_battleground_click_action('monster_attack_character',screen,buttons, screen_status, button_status, card_database_filter, user,player2)

        elif "Do you want to attack opponent's monster: " in button_status.battle_screen_instruction_bar_text:
            opponent_monster_position = button_status.battle_screen_instruction_bar_text.replace("Do you want to attack opponent's monster: ",'')[0]
            battle_screen_battleground_click_action('monster_attack_monster',screen,buttons, screen_status, button_status, card_database_filter, user,player2,opponent_monster_position)


        if user.monster_in_play_dict[str(int(x)+1)] != '':
            screen_status.battle_screen_action_indicator = 'stage-3-monster-' + str(int(x)+1) + '-action'
            battle_screen_stage_3_action(str(int(x)+1), screen,buttons, screen_status, button_status, card_database_filter, user)

        else:

            screen_status.battle_screen_action_indicator = 'stage-4-end-turn'




    # Which stage to go when user at stage-4-end-turn
    elif screen_status.battle_screen_action_indicator == 'stage-4-end-turn':
        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False

        screen_status.battle_screen_action_indicator = 'player2-stage-0'
        screen_status.battle_screen_player2_action_display_indicator = True


    # Which stage to go when user at stage-4-wait-for-opponent



    print(screen_status.battle_screen_action_indicator)

def battle_screen_instruction_bar_skip_action(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ actions when click on skip on instruction bar"""
    if screen_status.battle_screen_action_indicator == 'stage-0':
        pass
    # Which stage to go when user at stage-1
    elif screen_status.battle_screen_action_indicator == 'stage-1':
        user.stage_2_other_card_usable_list = user.get_stage_2_other_card_usable_list()
        if int(user.character_card.skill_1_lv) <= int(user.character_card.level):
            screen_status.battle_screen_action_indicator = 'stage-2-character-action-1'
        elif len(user.stage_2_other_card_usable_list) >= 1:
            for position, card in user.character_under_card_by_level.items():
                if card == user.stage_2_other_card_usable_list[0]:
                    screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
        else:
            if (user.monster_in_play_dict['1'] == ''
            and user.monster_in_play_dict['2'] == ''
            and user.monster_in_play_dict['3'] == ''
            and user.monster_in_play_dict['4'] == ''
            and user.monster_in_play_dict['5'] == ''
            and user.monster_in_play_dict['6'] == ''):
                screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
            else:
                battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'

    # Which stage to go when user at stage-2-character-action-1,2,3
    elif 'stage-2-character-action-' in screen_status.battle_screen_action_indicator:
        pass

def battle_screen_stage_2_action(position, screen,buttons, screen_status, button_status, card_database_filter, user,action):
    """ Input position of the action, output action according to the type on specific card"""

    if int(position) <= 3:
        attribute_name = 'skill_' + position + '_type'
        character_skill_name = getattr(user.character_card, attribute_name)
        if ('Easy Shot' in character_skill_name
            or 'Stab' in character_skill_name
            or 'Fire Arrow' in character_skill_name
            or 'Bash' in character_skill_name
            or 'Wand Thwack' in character_skill_name
            ):
            action.stage_2_easy_shot('character', screen,buttons, screen_status, button_status, card_database_filter, user, under_position = position)

        elif ('Tricky Shot' in character_skill_name

            ):
            action.stage_2_tricky_shot('character', screen,buttons, screen_status, button_status, card_database_filter, user, under_position = position)

        elif ('Quest' in character_skill_name

            ):
            action.stage_2_quest(screen,buttons, screen_status, button_status, card_database_filter, user)

    else:
        if user.character_under_card_by_level[position].lv_type[-1:] == 'X':
            action_level = user.character_card.level
        else:
            action_level = user.character_under_card_by_level[position].lv_type[-3:]

        if 'Spawn' in user.character_under_card_by_level[position].lv_type:
            if 'Equip' in user.character_under_card_by_level[position].lv_type:
                action.stage_2_spawn_and_equip(position, action_level, screen,buttons, screen_status, button_status, card_database_filter, user)
            elif 'Think Fast' in user.character_under_card_by_level[position].lv_type:
                action.stage_2_spawn_and_think_fast(position, action_level, screen,buttons, screen_status, button_status, card_database_filter, user)
            else:
                action.stage_2_spawn(position, action_level, screen,buttons, screen_status, button_status, card_database_filter, user)
        elif 'Think Fast' in user.character_under_card_by_level[position].lv_type:
            if 'Equip' in user.character_under_card_by_level[position].lv_type:
                action.stage_2_think_fast_and_equip(position, action_level, screen,buttons, screen_status, button_status, card_database_filter, user)
            else:
                action.stage_2_think_fast(position, action_level, screen,buttons, screen_status, button_status, card_database_filter, user)
        elif 'Equip' in user.character_under_card_by_level[position].lv_type:
                action.stage_2_equip(position, action_level, screen,buttons, screen_status, button_status, card_database_filter, user)
        elif ('Easy Shot' in user.character_under_card_by_level[position].lv_type
            or 'Stab' in user.character_under_card_by_level[position].lv_type
            or 'Fire Arrow' in user.character_under_card_by_level[position].lv_type
            or 'Bash' in user.character_under_card_by_level[position].lv_type
            or 'Wand Thwack' in user.character_under_card_by_level[position].lv_type

            ):
            action.stage_2_easy_shot('other', screen,buttons, screen_status, button_status, card_database_filter, user)

        elif ('Tricky Shot' in user.character_under_card_by_level[position].lv_type
            or 'Slash' in user.character_under_card_by_level[position].lv_type
            ):
            action.stage_2_tricky_shot('other', screen,buttons, screen_status, button_status, card_database_filter, user)

        elif ('Quest' in user.character_under_card_by_level[position].lv_type

            ):
            action.stage_2_quest(screen,buttons, screen_status, button_status, card_database_filter, user)

        else:
            print(user.character_under_card_by_level[position].lv_type)

def battle_screen_stage_3_action(position, screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Input position of the action, output action according to the type on specific card"""
    button_status.battle_screen_instruction_bar_text = "Pick a target to attack with monster: " + position
    button_status.battle_screen_instruction_bar_yes_display = False
    button_status.battle_screen_instruction_bar_yes_backend = False




# For offline AI player2 only
def battle_screen_player2_action(screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Actions of player2"""
    # Level up action
    if screen_status.battle_screen_action_indicator == 'player2-stage-0':
        screen_status.battle_screen_action_indicator = 'player2-stage-1'
        button_status.battle_screen_instruction_bar_text = "Now it's your opponent's turn"

    elif screen_status.battle_screen_action_indicator == 'player2-stage-1':
        screen_status.battle_screen_action_indicator = 'player2-stage-1-level-up'
        button_status.battle_screen_instruction_bar_text = 'Opponent is deciding whether to level up '


    elif screen_status.battle_screen_action_indicator == 'player2-stage-1-level-up':
        if player2.hand_list == []:
            button_status.battle_screen_instruction_bar_text = 'Opponent decide not to level up'
            pass # skip action
        else:
            located_card = player2.hand_list[0]
            for i in range(1,16):
                if player2.character_under_card_by_level[str(i*10)] == '':
                    player2.character_under_card_by_level[str(i*10)] = located_card
                    break
            player2.hand_list.remove(located_card)
            player2.character_card.level = str(int(player2.character_card.level) + 10)
            player2.character_card.health = str(int(player2.character_card.health) + 20)

            button_status.battle_screen_instruction_bar_text = 'Opponent has leveled up to lv ' + player2.character_card.level
            player2.stage_2_other_card_usable_list = player2.get_stage_2_other_card_usable_list()

            if int(player2.character_card.skill_1_lv) <= int(player2.character_card.level):
                screen_status.battle_screen_action_indicator = 'player2-stage-2-character-action-1'
                button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_card.skill_1_type
                #pygame.time.delay(3000)
            elif len(player2.stage_2_other_card_usable_list) >= 1:
                for position, card in player2.character_under_card_by_level.items():
                    if card == player2.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-' + position
                        button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_under_card_by_level[position].lv_type
                        #pygame.time.delay(3000)
            else:
                if (player2.monster_in_play_dict['1'] == ''
                and player2.monster_in_play_dict['2'] == ''
                and player2.monster_in_play_dict['3'] == ''
                and player2.monster_in_play_dict['4'] == ''
                and player2.monster_in_play_dict['5'] == ''
                and player2.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'
                    button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
                    #pygame.time.delay(3000)
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-1-action'
                    button_status.battle_screen_instruction_bar_text = "Opponent deciding action for first monster"
                    #pygame.time.delay(3000)


    #
    elif 'player2-stage-2-character-action-' in screen_status.battle_screen_action_indicator:
        x = screen_status.battle_screen_action_indicator.replace('player2-stage-2-character-action-','')
        attribute_name = 'skill_' + x + '_type'
        character_skill_name = getattr(player2.character_card, attribute_name)

        if ('Easy Shot' in character_skill_name
            or 'Stab' in character_skill_name
            or 'Fire Arrow' in character_skill_name
            or 'Bash' in character_skill_name
            or 'Wand Thwack' in character_skill_name
            ):
            user.character_card.health = str(int(user.character_card.health)-10)

        elif ('Tricky Shot' in character_skill_name

            ):
            user.character_card.health = str(int(user.character_card.health)-20)

        elif ('Quest' in character_skill_name

            ):
            player2.hand_list.append(player2.remain_deck_list[0])
            del player2.remain_deck_list[0]

        if int(x) <= 2:
            attribute_name = 'skill_' + str(int(x)+1) + '_lv'
            if int(getattr(player2.character_card, attribute_name)) <= int(player2.character_card.level):
                screen_status.battle_screen_action_indicator = 'player2-stage-2-character-action-' + str(int(x)+1)
                button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use character action: ' +  str(int(x)+1)
                #pygame.time.delay(3000)
            elif len(player2.stage_2_other_card_usable_list) >= 1:
                for position, card in player2.character_under_card_by_level.items():
                    if card == player2.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-' + position
                        button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_under_card_by_level[position].lv_type
                        #pygame.time.delay(3000)
            else:
                if (player2.monster_in_play_dict['1'] == ''
                and player2.monster_in_play_dict['2'] == ''
                and player2.monster_in_play_dict['3'] == ''
                and player2.monster_in_play_dict['4'] == ''
                and player2.monster_in_play_dict['5'] == ''
                and player2.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'
                    button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
                    #pygame.time.delay(3000)
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-1-action'
                    button_status.battle_screen_instruction_bar_text = "Opponent deciding action for first monster"
                    #pygame.time.delay(3000)
        else:
            if len(player2.stage_2_other_card_usable_list) >= 1:
                for position, card in player2.character_under_card_by_level.items():
                    if card == player2.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-' + position
                        button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_under_card_by_level[position].lv_type
                        #pygame.time.delay(3000)
            else:
                if (player2.monster_in_play_dict['1'] == ''
                and player2.monster_in_play_dict['2'] == ''
                and player2.monster_in_play_dict['3'] == ''
                and player2.monster_in_play_dict['4'] == ''
                and player2.monster_in_play_dict['5'] == ''
                and player2.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'
                    button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
                    #pygame.time.delay(3000)
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-1-action'
                    button_status.battle_screen_instruction_bar_text = "Opponent deciding action for first monster"
                    #pygame.time.delay(3000)



    # Which stage to go when user at stage-2-other-action-detail-
    elif 'player2-stage-2-other-action-detail-' in screen_status.battle_screen_action_indicator:

        if screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-spawn-and-think-fast':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'monster' or card.card_type == 'tactic')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a monster/tactic lv','').replace(' to play','')))):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                if located_card.card_type == 'monster':
                    for i in range(1,7):
                        if player2.monster_in_play_dict[str(i)] == '':
                            player2.monster_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)
                else:
                    player2.hand_list.remove(located_card)
                    print('Opponent use tactic')

        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-spawn-and-equip':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'monster' or card.card_type == 'item')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a monster/item lv','').replace(' to play','')))):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                if located_card.card_type == 'monster':
                    for i in range(1,7):
                        if player2.monster_in_play_dict[str(i)] == '':
                            player2.monster_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)
                else:
                    for i in range(1,7):
                        if player2.item_in_play_dict[str(i)] == '':
                            player2.item_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)

        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-think-fast-and-equip':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'tactic' or card.card_type == 'item')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a tactic/item lv','').replace(' to play','')))):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                if located_card.card_type == 'item':
                    for i in range(1,7):
                        if player2.item_in_play_dict[str(i)] == '':
                            player2.item_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)
                else:
                    player2.hand_list.remove(located_card)
                    print('Opponent use tactic')

        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-spawn':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'monster')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a monster lv','').replace(' to play','')))):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                for i in range(1,7):
                    if player2.monster_in_play_dict[str(i)] == '':
                        player2.monster_in_play_dict[str(i)] = located_card
                        break
                player2.hand_list.remove(located_card)


        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-think-fast':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'tactic')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a tactic lv','').replace(' to play','')))):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                player2.hand_list.remove(located_card)
                print('Opponent use tactic')

        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-equip':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'item')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a item lv','').replace(' to play','')))):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                for i in range(1,7):
                    if player2.item_in_play_dict[str(i)] == '':
                        player2.item_in_play_dict[str(i)] = located_card
                        break
                player2.hand_list.remove(located_card)


        del player2.stage_2_other_card_usable_list[0]
        if len(player2.stage_2_other_card_usable_list) >= 1:
            for position, card in player2.character_under_card_by_level.items():
                if card == player2.stage_2_other_card_usable_list[0]:
                    screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-' + position
                    button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_under_card_by_level[position].lv_type
                    #pygame.time.delay(3000)
        else:
            if (player2.monster_in_play_dict['1'] == ''
            and player2.monster_in_play_dict['2'] == ''
            and player2.monster_in_play_dict['3'] == ''
            and player2.monster_in_play_dict['4'] == ''
            and player2.monster_in_play_dict['5'] == ''
            and player2.monster_in_play_dict['6'] == ''):
                screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'
                button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
                #pygame.time.delay(3000)
            else:
                battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-1-action'
                button_status.battle_screen_instruction_bar_text = "Opponent deciding action for first monster"
                #pygame.time.delay(3000)




    #
    elif 'player2-stage-2-other-action-' in screen_status.battle_screen_action_indicator:
        x = screen_status.battle_screen_action_indicator.replace('player2-stage-2-other-action-','')

        # Check if action level is X
        if player2.character_under_card_by_level[x].lv_type[-1:] == 'X':
            action_level = player2.character_card.level
        else:
            action_level = player2.character_under_card_by_level[x].lv_type[-3:]

        if 'Spawn' in player2.character_under_card_by_level[x].lv_type:
            if 'Equip' in player2.character_under_card_by_level[x].lv_type:
                screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-spawn-and-equip'
                button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a monster/item lv' + str(int(action_level)) + ' to play'
                #pygame.time.delay(3000)
            elif 'Think Fast' in player2.character_under_card_by_level[x].lv_type:
                screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-spawn-and-think-fast'
                button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a monster/tactic lv' + str(int(action_level)) + ' to play'
                #pygame.time.delay(3000)
            else:
                screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-spawn'
                button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a monster lv' + str(int(action_level)) + ' to play'
                #pygame.time.delay(3000)
        elif 'Think Fast' in player2.character_under_card_by_level[x].lv_type:
            if 'Equip' in player2.character_under_card_by_level[x].lv_type:

                screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-think-fast-and-equip'
                button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a tactic/item lv' + str(int(action_level)) + ' to play'
                #pygame.time.delay(3000)
            else:
                screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-think-fast'
                button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a tactic lv' + str(int(action_level)) + ' to play'
                #pygame.time.delay(3000)
        elif 'Equip' in player2.character_under_card_by_level[x].lv_type:
                screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-equip'
                button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a item lv' + str(int(action_level)) + ' to play'
                #pygame.time.delay(3000)
        else:
            print(player2.character_under_card_by_level[x].lv_type)

        if screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-' + x:
            del player2.stage_2_other_card_usable_list[0]
            if len(player2.stage_2_other_card_usable_list) >= 1:
                for position, card in player2.character_under_card_by_level.items():
                    if card == player2.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-' + position
                        button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_under_card_by_level[position].lv_type
                        #pygame.time.delay(3000)
            else:
                if (player2.monster_in_play_dict['1'] == ''
                and player2.monster_in_play_dict['2'] == ''
                and player2.monster_in_play_dict['3'] == ''
                and player2.monster_in_play_dict['4'] == ''
                and player2.monster_in_play_dict['5'] == ''
                and player2.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'
                    button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
                    #pygame.time.delay(3000)
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-1-action'
                    button_status.battle_screen_instruction_bar_text = "Opponent deciding action for first monster"
                    #pygame.time.delay(3000)
        else:
            pass







    elif screen_status.battle_screen_action_indicator == 'player2-stage-3-monster-1-action':
        screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'



    # Which stage to go when user at stage-4-end-turn
    elif screen_status.battle_screen_action_indicator == 'player2-stage-4-end-turn':
            button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
            #pygame.time.delay(3000)
            screen_status.battle_screen_action_indicator = 'stage-1'
            screen_status.battle_screen_player2_action_display_indicator = False # No longer doing player2 loops
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True






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
