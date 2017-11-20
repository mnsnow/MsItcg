import sys
import pygame
from card import Character, Monster

#-----------------------Set 1--------------------------------------------
card_01_05 = Monster(set_number='01',card_number='05',card_type='monster',job='bowman',level='72',
attack='70',health='70',lv_type='',lv_active_level='80',special_effect='')

card_01_06 = Monster(set_number='01',card_number='06',card_type='monster',job='bowman',level='35',
attack='30',health='40',lv_type='',lv_active_level='50',special_effect='')

card_01_08 = Monster(set_number='01',card_number='08',card_type='monster',job='bowman',level='30',
attack='30',health='20',lv_type='',lv_active_level='30',special_effect='')

card_01_11 = Monster(set_number='01',card_number='11',card_type='monster',job='bowman',level='28',
attack='20',health='20',lv_type='',lv_active_level='20',special_effect='')

card_01_13 = Monster(set_number='01',card_number='13',card_type='monster',job='bowman',level='22',
attack='20',health='40',lv_type='spawn/equip-30',lv_active_level='40',special_effect='')

card_01_14 = Monster(set_number='01',card_number='14',card_type='monster',job='bowman',level='35',
attack='30',health='30',lv_type='',lv_active_level='one-time',special_effect='')

card_01_16 = Character(set_number='01',card_number='16',card_type='character',job='bowman',level='0',
health='200',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_01_21 = Character(set_number='01',card_number='21',card_type='character',job='bowman',level='0',
health='210',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '10', skill_2_type = '',skill_3_lv = '60', skill_3_type = '')

card_01_23 = Monster(set_number='01',card_number='23',card_type='monster',job='bowman',level='20',
attack='30',health='20',lv_type='spawn/equip-50',lv_active_level='60',special_effect='')

card_01_27 = Monster(set_number='01',card_number='27',card_type='monster',job='magician',level='22',
attack='10',health='40',lv_type='',lv_active_level='40',special_effect='')

card_01_31 = Monster(set_number='01',card_number='31',card_type='monster',job='magician',level='21',
attack='30',health='30',lv_type='spawn-30',lv_active_level='30',special_effect='')

card_01_34 = Monster(set_number='01',card_number='34',card_type='monster',job='magician',level='73',
attack='60',health='90',lv_type='',lv_active_level='one-time',special_effect='')

card_01_37 = Character(set_number='01',card_number='37',card_type='character',job='magician',level='0',
health='190',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '30', skill_3_type = '')

card_01_40 = Monster(set_number='01',card_number='40',card_type='monster',job='magician',level='12',
attack='10',health='10',lv_type='quest',lv_active_level='one-time',special_effect='')

card_01_44 = Character(set_number='01',card_number='44',card_type='character',job='magician',level='0',
health='180',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '70', skill_3_type = '')

card_01_53 = Monster(set_number='01',card_number='53',card_type='monster',job='thief',level='25',
attack='30',health='20',lv_type='',lv_active_level='40',special_effect='')

card_01_59 = Character(set_number='01',card_number='59',card_type='character',job='thief',level='0',
health='220',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '10', skill_2_type = '',skill_3_lv = '20', skill_3_type = '')

card_01_60 = Monster(set_number='01',card_number='60',card_type='monster',job='thief',level='24',
attack='60',health='30',lv_type='',lv_active_level='30',special_effect='')

card_01_61 = Monster(set_number='01',card_number='61',card_type='monster',job='thief',level='30',
attack='30',health='20',lv_type='',lv_active_level='70',special_effect='')

card_01_64 = Character(set_number='01',card_number='64',card_type='character',job='thief',level='0',
health='200',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_01_65 = Monster(set_number='01',card_number='65',card_type='monster',job='thief',level='8',
attack='30',health='10',lv_type='equip-40',lv_active_level='30',special_effect='')

card_01_66 = Monster(set_number='01',card_number='66',card_type='monster',job='thief',level='32',
attack='30',health='30',lv_type='',lv_active_level='one-time',special_effect='')

card_01_69 = Monster(set_number='01',card_number='69',card_type='monster',job='thief',level='4',
attack='10',health='20',lv_type='spawn-90',lv_active_level='70',special_effect='tough')

card_01_70 = Monster(set_number='01',card_number='70',card_type='monster',job='thief',level='23',
attack='20',health='20',lv_type='',lv_active_level='30',special_effect='')

card_01_71 = Monster(set_number='01',card_number='71',card_type='monster',job='thief',level='63',
attack='50',health='40',lv_type='',lv_active_level='one-time',special_effect='')

card_01_76 = Monster(set_number='01',card_number='76',card_type='monster',job='warrior',level='32',
attack='10',health='50',lv_type='',lv_active_level='30',special_effect='')

card_01_77 = Monster(set_number='01',card_number='77',card_type='monster',job='warrior',level='15',
attack='10',health='40',lv_type='spawn/equip-90',lv_active_level='70',special_effect='')

card_01_81 = Monster(set_number='01',card_number='81',card_type='monster',job='warrior',level='63',
attack='50',health='60',lv_type='',lv_active_level='50',special_effect='')

card_01_86 = Monster(set_number='01',card_number='86',card_type='monster',job='warrior',level='10',
attack='20',health='20',lv_type='spawn-20',lv_active_level='10',special_effect='')

card_01_87 = Monster(set_number='01',card_number='87',card_type='monster',job='warrior',level='30',
attack='20',health='30',lv_type='',lv_active_level='one-time',special_effect='')

card_01_89 = Character(set_number='01',card_number='89',card_type='character',job='warrior',level='0',
health='240',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '30', skill_3_type = '')

card_01_90 = Monster(set_number='01',card_number='90',card_type='monster',job='warrior',level='6',
attack='10',health='10',lv_type='refresh',lv_active_level='40',special_effect='')

card_01_91 = Character(set_number='01',card_number='91',card_type='character',job='warrior',level='0',
health='260',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_01_93 = Monster(set_number='01',card_number='93',card_type='monster',job='warrior',level='70',
attack='50',health='40',lv_type='',lv_active_level='one-time',special_effect='')

card_01_95 = Monster(set_number='01',card_number='95',card_type='monster',job='warrior',level='25',
attack='30',health='30',lv_type='',lv_active_level='40',special_effect='')

card_01_96 = Monster(set_number='01',card_number='96',card_type='monster',job='warrior',level='78',
attack='50',health='80',lv_type='',lv_active_level='70',special_effect='')


#-----------------------Set 2--------------------------------------------
card_02_01 = Monster(set_number='02',card_number='01',card_type='monster',job='bowman',level='20',
attack='30',health='20',lv_type='snare',lv_active_level='40',special_effect='')

card_02_02 = Monster(set_number='02',card_number='02',card_type='monster',job='bowman',level='20',
attack='20',health='20',lv_type='spawn-30',lv_active_level='30',special_effect='')

card_02_03 = Monster(set_number='02',card_number='03',card_type='monster',job='bowman',level='30',
attack='30',health='10',lv_type='',lv_active_level='20',special_effect='')

card_02_05 = Monster(set_number='02',card_number='05',card_type='monster',job='bowman',level='68',
attack='50',health='50',lv_type='',lv_active_level='60',special_effect='')

card_02_07 = Character(set_number='02',card_number='07',card_type='character',job='bowman',level='0',
health='210',skill_1_lv = '20', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_02_15 = Monster(set_number='02',card_number='15',card_type='monster',job='bowman',level='95',
attack='70',health='70',lv_type='',lv_active_level='80',special_effect='')

card_02_20 = Monster(set_number='02',card_number='20',card_type='monster',job='magician',level='90',
attack='80',health='100',lv_type='',lv_active_level='70',special_effect='')

card_02_23 = Character(set_number='02',card_number='23',card_type='character',job='magician',level='0',
health='170',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_02_25 = Monster(set_number='02',card_number='25',card_type='monster',job='magician',level='19',
attack='10',health='40',lv_type='spawn-140',lv_active_level='90',special_effect='')

card_02_29 = Monster(set_number='02',card_number='29',card_type='monster',job='magician',level='12',
attack='20',health='20',lv_type='think fast-90',lv_active_level='70',special_effect='')

card_02_33 = Monster(set_number='02',card_number='33',card_type='monster',job='thief',level='66',
attack='50',health='40',lv_type='',lv_active_level='one-time',special_effect='')

card_02_34 = Character(set_number='02',card_number='34',card_type='character',job='thief',level='0',
health='200',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_02_46 = Character(set_number='02',card_number='46',card_type='character',job='warrior',level='0',
health='220',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_02_47 = Monster(set_number='02',card_number='47',card_type='monster',job='warrior',level='12',
attack='10',health='30',lv_type='spawn-60',lv_active_level='50',special_effect='')

card_02_48 = Monster(set_number='02',card_number='48',card_type='monster',job='warrior',level='82',
attack='50',health='70',lv_type='',lv_active_level='70',special_effect='')

card_02_49 = Monster(set_number='02',card_number='49',card_type='monster',job='warrior',level='23',
attack='10',health='20',lv_type='',lv_active_level='20',special_effect='')

card_02_52 = Monster(set_number='02',card_number='52',card_type='monster',job='warrior',level='35',
attack='10',health='50',lv_type='',lv_active_level='50',special_effect='')

card_02_60 = Monster(set_number='02',card_number='60',card_type='monster',job='warrior',level='70',
attack='40',health='70',lv_type='',lv_active_level='70',special_effect='')


#-----------------------Set 3--------------------------------------------
card_03_03 = Monster(set_number='03',card_number='03',card_type='monster',job='bowman',level='31',
attack='20',health='40',lv_type='',lv_active_level='20',special_effect='')

card_03_05 = Monster(set_number='03',card_number='05',card_type='monster',job='bowman',level='25',
attack='10',health='20',lv_type='',lv_active_level='50',special_effect='')

card_03_07 = Monster(set_number='03',card_number='07',card_type='monster',job='bowman',level='120',
attack='100',health='100',lv_type='',lv_active_level='70',special_effect='')

card_03_08 = Monster(set_number='03',card_number='08',card_type='monster',job='bowman',level='65',
attack='50',health='40',lv_type='',lv_active_level='one-time',special_effect='')

card_03_11 = Character(set_number='03',card_number='11',card_type='character',job='bowman',level='0',
health='190',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '20', skill_3_type = '')

card_03_16 = Monster(set_number='03',card_number='16',card_type='monster',job='magician',level='120',
attack='50',health='100',lv_type='',lv_active_level='70',special_effect='')

card_03_17 = Monster(set_number='03',card_number='17',card_type='monster',job='magician',level='30',
attack='20',health='30',lv_type='',lv_active_level='80',special_effect='')

card_03_22 = Character(set_number='03',card_number='22',card_type='character',job='magician',level='0',
health='180',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '60', skill_2_type = '',skill_3_lv = 'N/A', skill_3_type = '')

card_03_35 = Monster(set_number='03',card_number='35',card_type='monster',job='thief',level='70',
attack='70',health='40',lv_type='',lv_active_level='70',special_effect='')

card_03_39 = Character(set_number='03',card_number='39',card_type='character',job='thief',level='0',
health='200',skill_1_lv = '20', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_03_40 = Monster(set_number='03',card_number='40',card_type='monster',job='thief',level='68',
attack='60',health='50',lv_type='',lv_active_level='60',special_effect='')

card_03_43 = Monster(set_number='03',card_number='43',card_type='monster',job='thief',level='22',
attack='0',health='10',lv_type='',lv_active_level='40',special_effect='')

card_03_44 = Monster(set_number='03',card_number='44',card_type='monster',job='thief',level='94',
attack='80',health='90',lv_type='',lv_active_level='one-time',special_effect='')

card_03_45 = Monster(set_number='03',card_number='45',card_type='monster',job='thief',level='24',
attack='40',health='10',lv_type='',lv_active_level='50',special_effect='')

card_03_46 = Monster(set_number='03',card_number='46',card_type='monster',job='warrior',level='90',
attack='60',health='80',lv_type='',lv_active_level='70',special_effect='')

card_03_48 = Monster(set_number='03',card_number='48',card_type='monster',job='warrior',level='72',
attack='50',health='60',lv_type='',lv_active_level='20',special_effect='')

card_03_49 = Monster(set_number='03',card_number='49',card_type='monster',job='warrior',level='35',
attack='20',health='30',lv_type='',lv_active_level='one-time',special_effect='')

card_03_51 = Monster(set_number='03',card_number='51',card_type='monster',job='warrior',level='100',
attack='70',health='100',lv_type='',lv_active_level='one-time',special_effect='')

card_03_53 = Character(set_number='03',card_number='53',card_type='character',job='warrior',level='0',
health='240',skill_1_lv = '20', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_03_56 = Monster(set_number='03',card_number='56',card_type='monster',job='warrior',level='7',
attack='10',health='20',lv_type='spawn-80',lv_active_level='60',special_effect='')


#-----------------------Set 4--------------------------------------------
card_04_06 = Monster(set_number='04',card_number='06',card_type='monster',job='bowman',level='25',
attack='30',health='30',lv_type='',lv_active_level='40',special_effect='')

card_04_08 = Monster(set_number='04',card_number='08',card_type='monster',job='bowman',level='5',
attack='10',health='20',lv_type='spawn-30',lv_active_level='20',special_effect='NPC-QUEST')

card_04_15 = Character(set_number='04',card_number='15',card_type='character',job='bowman',level='0',
health='210',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_04_16 = Character(set_number='04',card_number='16',card_type='character',job='magician',level='0',
health='190',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '10', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_04_18 = Monster(set_number='04',card_number='18',card_type='monster',job='magician',level='70',
attack='60',health='60',lv_type='',lv_active_level='one-time',special_effect='')

card_04_20 = Monster(set_number='04',card_number='20',card_type='monster',job='magician',level='20',
attack='20',health='20',lv_type='spawn-30',lv_active_level='30',special_effect='')

card_04_24 = Monster(set_number='04',card_number='24',card_type='monster',job='magician',level='30',
attack='30',health='20',lv_type='',lv_active_level='80',special_effect='')

card_04_27 = Monster(set_number='04',card_number='27',card_type='monster',job='magician',level='10',
attack='10',health='20',lv_type='buff a friend',lv_active_level='10',special_effect='')

card_04_29 = Monster(set_number='04',card_number='29',card_type='monster',job='magician',level='29',
attack='30',health='40',lv_type='',lv_active_level='50',special_effect='')

card_04_31 = Monster(set_number='04',card_number='31',card_type='monster',job='thief',level='92',
attack='120',health='120',lv_type='',lv_active_level='one-time',special_effect='')

card_04_32 = Monster(set_number='04',card_number='32',card_type='monster',job='thief',level='27',
attack='30',health='20',lv_type='',lv_active_level='80',special_effect='')

card_04_34 = Monster(set_number='04',card_number='34',card_type='monster',job='thief',level='10',
attack='20',health='10',lv_type='spawn-20',lv_active_level='20',special_effect='')

card_04_37 = Monster(set_number='04',card_number='37',card_type='monster',job='thief',level='85',
attack='80',health='80',lv_type='',lv_active_level='50',special_effect='')

card_04_40 = Character(set_number='04',card_number='40',card_type='character',job='thief',level='0',
health='200',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_04_49 = Monster(set_number='04',card_number='49',card_type='monster',job='warrior',level='35',
attack='30',health='30',lv_type='',lv_active_level='80',special_effect='')

card_04_52 = Monster(set_number='04',card_number='52',card_type='monster',job='warrior',level='95',
attack='80',health='80',lv_type='',lv_active_level='one-time',special_effect='')

card_04_55 = Monster(set_number='04',card_number='55',card_type='monster',job='warrior',level='19',
attack='10',health='10',lv_type='stick together',lv_active_level='50',special_effect='')

card_04_56 = Monster(set_number='04',card_number='56',card_type='monster',job='warrior',level='75',
attack='70',health='50',lv_type='',lv_active_level='one-time',special_effect='')

card_04_58 = Character(set_number='04',card_number='58',card_type='character',job='warrior',level='0',
health='240',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '30', skill_3_type = '')

card_04_59 = Monster(set_number='04',card_number='59',card_type='monster',job='warrior',level='62',
attack='60',health='70',lv_type='',lv_active_level='30',special_effect='')

card_04_60 = Monster(set_number='04',card_number='60',card_type='monster',job='warrior',level='23',
attack='20',health='30',lv_type='',lv_active_level='one-time',special_effect='')


#-----------------------Set 5--------------------------------------------
card_05_03 = Monster(set_number='05',card_number='03',card_type='monster',job='bowman',level='72',
attack='70',health='70',lv_type='',lv_active_level='80',special_effect='')

card_05_06 = Character(set_number='05',card_number='06',card_type='character',job='bowman',level='0',
health='190',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '30', skill_3_type = '')

card_05_09 = Monster(set_number='05',card_number='09',card_type='monster',job='bowman',level='99',
attack='80',health='80',lv_type='',lv_active_level='one-time',special_effect='')

card_05_10 = Monster(set_number='05',card_number='10',card_type='monster',job='bowman',level='35',
attack='30',health='30',lv_type='',lv_active_level='one-time',special_effect='')

card_05_11 = Monster(set_number='05',card_number='11',card_type='monster',job='bowman',level='30',
attack='20',health='40',lv_type='',lv_active_level='40',special_effect='')

card_05_12 = Monster(set_number='05',card_number='12',card_type='monster',job='bowman',level='30',
attack='30',health='20',lv_type='',lv_active_level='60',special_effect='')

card_05_23 = Monster(set_number='05',card_number='23',card_type='monster',job='magician',level='22',
attack='10',health='40',lv_type='',lv_active_level='40',special_effect='')

card_05_25 = Monster(set_number='05',card_number='25',card_type='monster',job='magician',level='22',
attack='30',health='90',lv_type='',lv_active_level='one-time',special_effect='')

card_05_30 = Character(set_number='05',card_number='30',card_type='character',job='magician',level='0',
health='190',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '80', skill_3_type = '')

card_05_32 = Monster(set_number='05',card_number='32',card_type='monster',job='magician',level='62',
attack='60',health='60',lv_type='',lv_active_level='80',special_effect='')

card_05_43 = Monster(set_number='05',card_number='43',card_type='monster',job='thief',level='29',
attack='20',health='30',lv_type='',lv_active_level='50',special_effect='')

card_05_45 = Character(set_number='05',card_number='45',card_type='character',job='thief',level='0',
health='200',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_05_48 = Monster(set_number='05',card_number='48',card_type='monster',job='thief',level='89',
attack='80',health='90',lv_type='',lv_active_level='60',special_effect='')

card_05_51 = Monster(set_number='05',card_number='51',card_type='monster',job='thief',level='30',
attack='30',health='20',lv_type='',lv_active_level='one-time',special_effect='')

card_05_52 = Monster(set_number='05',card_number='52',card_type='monster',job='thief',level='8',
attack='30',health='30',lv_type='spy',lv_active_level='one-time',special_effect='')

card_05_53 = Monster(set_number='05',card_number='53',card_type='monster',job='thief',level='23',
attack='30',health='10',lv_type='',lv_active_level='30',special_effect='')

card_05_56 = Monster(set_number='05',card_number='56',card_type='monster',job='warrior',level='88',
attack='80',health='80',lv_type='',lv_active_level='70',special_effect='')

card_05_57 = Monster(set_number='05',card_number='57',card_type='monster',job='warrior',level='32',
attack='20',health='30',lv_type='',lv_active_level='30',special_effect='')

card_05_61 = Character(set_number='05',card_number='61',card_type='character',job='warrior',level='0',
health='280',skill_1_lv = '20', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_05_65 = Monster(set_number='05',card_number='65',card_type='monster',job='warrior',level='30',
attack='20',health='20',lv_type='',lv_active_level='60',special_effect='')

card_05_68 = Monster(set_number='05',card_number='68',card_type='monster',job='warrior',level='33',
attack='30',health='30',lv_type='',lv_active_level='50',special_effect='')

card_05_76 = Monster(set_number='05',card_number='76',card_type='monster',job='jobless',level='65',
attack='70',health='30',lv_type='',lv_active_level='one-time',special_effect='')

card_05_77 = Monster(set_number='05',card_number='77',card_type='monster',job='jobless',level='2',
attack='10',health='20',lv_type='bash-10',lv_active_level='10',special_effect='N/A')

card_05_78 = Monster(set_number='05',card_number='78',card_type='monster',job='jobless',level='35',
attack='30',health='40',lv_type='',lv_active_level='30',special_effect='')

card_05_81 = Monster(set_number='05',card_number='81',card_type='monster',job='jobless',level='80',
attack='50',health='80',lv_type='',lv_active_level='60',special_effect='')

card_05_85 = Monster(set_number='05',card_number='85',card_type='monster',job='jobless',level='70',
attack='40',health='60',lv_type='',lv_active_level='50',special_effect='')

card_05_86 = Monster(set_number='05',card_number='86',card_type='monster',job='jobless',level='67',
attack='60',health='70',lv_type='',lv_active_level='40',special_effect='')

card_05_87 = Monster(set_number='05',card_number='87',card_type='monster',job='jobless',level='80',
attack='80',health='50',lv_type='',lv_active_level='60',special_effect='')

card_05_90 = Character(set_number='05',card_number='90',card_type='character',job='jobless',level='0',
health='180',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '30', skill_3_type = '')






#--
