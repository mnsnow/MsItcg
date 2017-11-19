import sys
import pygame
from card import Character, Monster

#-----------------------Set 1--------------------------------------------
card_01_08 = Monster(set_number='01',card_number='08',card_type='monster',job='bowman',level='30',
attack='30',health='20',lv_type='',lv_active_level='30',special_effect='')

card_01_11 = Monster(set_number='01',card_number='11',card_type='monster',job='bowman',level='28',
attack='20',health='20',lv_type='',lv_active_level='20',special_effect='')

card_01_13 = Monster(set_number='01',card_number='13',card_type='monster',job='bowman',level='22',
attack='20',health='40',lv_type='spawn/equip-30',lv_active_level='40',special_effect='')

card_01_23 = Monster(set_number='01',card_number='23',card_type='monster',job='bowman',level='20',
attack='30',health='20',lv_type='spawn/equip-50',lv_active_level='60',special_effect='')

card_01_27 = Monster(set_number='01',card_number='27',card_type='monster',job='magician',level='22',
attack='10',health='40',lv_type='',lv_active_level='40',special_effect='')

card_01_31 = Monster(set_number='01',card_number='31',card_type='monster',job='magician',level='21',
attack='30',health='30',lv_type='spawn-30',lv_active_level='30',special_effect='')

card_01_40 = Monster(set_number='01',card_number='40',card_type='monster',job='magician',level='12',
attack='10',health='10',lv_type='quest',lv_active_level='one-time',special_effect='')

card_01_53 = Monster(set_number='01',card_number='53',card_type='monster',job='thief',level='25',
attack='30',health='20',lv_type='',lv_active_level='40',special_effect='')

card_01_60 = Monster(set_number='01',card_number='60',card_type='monster',job='thief',level='24',
attack='60',health='30',lv_type='',lv_active_level='30',special_effect='')

card_01_61 = Monster(set_number='01',card_number='61',card_type='monster',job='thief',level='30',
attack='30',health='20',lv_type='',lv_active_level='70',special_effect='')

card_01_65 = Monster(set_number='01',card_number='65',card_type='monster',job='thief',level='8',
attack='30',health='10',lv_type='equip-40',lv_active_level='30',special_effect='')

card_01_69 = Monster(set_number='01',card_number='69',card_type='monster',job='thief',level='4',
attack='10',health='20',lv_type='spawn-90',lv_active_level='70',special_effect='tough')

card_01_70 = Monster(set_number='01',card_number='70',card_type='monster',job='thief',level='23',
attack='20',health='20',lv_type='',lv_active_level='30',special_effect='')

card_01_77 = Monster(set_number='01',card_number='77',card_type='monster',job='warrior',level='15',
attack='10',health='40',lv_type='spawn/equip-90',lv_active_level='70',special_effect='')

card_01_86 = Monster(set_number='01',card_number='86',card_type='monster',job='warrior',level='10',
attack='20',health='20',lv_type='spawn-20',lv_active_level='10',special_effect='')

card_01_87 = Monster(set_number='01',card_number='87',card_type='monster',job='warrior',level='30',
attack='20',health='30',lv_type='',lv_active_level='one-time',special_effect='')

card_01_90 = Monster(set_number='01',card_number='90',card_type='monster',job='warrior',level='6',
attack='10',health='10',lv_type='refresh',lv_active_level='40',special_effect='')

card_01_95 = Monster(set_number='01',card_number='95',card_type='monster',job='warrior',level='25',
attack='30',health='30',lv_type='',lv_active_level='40',special_effect='')


#-----------------------Set 2--------------------------------------------
card_02_01 = Monster(set_number='02',card_number='01',card_type='monster',job='bowman',level='20',
attack='30',health='20',lv_type='snare',lv_active_level='40',special_effect='')

card_02_02 = Monster(set_number='02',card_number='02',card_type='monster',job='bowman',level='20',
attack='20',health='20',lv_type='spawn-30',lv_active_level='30',special_effect='')

card_02_03 = Monster(set_number='02',card_number='03',card_type='monster',job='bowman',level='30',
attack='30',health='10',lv_type='',lv_active_level='20',special_effect='')

