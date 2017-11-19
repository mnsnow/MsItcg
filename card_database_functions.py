import sys
import pygame
from card import Card
from card_database import *

card_list = [
    card_01_13, card_01_23, card_01_27, card_01_31, card_01_40, card_01_65, card_01_69, card_01_70, card_01_77, card_01_86, card_01_90,
    card_02_01, card_02_02, card_02_25, card_02_29, card_02_47, card_02_49,
    card_03_43, card_03_56,
    card_04_08, card_04_20, card_04_27, card_04_34, card_04_55, card_04_60,
    card_05_23, card_05_25, card_05_52, card_05_77,
]

class Card_database_filter():
    """Contains filters for card database"""
    def __init__(self, bowman = False, magician = False, thief = False, warrior = False, jobless = False ):
        self.bowman = bowman
        self.magician = magician
        self.thief = thief
        self.warrior = warrior
        self.jobless = jobless







def request_card_list(card_database_filter, input_list = card_list):
    """Return cards that user request"""
    req_list = []

    if (
    card_database_filter.bowman == False and
    card_database_filter.magician == False and
    card_database_filter.thief == False and
    card_database_filter.warrior == False and
    card_database_filter.jobless == False
    ):

        return input_list

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
