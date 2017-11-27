import sys
import pygame
from card import Character, Monster
from card_database import *

# available character(missing one warrior for 2 for each class): card_01_16, card_01_37, card_01_59, card_01_64, card_01_89, card_03_11, card_05_30,
# Card in database that playable in current version of the game:
card_list_playable = [
    # Set 1

    # Set 2

    # Set 3

    # Set 4

    # Set 5


]


# Testing purpose, no character card
card_for_test = [
    # Set 1

    # Set 2

    # Set 3

    # Set 4

    # Set 5




]



# All cards that in card_database
card_list = [
    # Set 1
    card_01_01, card_01_03, card_01_04, card_01_05, card_01_06, card_01_08,
    card_01_11, card_01_13, card_01_14, card_01_16,
    card_01_21, card_01_23, card_01_25, card_01_27, card_01_28,
    card_01_31, card_01_33, card_01_34, card_01_37,
    card_01_40, card_01_42, card_01_44,
    card_01_53, card_01_55, card_01_59,
    card_01_60, card_01_61, card_01_64, card_01_65, card_01_66, card_01_69,
    card_01_70, card_01_71, card_01_76, card_01_77, card_01_78,
    card_01_81, card_01_85, card_01_86, card_01_87, card_01_89,
    card_01_90, card_01_91, card_01_93, card_01_95, card_01_96,
    # Set 2
    card_02_01, card_02_02, card_02_03, card_02_05, card_02_07,
    card_02_15, card_02_18,
    card_02_20, card_02_23, card_02_24, card_02_25, card_02_29,
    card_02_31, card_02_33, card_02_34,
    card_02_46, card_02_47, card_02_48, card_02_49,
    card_02_52, card_02_60,
    # Set 3
    card_03_02, card_03_03, card_03_05, card_03_07, card_03_08, card_03_09,
    card_03_11, card_03_16, card_03_17,
    card_03_22, card_03_25, card_03_29,
    card_03_35, card_03_39,
    card_03_40, card_03_43, card_03_44, card_03_45, card_03_46, card_03_48, card_03_49,
    card_03_51, card_03_53, card_03_56,
    # Set 4
    card_04_06, card_04_08,
    card_04_10, card_04_12, card_04_15, card_04_16, card_04_18,
    card_04_20, card_04_23, card_04_24, card_04_26, card_04_27, card_04_29,
    card_04_31, card_04_32, card_04_34, card_04_37,
    card_04_40, card_04_42, card_04_44, card_04_49,
    card_04_51, card_04_52, card_04_55, card_04_56, card_04_58, card_04_59, card_04_60,
    # Set 5
    card_05_02, card_05_03, card_05_06, card_05_09,
    card_05_10, card_05_11, card_05_12,
    card_05_21, card_05_23, card_05_25,
    card_05_30, card_05_32,
    card_05_40, card_05_43, card_05_45, card_05_48,
    card_05_50, card_05_51, card_05_52, card_05_53, card_05_56, card_05_57,
    card_05_61, card_05_65, card_05_68,
    card_05_76, card_05_77, card_05_78,
    card_05_81, card_05_85, card_05_86, card_05_87, card_05_88, card_05_90,
]

class Card_database_filter():
    """Contains filters for card database"""
    def __init__(self, character = False, bowman = False, magician = False, thief = False, warrior = False, jobless = False ):
        self.character = character
        self.bowman = bowman
        self.magician = magician
        self.thief = thief
        self.warrior = warrior
        self.jobless = jobless






def request_card_list(card_database_filter, input_list = card_list_playable): #Input list is the cards available in the game
    """Return cards that user request"""
    req_list = []

    if (
    card_database_filter.character == False and
    card_database_filter.bowman == False and
    card_database_filter.magician == False and
    card_database_filter.thief == False and
    card_database_filter.warrior == False and
    card_database_filter.jobless == False
    ):

        return input_list

    else:
        # Character filter
        if card_database_filter.character:

            if card_database_filter.bowman:
                for card in input_list:
                    if card.card_type == 'character' and card.job == 'bowman':
                        req_list.append(card)


            if card_database_filter.magician:
                for card in input_list:
                    if card.card_type == 'character' and card.job == 'magician':
                        req_list.append(card)


            if card_database_filter.thief:
                for card in input_list:
                    if card.card_type == 'character' and card.job == 'thief':
                        req_list.append(card)

            if card_database_filter.warrior:
                for card in input_list:
                    if card.card_type == 'character' and card.job == 'warrior':
                        req_list.append(card)

            if card_database_filter.jobless:
                for card in input_list:
                    if card.card_type == 'character' and card.job == 'jobless':
                        req_list.append(card)

            if (
            card_database_filter.bowman == False and
            card_database_filter.magician == False and
            card_database_filter.thief == False and
            card_database_filter.warrior == False and
            card_database_filter.jobless == False
            ):
                for card in input_list:
                    if card.card_type == 'character':
                        req_list.append(card)


            return req_list

        # Other filter
        else:
            if card_database_filter.bowman:
                for card in input_list:
                    if card.job == 'bowman':
                        req_list.append(card)

            if card_database_filter.magician:
                for card in input_list:
                    if card.job == 'magician':
                        req_list.append(card)

            if card_database_filter.thief:
                for card in input_list:
                    if card.job == 'thief':
                        req_list.append(card)

            if card_database_filter.warrior:
                for card in input_list:
                    if card.job == 'warrior':
                        req_list.append(card)

            if card_database_filter.jobless:
                for card in input_list:
                    if card.job == 'jobless':
                        req_list.append(card)


        return req_list










#--------