card_02_07 = Character(set_number='02',card_number='07',card_type='character',job='bowman',level='0',
health='210',skill_1_lv = '20', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_02_23 = Character(set_number='02',card_number='23',card_type='character',job='magician',level='0',
health='170',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_02_25 = Monster(set_number='02',card_number='25',card_type='monster',job='magician',level='19',
attack='10',health='40',lv_type='spawn-140',lv_active_level='90',special_effect='')

card_02_29 = Monster(set_number='02',card_number='29',card_type='monster',job='magician',level='12',
attack='20',health='20',lv_type='think fast-90',lv_active_level='70',special_effect='')

card_02_47 = Monster(set_number='02',card_number='47',card_type='monster',job='warrior',level='12',
attack='10',health='30',lv_type='spawn-60',lv_active_level='50',special_effect='')

card_02_49 = Monster(set_number='02',card_number='49',card_type='monster',job='warrior',level='23',
attack='10',health='20',lv_type='',lv_active_level='20',special_effect='')


#-----------------------Set 3--------------------------------------------
card_03_05 = Monster(set_number='03',card_number='05',card_type='monster',job='bowman',level='25',
attack='10',health='20',lv_type='',lv_active_level='50',special_effect='')

card_03_43 = Monster(set_number='03',card_number='43',card_type='monster',job='thief',level='22',
attack='0',health='10',lv_type='',lv_active_level='40',special_effect='')

card_03_45 = Monster(set_number='03',card_number='45',card_type='monster',job='thief',level='24',
attack='40',health='10',lv_type='',lv_active_level='50',special_effect='')

card_03_56 = Monster(set_number='03',card_number='56',card_type='monster',job='warrior',level='7',
attack='10',health='20',lv_type='spawn-80',lv_active_level='60',special_effect='')


#-----------------------Set 4--------------------------------------------
card_04_06 = Monster(set_number='04',card_number='06',card_type='monster',job='bowman',level='25',
attack='30',health='30',lv_type='',lv_active_level='40',special_effect='')

card_04_08 = Monster(set_number='04',card_number='08',card_type='monster',job='bowman',level='5',
attack='10',health='20',lv_type='spawn-30',lv_active_level='20',special_effect='NPC-QUEST')

card_04_20 = Monster(set_number='04',card_number='20',card_type='monster',job='magician',level='20',
attack='20',health='20',lv_type='spawn-30',lv_active_level='30',special_effect='')

card_04_27 = Monster(set_number='04',card_number='27',card_type='monster',job='magician',level='10',
attack='10',health='20',lv_type='buff a friend',lv_active_level='10',special_effect='')

card_04_32 = Monster(set_number='04',card_number='32',card_type='monster',job='thief',level='27',
attack='30',health='20',lv_type='',lv_active_level='80',special_effect='')

card_04_34 = Monster(set_number='04',card_number='34',card_type='monster',job='thief',level='10',
attack='20',health='10',lv_type='spawn-20',lv_active_level='20',special_effect='')

card_04_55 = Monster(set_number='04',card_number='55',card_type='monster',job='warrior',level='19',
attack='10',health='10',lv_type='stick together',lv_active_level='50',special_effect='')

card_04_60 = Monster(set_number='04',card_number='60',card_type='monster',job='warrior',level='23',
attack='20',health='30',lv_type='',lv_active_level='one-time',special_effect='')


#-----------------------Set 5--------------------------------------------
card_05_23 = Monster(set_number='05',card_number='23',card_type='monster',job='magician',level='22',
attack='10',health='40',lv_type='',lv_active_level='40',special_effect='')

card_05_25 = Monster(set_number='05',card_number='25',card_type='monster',job='magician',level='22',
attack='30',health='90',lv_type='',lv_active_level='one-time',special_effect='')

card_05_43 = Monster(set_number='05',card_number='43',card_type='monster',job='thief',level='29',
attack='20',health='30',lv_type='',lv_active_level='50',special_effect='')

card_05_45 = Character(set_number='05',card_number='45',card_type='character',job='thief',level='0',
health='200',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_05_52 = Monster(set_number='05',card_number='52',card_type='monster',job='thief',level='8',
attack='30',health='30',lv_type='spy',lv_active_level='one-time',special_effect='')

card_05_53 = Monster(set_number='05',card_number='53',card_type='monster',job='thief',level='23',
attack='30',health='10',lv_type='',lv_active_level='30',special_effect='')

card_05_61 = Character(set_number='05',card_number='61',card_type='character',job='warrior',level='0',
health='280',skill_1_lv = '20', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_05_77 = Monster(set_number='05',card_number='77',card_type='monster',job='jobless',level='2',
attack='10',health='20',lv_type='bash-10',lv_active_level='10',special_effect='N/A')

card_05_90 = Character(set_number='05',card_number='90',card_type='character',job='jobless',level='0',
health='180',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '30', skill_3_type = '')
