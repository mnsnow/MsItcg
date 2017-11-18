import sys
import pygame
from card import Card

#-----------------------Set 1--------------------------------------------
card_01_13 = Card(set_number='01',card_number='13',card_type='monster',job='bowman',level='22',
attack='20',health='40',lv_type='spawn/equip-30',lv_active_level='40',special_effect='')

card_01_23 = Card(set_number='01',card_number='23',card_type='monster',job='bowman',level='20',
attack='30',health='20',lv_type='spawn/equip-50',lv_active_level='60',special_effect='')

card_01_27 = Card(set_number='01',card_number='27',card_type='monster',job='magician',level='22',
attack='10',health='40',lv_type='',lv_active_level='40',special_effect='')

card_01_31 = Card(set_number='01',card_number='31',card_type='monster',job='magician',level='21',
attack='30',health='30',lv_type='spawn-30',lv_active_level='30',special_effect='')

card_01_40 = Card(set_number='01',card_number='40',card_type='monster',job='magician',level='12',
attack='10',health='10',lv_type='quest',lv_active_level='one-time',special_effect='')

card_01_65 = Card(set_number='01',card_number='65',card_type='monster',job='thief',level='8',
attack='30',health='10',lv_type='equip-40',lv_active_level='30',special_effect='')

card_01_69 = Card(set_number='01',card_number='69',card_type='monster',job='thief',level='4',
attack='10',health='20',lv_type='spawn-90',lv_active_level='70',special_effect='tough')

card_01_70 = Card(set_number='01',card_number='70',card_type='monster',job='thief',level='23',
attack='20',health='20',lv_type='',lv_active_level='30',special_effect='')

card_01_77 = Card(set_number='01',card_number='77',card_type='monster',job='warrior',level='15',
attack='10',health='40',lv_type='spawn/equip-90',lv_active_level='70',special_effect='')

card_01_86 = Card(set_number='01',card_number='86',card_type='monster',job='warrior',level='10',
attack='20',health='20',lv_type='spawn-20',lv_active_level='10',special_effect='')

card_01_90 = Card(set_number='01',card_number='90',card_type='monster',job='warrior',level='6',
attack='10',health='10',lv_type='refresh',lv_active_level='40',special_effect='')


#-----------------------Set 2--------------------------------------------
card_02_01 = Card(set_number='02',card_number='01',card_type='monster',job='bowman',level='20',
attack='30',health='20',lv_type='snare',lv_active_level='40',special_effect='')

card_02_02 = Card(set_number='02',card_number='02',card_type='monster',job='bowman',level='20',
attack='20',health='20',lv_type='spawn-30',lv_active_level='30',special_effect='')

card_02_25 = Card(set_number='02',card_number='25',card_type='monster',job='magician',level='19',
attack='10',health='40',lv_type='spawn-140',lv_active_level='90',special_effect='')

card_02_29 = Card(set_number='02',card_number='29',card_type='monster',job='magician',level='12',
attack='20',health='20',lv_type='think fast-90',lv_active_level='70',special_effect='')

card_02_47 = Card(set_number='02',card_number='47',card_type='monster',job='warrior',level='12',
attack='10',health='30',lv_type='spawn-60',lv_active_level='50',special_effect='')

card_02_49 = Card(set_number='02',card_number='49',card_type='monster',job='warrior',level='23',
attack='10',health='20',lv_type='',lv_active_level='20',special_effect='')


#-----------------------Set 3--------------------------------------------
card_03_43 = Card(set_number='03',card_number='43',card_type='monster',job='thief',level='22',
attack='0',health='10',lv_type='',lv_active_level='40',special_effect='')

card_03_56 = Card(set_number='03',card_number='56',card_type='monster',job='warrior',level='7',
attack='10',health='20',lv_type='spawn-80',lv_active_level='60',special_effect='')


#-----------------------Set 4--------------------------------------------
card_04_08 = Card(set_number='04',card_number='08',card_type='monster',job='bowman',level='5',
attack='10',health='20',lv_type='spawn-30',lv_active_level='20',special_effect='NPC-QUEST')

card_04_20 = Card(set_number='04',card_number='20',card_type='monster',job='magician',level='20',
attack='20',health='20',lv_type='spawn-30',lv_active_level='30',special_effect='')

card_04_27 = Card(set_number='04',card_number='27',card_type='monster',job='magician',level='10',
attack='10',health='20',lv_type='buff a friend',lv_active_level='10',special_effect='')

card_04_34 = Card(set_number='04',card_number='34',card_type='monster',job='thief',level='10',
attack='20',health='10',lv_type='spawn-20',lv_active_level='20',special_effect='')

card_04_55 = Card(set_number='04',card_number='55',card_type='monster',job='warrior',level='19',
attack='10',health='10',lv_type='stick together',lv_active_level='50',special_effect='')

card_04_60 = Card(set_number='04',card_number='60',card_type='monster',job='warrior',level='23',
attack='20',health='30',lv_type='',lv_active_level='one-time',special_effect='')


#-----------------------Set 5--------------------------------------------
card_05_23 = Card(set_number='05',card_number='23',card_type='monster',job='magician',level='22',
attack='10',health='40',lv_type='',lv_active_level='40',special_effect='')

card_05_25 = Card(set_number='05',card_number='25',card_type='monster',job='magician',level='22',
attack='30',health='90',lv_type='',lv_active_level='one-time',special_effect='')

card_05_52 = Card(set_number='05',card_number='52',card_type='monster',job='thief',level='8',
attack='30',health='30',lv_type='spy',lv_active_level='one-time',special_effect='')

card_05_77 = Card(set_number='05',card_number='77',card_type='monster',job='jobless',level='2',
attack='10',health='20',lv_type='bash-10',lv_active_level='10',special_effect='N/A')
