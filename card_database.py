import sys
import pygame
from card import Character, Monster, Tactic, Item

#-----------------------Set 1--------------------------------------------
#monster lv_type list: spawn, equip, think fast, easy shot, quest, stab, slash,refresh, sneak, crush
#tactic lv_type list: Dmg, Heal, Quest

card_01_01 = Tactic(name = 'ARROW BLOW',set_number='01',card_number='01',card_type='tactic',job='bowman',level='10',
lv_type='Spawn/Think Fast 40',lv_active_level='50',special_effect='Dmg 30')

card_01_03 = Item(name = 'BLACK ROBIN HAT',set_number='01',card_number='03',card_type='item',job='bowman',level='20',
lv_type='Tricky Shot',lv_active_level='60',special_effect='')

card_01_04 = Item(name = 'BLUE DIROS',set_number='01',card_number='04',card_type='item',job='bowman',level='20',
lv_type='Equip 30',lv_active_level='30',special_effect='')

card_01_05 = Monster(name = '',set_number='01',card_number='05',card_type='monster',job='bowman',level='72',
attack='70',health='70',lv_type='Spawn/Equip 120',lv_active_level='80',special_effect='')

card_01_06 = Monster(name = 'CURSE EYE',set_number='01',card_number='06',card_type='monster',job='bowman',level='35',
attack='30',health='40',lv_type='Spawn/Think Fast 40',lv_active_level='50',special_effect='')

card_01_08 = Monster(name = '',set_number='01',card_number='08',card_type='monster',job='bowman',level='30',
attack='30',health='20',lv_type='Spawn 30',lv_active_level='30',special_effect='')

card_01_11 = Monster(name = '',set_number='01',card_number='11',card_type='monster',job='bowman',level='28',
attack='20',health='20',lv_type='Easy Shot',lv_active_level='20',special_effect='')

card_01_13 = Monster(name = 'HORNED MUSHROOM',set_number='01',card_number='13',card_type='monster',job='bowman',level='22',
attack='20',health='40',lv_type='Spawn/Equip 30',lv_active_level='40',special_effect='')

card_01_14 = Monster(name = '',set_number='01',card_number='14',card_type='monster',job='bowman',level='35',
attack='30',health='30',lv_type='lalalala',lv_active_level='0',special_effect='')

card_01_16 = Character(name = 'NIXIE',set_number='01',card_number='16',card_type='character',job='bowman',level='0',
health='200',skill_1_lv = '10', skill_1_type = 'Easy Shot',skill_2_lv = '20', skill_2_type = 'Quest',skill_3_lv = '50', skill_3_type = 'Tricky Shot')

card_01_21 = Character(name = 'SKYHAWK', set_number='01',card_number='21',card_type='character',job='bowman',level='0',
health='210',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '10', skill_2_type = '',skill_3_lv = '60', skill_3_type = '')

card_01_23 = Monster(name = 'STIRGE',set_number='01',card_number='23',card_type='monster',job='bowman',level='20',
attack='30',health='20',lv_type='Spawn/Equip 50',lv_active_level='60',special_effect='')

card_01_25 = Monster(name = 'BELLFLOWER ROOT',set_number='01',card_number='25',card_type='monster',job='magician',level='53',
attack='40',health='60',lv_type='Think Fast/Equip 50',lv_active_level='50',special_effect='')

card_01_27 = Monster(name = 'DARK AXE STUMP',set_number='01',card_number='27',card_type='monster',job='magician',level='22',
attack='10',health='40',lv_type='Spawn 40',lv_active_level='40',special_effect='')

card_01_28 = Tactic(name = 'ENERGY BOLT',set_number='01',card_number='28',card_type='tactic',job='magician',level='40',
lv_type='Spawn/Think Fast 70',lv_active_level='60',special_effect='Dmg 80')

card_01_29 = Item(name = 'EVIL TALE',set_number='01',card_number='29',card_type='item',job='magician',level='58',
lv_type='Think Fast/Equip 70',lv_active_level='60',special_effect='')

card_01_31 = Monster(name = 'JR. NECKI',set_number='01',card_number='31',card_type='monster',job='magician',level='21',
attack='30',health='30',lv_type='Spawn 30',lv_active_level='30',special_effect='')

card_01_33 = Monster(name = 'LIONER',set_number='01',card_number='33',card_type='monster',job='magician',level='53',
attack='50',health='50',lv_type='Spawn/Think Fast 90',lv_active_level='70',special_effect='')

card_01_34 = Monster(name = '',set_number='01',card_number='34',card_type='monster',job='magician',level='73',
attack='60',health='90',lv_type='lalalala',lv_active_level='0',special_effect='')

card_01_36 = Item(name = 'MAPLE STAFF',set_number='01',card_number='36',card_type='item',job='magician',level='35',
lv_type='Think Fast 40',lv_active_level='30',special_effect='')

card_01_37 = Character(name = 'MAYA',set_number='01',card_number='37',card_type='character',job='magician',level='0',
health='190',skill_1_lv = '10', skill_1_type = 'Quest',skill_2_lv = '20', skill_2_type = 'Fire Arrow',skill_3_lv = '30', skill_3_type = 'Think Fast X')

card_01_40 = Monster(name = '',set_number='01',card_number='40',card_type='monster',job='magician',level='12',
attack='10',health='10',lv_type='Quest',lv_active_level='0',special_effect='')

card_01_42 = Item(name = 'RED APPRENTICE HAT',set_number='01',card_number='42',card_type='item',job='magician',level='10',
lv_type='Equip 40',lv_active_level='40',special_effect='')

card_01_43 = Tactic(name = 'SIDE QUEST',set_number='01',card_number='43',card_type='tactic',job='magician',level='40',
lv_type='Think Fast 40',lv_active_level='30',special_effect='Quest/Quest')

card_01_44 = Character(name = 'STORMWIND',set_number='01',card_number='44',card_type='character',job='magician',level='0',
health='180',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '70', skill_3_type = '')

card_01_50 = Item(name = 'BLOOD SLAIN',set_number='01',card_number='50',card_type='item',job='thief',level='50',
lv_type='Sneak X',lv_active_level='70',special_effect='')

card_01_53 = Monster(name = '',set_number='01',card_number='53',card_type='monster',job='thief',level='25',
attack='30',health='20',lv_type='Spawn/Equip 30',lv_active_level='40',special_effect='')

card_01_55 = Monster(name = 'CROCO',set_number='01',card_number='55',card_type='monster',job='thief',level='52',
attack='70',health='40',lv_type='Equip X',lv_active_level='30',special_effect='')

card_01_56 = Item(name = 'DARK SHADOW',set_number='01',card_number='56',card_type='item',job='thief',level='40',
lv_type='Spawn/Equip 70',lv_active_level='60',special_effect='')

card_01_58 = Item(name = 'EMERALD EARRINGS',set_number='01',card_number='58',card_type='item',job='thief',level='30',
lv_type='Sneak 70',lv_active_level='70',special_effect='')

card_01_59 = Character(name = 'IVAN',set_number='01',card_number='59',card_type='character',job='thief',level='0',
health='220',skill_1_lv = '10', skill_1_type = 'Stab',skill_2_lv = '10', skill_2_type = 'Quest',skill_3_lv = '20', skill_3_type = 'Equip X')

card_01_60 = Monster(name = '',set_number='01',card_number='60',card_type='monster',job='thief',level='24',
attack='60',health='30',lv_type='Stab',lv_active_level='30',special_effect='')

card_01_61 = Monster(name = 'KRIP',set_number='01',card_number='61',card_type='monster',job='thief',level='30',
attack='30',health='20',lv_type='Slash',lv_active_level='70',special_effect='')

card_01_62 = Item(name = 'KUMBI THROWING-STAR',set_number='01',card_number='62',card_type='item',job='thief',level='30',
lv_type='Equip 20',lv_active_level='10',special_effect='')

card_01_64 = Character(name = 'MISTMOON',set_number='01',card_number='64',card_type='character',job='thief',level='0',
health='200',skill_1_lv = '10', skill_1_type = 'Stab',skill_2_lv = '20', skill_2_type = 'Quest',skill_3_lv = '40', skill_3_type = 'Sneak 40')

card_01_65 = Monster(name = '',set_number='01',card_number='65',card_type='monster',job='thief',level='8',
attack='30',health='10',lv_type='Equip 40',lv_active_level='30',special_effect='')

card_01_66 = Monster(name = '',set_number='01',card_number='66',card_type='monster',job='thief',level='32',
attack='30',health='30',lv_type='lalalala',lv_active_level='0',special_effect='')

card_01_69 = Monster(name = '',set_number='01',card_number='69',card_type='monster',job='thief',level='4',
attack='10',health='20',lv_type='Spawn 90',lv_active_level='70',special_effect='tough')

card_01_70 = Monster(name = '',set_number='01',card_number='70',card_type='monster',job='thief',level='23',
attack='20',health='20',lv_type='Spawn/Think Fast 30',lv_active_level='30',special_effect='')

card_01_71 = Monster(name = '',set_number='01',card_number='71',card_type='monster',job='thief',level='63',
attack='50',health='40',lv_type='lalalala',lv_active_level='0',special_effect='')

card_01_73 = Item(name = 'BATTLE SHIELD',set_number='01',card_number='73',card_type='item',job='warrior',level='35',
lv_type='Think Fast/Equip 40',lv_active_level='50',special_effect='')

card_01_76 = Monster(name = '',set_number='01',card_number='76',card_type='monster',job='warrior',level='32',
attack='10',health='50',lv_type='Spawn 40',lv_active_level='30',special_effect='')

card_01_77 = Monster(name = 'GREEN MUSHROOM',set_number='01',card_number='77',card_type='monster',job='warrior',level='15',
attack='10',health='40',lv_type='Spawn/Equip 90',lv_active_level='70',special_effect='')

card_01_78 = Monster(name = 'GRIZZLY',set_number='01',card_number='78',card_type='monster',job='warrior',level='56',
attack='50',health='60',lv_type='Spawn X',lv_active_level='50',special_effect='')

card_01_81 = Monster(name = '',set_number='01',card_number='81',card_type='monster',job='warrior',level='63',
attack='50',health='60',lv_type='lalalala',lv_active_level='50',special_effect='')

card_01_85 = Tactic(name = 'RESTING',set_number='01',card_number='85',card_type='tactic',job='warrior',level='10',
lv_type='Spawn/Think Fast 90',lv_active_level='70',special_effect='Heal 20/Quest')

card_01_86 = Monster(name = 'RIBBON PIG',set_number='01',card_number='86',card_type='monster',job='warrior',level='10',
attack='20',health='20',lv_type='Spawn 20',lv_active_level='10',special_effect='')

card_01_87 = Monster(name = '',set_number='01',card_number='87',card_type='monster',job='warrior',level='30',
attack='20',health='30',lv_type='lalalala',lv_active_level='0',special_effect='')

card_01_88 = Item(name = "SERPENT'S TONGUE",set_number='01',card_number='88',card_type='item',job='warrior',level='50',
lv_type='Crush',lv_active_level='50',special_effect='')

card_01_89 = Character(name = 'SHERMAN',set_number='01',card_number='89',card_type='character',job='warrior',level='0',
health='240',skill_1_lv = '10', skill_1_type = 'Bash',skill_2_lv = '20', skill_2_type = 'Quest',skill_3_lv = '30', skill_3_type = 'Spawn X')

card_01_90 = Monster(name = '',set_number='01',card_number='90',card_type='monster',job='warrior',level='6',
attack='10',health='10',lv_type='refresh',lv_active_level='40',special_effect='')

card_01_91 = Character(name = 'STARBLADE',set_number='01',card_number='91',card_type='character',job='warrior',level='0',
health='260',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_01_93 = Monster(name = '',set_number='01',card_number='93',card_type='monster',job='warrior',level='70',
attack='50',health='40',lv_type='lalalala',lv_active_level='0',special_effect='')

card_01_94 = Item(name = 'THE NINE DRAGONS',set_number='01',card_number='94',card_type='item',job='warrior',level='50',
lv_type='Equip 30',lv_active_level='30',special_effect='')

card_01_95 = Monster(name = 'WILD BOAR',set_number='01',card_number='95',card_type='monster',job='warrior',level='25',
attack='30',health='30',lv_type='Think Fast/Equip 30',lv_active_level='40',special_effect='')

card_01_96 = Monster(name = '',set_number='01',card_number='96',card_type='monster',job='warrior',level='78',
attack='50',health='80',lv_type='Spawn/Equip 100',lv_active_level='70',special_effect='')


#-----------------------Set 2--------------------------------------------
card_02_01 = Monster(name = '',set_number='02',card_number='01',card_type='monster',job='bowman',level='20',
attack='30',health='20',lv_type='snare',lv_active_level='40',special_effect='')

card_02_02 = Monster(name = '',set_number='02',card_number='02',card_type='monster',job='bowman',level='20',
attack='20',health='20',lv_type='Spawn 30',lv_active_level='30',special_effect='')

card_02_03 = Monster(name = '',set_number='02',card_number='03',card_type='monster',job='bowman',level='30',
attack='30',health='10',lv_type='lalalala',lv_active_level='20',special_effect='')

card_02_05 = Monster(name = '',set_number='02',card_number='05',card_type='monster',job='bowman',level='68',
attack='50',health='50',lv_type='lalalala',lv_active_level='60',special_effect='')

card_02_07 = Character(name = 'INDIGO',set_number='02',card_number='07',card_type='character',job='bowman',level='0',
health='210',skill_1_lv = '20', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_02_11 = Item(name = 'MAPLE SOUL SEARCHER',set_number='02',card_number='11',card_type='item',job='bowman',level='45',
lv_type='Think Fast/Equip 40',lv_active_level='45',special_effect='')

card_02_15 = Monster(name = '',set_number='02',card_number='15',card_type='monster',job='bowman',level='95',
attack='70',health='70',lv_type='lalalala',lv_active_level='80',special_effect='')

card_02_18 = Tactic(name = "BEGINNER'S BOLT",set_number='02',card_number='18',card_type='tactic',job='magician',level='20',
lv_type='Spawn/Equip 30',lv_active_level='30',special_effect='Dmg 60')

card_02_19 = Item(name = 'BLACK MAGIC SHOES',set_number='02',card_number='19',card_type='item',job='magician',level='30',
lv_type='Spawn/Equip 70',lv_active_level='60',special_effect='')

card_02_20 = Monster(name = 'BLUE DRAGON TURTLE',set_number='02',card_number='20',card_type='monster',job='magician',level='90',
attack='80',health='100',lv_type='Spawn 90',lv_active_level='70',special_effect='')

card_02_23 = Character(name = 'FELIX',set_number='02',card_number='23',card_type='character',job='magician',level='0',
health='170',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_02_24 = Tactic(name = '',set_number='02',card_number='24',card_type='tactic',job='magician',level='60',
lv_type='Spawn/Think Fast 50',lv_active_level='50',special_effect='Dmg 50/Quest')

card_02_25 = Monster(name = 'GHOST STUMP',set_number='02',card_number='25',card_type='monster',job='magician',level='19',
attack='10',health='40',lv_type='Spawn 140',lv_active_level='90',special_effect='')

card_02_29 = Monster(name = '',set_number='02',card_number='29',card_type='monster',job='magician',level='12',
attack='20',health='20',lv_type='think fast 90',lv_active_level='70',special_effect='')

card_02_30 = Item(name = 'WIZARD WAND',set_number='02',card_number='30',card_type='item',job='magician',level='40',
lv_type='Think Fast 40',lv_active_level='30',special_effect='')

card_02_31 = Monster(name = 'BOOK GHOST',set_number='02',card_number='31',card_type='monster',job='thief',level='55',
attack='60',health='40',lv_type='Spawn/Think Fast 50',lv_active_level='50',special_effect='')

card_02_33 = Monster(name = '',set_number='02',card_number='33',card_type='monster',job='thief',level='66',
attack='50',health='40',lv_type='lalalala',lv_active_level='0',special_effect='')

card_02_34 = Character(name = 'NOVA',set_number='02',card_number='34',card_type='character',job='thief',level='0',
health='200',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_02_35 = Item(name = 'OMOK TABLE',set_number='02',card_number='35',card_type='item',job='thief',level='30',
lv_type='Think Fast/Equip 80',lv_active_level='70',special_effect='')

card_02_38 = Item(name = 'POISONOUS MUSHROOM',set_number='02',card_number='38',card_type='item',job='thief',level='30',
lv_type='Spawn/Equip 30',lv_active_level='30',special_effect='')

card_02_46 = Character(name = 'BRUNO',set_number='02',card_number='46',card_type='character',job='warrior',level='0',
health='220',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_02_47 = Monster(name = '',set_number='02',card_number='47',card_type='monster',job='warrior',level='12',
attack='10',health='30',lv_type='Spawn 60',lv_active_level='50',special_effect='')

card_02_48 = Monster(name = '',set_number='02',card_number='48',card_type='monster',job='warrior',level='82',
attack='50',health='70',lv_type='lalalala',lv_active_level='70',special_effect='')

card_02_49 = Monster(name = '',set_number='02',card_number='49',card_type='monster',job='warrior',level='23',
attack='10',health='20',lv_type='lalalala',lv_active_level='20',special_effect='')

card_02_52 = Monster(name = '',set_number='02',card_number='52',card_type='monster',job='warrior',level='35',
attack='10',health='50',lv_type='lalalala',lv_active_level='50',special_effect='')

card_02_60 = Monster(name = '',set_number='02',card_number='60',card_type='monster',job='warrior',level='70',
attack='40',health='70',lv_type='lalalala',lv_active_level='70',special_effect='')


#-----------------------Set 3--------------------------------------------
card_03_01 = Item(name = 'BLACK BUNNY',set_number='03',card_number='01',card_type='item',job='bowman',level='10',
lv_type='Easy Shot',lv_active_level='20',special_effect='')

card_03_02 = Tactic(name = '',set_number='03',card_number='02',card_type='tactic',job='bowman',level='10',
lv_type='lalalala',lv_active_level='one-time',special_effect='Dmg 40')

card_03_03 = Monster(name = '',set_number='03',card_number='03',card_type='monster',job='bowman',level='31',
attack='20',health='40',lv_type='lalalala',lv_active_level='20',special_effect='')

card_03_05 = Monster(name = '',set_number='03',card_number='05',card_type='monster',job='bowman',level='25',
attack='10',health='20',lv_type='lalalala',lv_active_level='50',special_effect='')

card_03_07 = Monster(name = '',set_number='03',card_number='07',card_type='monster',job='bowman',level='120',
attack='100',health='100',lv_type='lalalala',lv_active_level='70',special_effect='')

card_03_08 = Monster(name = '',set_number='03',card_number='08',card_type='monster',job='bowman',level='65',
attack='50',health='40',lv_type='lalalala',lv_active_level='0',special_effect='')

card_03_09 = Monster(name = 'GINSENG JAR',set_number='03',card_number='09',card_type='monster',job='bowman',level='48',
attack='40',health='40',lv_type='Tricky Shot',lv_active_level='60',special_effect='')

card_03_10 = Item(name = 'MAPLE SHIELD',set_number='03',card_number='10',card_type='item',job='bowman',level='20',
lv_type='Spawn 50',lv_active_level='50',special_effect='')

card_03_11 = Character(name = 'MOBY',set_number='03',card_number='11',card_type='character',job='bowman',level='0',
health='190',skill_1_lv = '10', skill_1_type = 'Easy Shot',skill_2_lv = '20', skill_2_type = 'Quest',skill_3_lv = '20', skill_3_type = 'Spawn 30')

card_03_16 = Monster(name = '',set_number='03',card_number='16',card_type='monster',job='magician',level='120',
attack='50',health='100',lv_type='lalalala',lv_active_level='70',special_effect='')

card_03_17 = Monster(name = '',set_number='03',card_number='17',card_type='monster',job='magician',level='30',
attack='20',health='30',lv_type='lalalala',lv_active_level='80',special_effect='')

card_03_22 = Character(name = 'PENELOPE',set_number='03',card_number='22',card_type='character',job='magician',level='0',
health='180',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '60', skill_2_type = '',skill_3_lv = 'N/A', skill_3_type = '')

card_03_25 = Tactic(name = 'ROOKIE ENERGY BOLT',set_number='03',card_number='25',card_type='tactic',job='magician',level='30',
lv_type='Think Fast X',lv_active_level='40',special_effect='Dmg 70')

card_03_29 = Monster(name = 'SR. BELLFLOWER ROOT',set_number='03',card_number='29',card_type='monster',job='magician',level='54',
attack='50',health='50',lv_type='Spawn 60',lv_active_level='60',special_effect='')

card_03_35 = Monster(name = '',set_number='03',card_number='35',card_type='monster',job='thief',level='70',
attack='70',health='40',lv_type='lalalala',lv_active_level='70',special_effect='')

card_03_38 = Item(name = 'HALFMOON ZAMADAR',set_number='03',card_number='38',card_type='item',job='thief',level='32',
lv_type='Stab',lv_active_level='20',special_effect='')

card_03_39 = Character(name = 'KEATON',set_number='03',card_number='39',card_type='character',job='thief',level='0',
health='200',skill_1_lv = '20', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_03_40 = Monster(name = '',set_number='03',card_number='40',card_type='monster',job='thief',level='68',
attack='60',health='50',lv_type='lalalala',lv_active_level='60',special_effect='')

card_03_43 = Monster(name = '',set_number='03',card_number='43',card_type='monster',job='thief',level='22',
attack='0',health='10',lv_type='lalalala',lv_active_level='40',special_effect='')

card_03_44 = Monster(name = '',set_number='03',card_number='44',card_type='monster',job='thief',level='94',
attack='80',health='90',lv_type='lalalala',lv_active_level='0',special_effect='')

card_03_45 = Monster(name = 'ZOMBIE MUSHROOM',set_number='03',card_number='45',card_type='monster',job='thief',level='24',
attack='40',health='10',lv_type='Spawn/Think Fast 40',lv_active_level='50',special_effect='')

card_03_46 = Monster(name = '',set_number='03',card_number='46',card_type='monster',job='warrior',level='90',
attack='60',health='80',lv_type='lalalala',lv_active_level='70',special_effect='')

card_03_48 = Monster(name = '',set_number='03',card_number='48',card_type='monster',job='warrior',level='72',
attack='50',health='60',lv_type='lalalala',lv_active_level='20',special_effect='')

card_03_49 = Monster(name = '',set_number='03',card_number='49',card_type='monster',job='warrior',level='35',
attack='20',health='30',lv_type='lalalala',lv_active_level='0',special_effect='')

card_03_51 = Monster(name = '',set_number='03',card_number='51',card_type='monster',job='warrior',level='100',
attack='70',health='100',lv_type='lalalala',lv_active_level='0',special_effect='')

card_03_53 = Character(name = 'KIRI VIVA',set_number='03',card_number='53',card_type='character',job='warrior',level='0',
health='240',skill_1_lv = '20', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_03_56 = Monster(name = '',set_number='03',card_number='56',card_type='monster',job='warrior',level='7',
attack='10',health='20',lv_type='Spawn 80',lv_active_level='60',special_effect='')

card_03_57 = Item(name = 'PUPPY',set_number='03',card_number='57',card_type='item',job='warrior',level='10',
lv_type='Spawn 50',lv_active_level='40',special_effect='')

card_03_60 = Item(name = 'WATCH HOG',set_number='03',card_number='60',card_type='item',job='warrior',level='70',
lv_type='Spawn 70',lv_active_level='60',special_effect='')


#-----------------------Set 4--------------------------------------------
card_04_04 = Item(name = 'HEROIC PENTAGON',set_number='04',card_number='04',card_type='item',job='bowman',level='40',
lv_type='Tricky Shot',lv_active_level='60',special_effect='')

card_04_05 = Item(name = 'JR.REAPER',set_number='04',card_number='05',card_type='item',job='bowman',level='10',
lv_type='Spawn 70',lv_active_level='60',special_effect='')

card_04_06 = Monster(name = 'KILLA BEE',set_number='04',card_number='06',card_type='monster',job='bowman',level='25',
attack='30',health='30',lv_type='Spawn/Equip 30',lv_active_level='40',special_effect='')

card_04_08 = Monster(name = '',set_number='04',card_number='08',card_type='monster',job='bowman',level='5',
attack='10',health='20',lv_type='Spawn 30',lv_active_level='20',special_effect='NPC-QUEST')

card_04_10 = Item(name = 'SPIDER VENOM EARRINGS',set_number='04',card_number='10',card_type='item',job='bowman',level='15',
lv_type='Equip 50',lv_active_level='50',special_effect='')

card_04_12 = Item(name = 'WAR BOW',set_number='04',card_number='12',card_type='item',job='bowman',level='10',
lv_type='Easy Shot',lv_active_level='20',special_effect='')

card_04_15 = Character(name = 'ZOZO',set_number='04',card_number='15',card_type='character',job='bowman',level='0',
health='210',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_04_16 = Character(name = 'BRADDOCK',set_number='04',card_number='16',card_type='character',job='magician',level='0',
health='190',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '10', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_04_18 = Monster(name = '',set_number='04',card_number='18',card_type='monster',job='magician',level='70',
attack='60',health='60',lv_type='lalalala',lv_active_level='0',special_effect='')

card_04_20 = Monster(name = '',set_number='04',card_number='20',card_type='monster',job='magician',level='20',
attack='20',health='20',lv_type='Spawn 30',lv_active_level='30',special_effect='')

card_04_23 = Tactic(name = 'HOLY ARROW',set_number='04',card_number='23',card_type='tactic',job='magician',level='10',
lv_type='Think Fast 90',lv_active_level='70',special_effect='Dmg 30')

card_04_24 = Monster(name = '',set_number='04',card_number='24',card_type='monster',job='magician',level='30',
attack='30',health='20',lv_type='lalalala',lv_active_level='80',special_effect='')

card_04_26 = Item(name = 'METAL WAND',set_number='04',card_number='26',card_type='item',job='magician',level='18',
lv_type='Think Fast/Equip 40',lv_active_level='40',special_effect='')

card_04_27 = Monster(name = '',set_number='04',card_number='27',card_type='monster',job='magician',level='10',
attack='10',health='20',lv_type='buff a friend',lv_active_level='10',special_effect='')

card_04_29 = Monster(name = 'SAND DWARF',set_number='04',card_number='29',card_type='monster',job='magician',level='29',
attack='30',health='40',lv_type='Spawn/Think Fast 50',lv_active_level='50',special_effect='')

card_04_31 = Monster(name = '',set_number='04',card_number='31',card_type='monster',job='thief',level='92',
attack='120',health='120',lv_type='lalalala',lv_active_level='0',special_effect='')

card_04_32 = Monster(name = '',set_number='04',card_number='32',card_type='monster',job='thief',level='27',
attack='30',health='20',lv_type='lalalala',lv_active_level='80',special_effect='')

card_04_34 = Monster(name = '',set_number='04',card_number='34',card_type='monster',job='thief',level='10',
attack='20',health='10',lv_type='Spawn 20',lv_active_level='20',special_effect='')

card_04_37 = Monster(name = '',set_number='04',card_number='37',card_type='monster',job='thief',level='85',
attack='80',health='80',lv_type='lalalala',lv_active_level='50',special_effect='')

card_04_38 = Item(name = 'DIAMOND DAGGER',set_number='04',card_number='38',card_type='item',job='thief',level='50',
lv_type='Equip 100',lv_active_level='70',special_effect='')

card_04_40 = Character(name = 'MICHI',set_number='04',card_number='40',card_type='character',job='thief',level='0',
health='200',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '40', skill_3_type = '')

card_04_41 = Item(name = 'MITHRIL WRISTBAND',set_number='04',card_number='41',card_type='item',job='thief',level='20',
lv_type='Stab',lv_active_level='30',special_effect='')

card_04_42 = Monster(name = 'MOON BUNNY',set_number='04',card_number='42',card_type='monster',job='thief',level='45',
attack='50',health='20',lv_type='Sneak 50',lv_active_level='60',special_effect='')

card_04_44 = Item(name = 'TRIPLE-TIPPED ZAMADAR',set_number='04',card_number='44',card_type='item',job='thief',level='17',
lv_type='Spawn 40',lv_active_level='40',special_effect='')

card_04_49 = Monster(name = '',set_number='04',card_number='49',card_type='monster',job='warrior',level='35',
attack='30',health='30',lv_type='lalalala',lv_active_level='80',special_effect='')

card_04_51 = Item(name = 'RELAXER',set_number='04',card_number='51',card_type='item',job='warrior',level='10',
lv_type='Refresh',lv_active_level='40',special_effect='')

card_04_52 = Monster(name = '',set_number='04',card_number='52',card_type='monster',job='warrior',level='95',
attack='80',health='80',lv_type='lalalala',lv_active_level='0',special_effect='')

card_04_55 = Monster(name = '',set_number='04',card_number='55',card_type='monster',job='warrior',level='19',
attack='10',health='10',lv_type='stick together',lv_active_level='50',special_effect='')

card_04_56 = Monster(name = '',set_number='04',card_number='56',card_type='monster',job='warrior',level='75',
attack='70',health='50',lv_type='lalalala',lv_active_level='0',special_effect='')

card_04_58 = Character(name = 'TUCKER',set_number='04',card_number='58',card_type='character',job='warrior',level='0',
health='240',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '30', skill_3_type = '')

card_04_59 = Monster(name = 'WILD KARGO',set_number='04',card_number='59',card_type='monster',job='warrior',level='62',
attack='60',health='70',lv_type='Spawn/Equip 30',lv_active_level='30',special_effect='')

card_04_60 = Monster(name = '',set_number='04',card_number='60',card_type='monster',job='warrior',level='23',
attack='20',health='30',lv_type='lalalala',lv_active_level='0',special_effect='')


#-----------------------Set 5--------------------------------------------
card_05_02 = Item(name = 'BROWN WOODSMAN BOOTS',set_number='05',card_number='02',card_type='item',job='bowman',level='15',
lv_type='Think Fast/Equip 20',lv_active_level='20',special_effect='')

card_05_03 = Monster(name = '',set_number='05',card_number='03',card_type='monster',job='bowman',level='72',
attack='70',health='70',lv_type='lalalala',lv_active_level='80',special_effect='')

card_05_06 = Character(name = 'FLYNN',set_number='05',card_number='06',card_type='character',job='bowman',level='0',
health='190',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '30', skill_3_type = '')

card_05_09 = Monster(name = '',set_number='05',card_number='09',card_type='monster',job='bowman',level='99',
attack='80',health='80',lv_type='lalalala',lv_active_level='0',special_effect='')

card_05_10 = Monster(name = '',set_number='05',card_number='10',card_type='monster',job='bowman',level='35',
attack='30',health='30',lv_type='lalalala',lv_active_level='0',special_effect='')

card_05_11 = Monster(name = '',set_number='05',card_number='11',card_type='monster',job='bowman',level='30',
attack='20',health='40',lv_type='lalalala',lv_active_level='40',special_effect='')

card_05_12 = Monster(name = '',set_number='05',card_number='12',card_type='monster',job='bowman',level='30',
attack='30',health='20',lv_type='lalalala',lv_active_level='60',special_effect='')

card_05_21 = Tactic(name = "BEGINNER'S BOLT",set_number='05',card_number='21',card_type='tactic',job='magician',level='20',
lv_type='Spawn/Equip 30',lv_active_level='30',special_effect='Dmg 60')

card_05_23 = Monster(name = 'DARK AXE STUMP',set_number='05',card_number='23',card_type='monster',job='magician',level='22',
attack='10',health='40',lv_type='Spawn 40',lv_active_level='40',special_effect='')

card_05_24 = Item(name = 'DARK NOEL',set_number='05',card_number='24',card_type='item',job='magician',level='35',
lv_type='Think Fast/Equip 50',lv_active_level='50',special_effect='')

card_05_25 = Monster(name = '',set_number='05',card_number='25',card_type='monster',job='magician',level='22',
attack='30',health='90',lv_type='lalalala',lv_active_level='0',special_effect='')

card_05_30 = Character(name = 'MAHIBANG',set_number='05',card_number='30',card_type='character',job='magician',level='0',
health='190',skill_1_lv = '10', skill_1_type = 'Quest',skill_2_lv = '20', skill_2_type = 'Wand Thwack',skill_3_lv = '80', skill_3_type = 'Think Fast 999')

card_05_32 = Monster(name = '',set_number='05',card_number='32',card_type='monster',job='magician',level='62',
attack='60',health='60',lv_type='lalalala',lv_active_level='80',special_effect='')

card_05_40 = Monster(name = 'CLANG',set_number='05',card_number='40',card_type='monster',job='thief',level='48',
attack='50',health='30',lv_type='Equip X',lv_active_level='30',special_effect='')

card_05_43 = Monster(name = '',set_number='05',card_number='43',card_type='monster',job='thief',level='29',
attack='20',health='30',lv_type='lalalala',lv_active_level='50',special_effect='')

card_05_45 = Character(name = 'IVAN19712',set_number='05',card_number='45',card_type='character',job='thief',level='0',
health='200',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '30', skill_2_type = '',skill_3_lv = '50', skill_3_type = '')

card_05_48 = Monster(name = '',set_number='05',card_number='48',card_type='monster',job='thief',level='89',
attack='80',health='90',lv_type='lalalala',lv_active_level='60',special_effect='')

card_05_50 = Item(name = 'PAPER FIGHTER PLANE',set_number='05',card_number='50',card_type='item',job='thief',level='10',
lv_type='Sneak 20',lv_active_level='20',special_effect='')

card_05_51 = Monster(name = '',set_number='05',card_number='51',card_type='monster',job='thief',level='30',
attack='30',health='20',lv_type='lalalala',lv_active_level='0',special_effect='')

card_05_52 = Monster(name = '',set_number='05',card_number='52',card_type='monster',job='thief',level='8',
attack='30',health='30',lv_type='spy',lv_active_level='0',special_effect='')

card_05_53 = Monster(name = '',set_number='05',card_number='53',card_type='monster',job='thief',level='23',
attack='30',health='10',lv_type='lalalala',lv_active_level='30',special_effect='')

card_05_56 = Monster(name = '',set_number='05',card_number='56',card_type='monster',job='warrior',level='88',
attack='80',health='80',lv_type='Spawn/Equip 100',lv_active_level='70',special_effect='')

card_05_57 = Monster(name = '',set_number='05',card_number='57',card_type='monster',job='warrior',level='32',
attack='20',health='30',lv_type='lalalala',lv_active_level='30',special_effect='')

card_05_58 = Item(name = 'DARK MASTER SERGEANT',set_number='05',card_number='58',card_type='item',job='warrior',level='25',
lv_type='Spawn/Equip 50',lv_active_level='50',special_effect='')

card_05_61 = Character(name = 'FANGBLADE',set_number='05',card_number='61',card_type='character',job='warrior',level='0',
health='280',skill_1_lv = '20', skill_1_type = 'Quest',skill_2_lv = '30', skill_2_type = 'Crush',skill_3_lv = '40', skill_3_type = 'Spawn X')

card_05_65 = Monster(name = '',set_number='05',card_number='65',card_type='monster',job='warrior',level='30',
attack='20',health='20',lv_type='lalalala',lv_active_level='60',special_effect='')

card_05_68 = Monster(name = '',set_number='05',card_number='68',card_type='monster',job='warrior',level='33',
attack='30',health='30',lv_type='lalalala',lv_active_level='50',special_effect='')

card_05_72 = Item(name = 'STUDDED POLE ARM',set_number='05',card_number='72',card_type='item',job='warrior',level='20',
lv_type='Spawn/Equip 70',lv_active_level='60',special_effect='')

card_05_76 = Monster(name = '',set_number='05',card_number='76',card_type='monster',job='jobless',level='65',
attack='70',health='30',lv_type='lalalala',lv_active_level='0',special_effect='')

card_05_77 = Monster(name = 'BLUE SNAIL',set_number='05',card_number='77',card_type='monster',job='jobless',level='2',
attack='10',health='20',lv_type='Bash',lv_active_level='10',special_effect='N/A')

card_05_78 = Monster(name = '',set_number='05',card_number='78',card_type='monster',job='jobless',level='35',
attack='30',health='40',lv_type='lalalala',lv_active_level='30',special_effect='')

card_05_79 = Item(name = 'EYE OF FIRE',set_number='05',card_number='79',card_type='item',job='jobless',level='60',
lv_type='Equip 60',lv_active_level='50',special_effect='')

card_05_81 = Monster(name = '',set_number='05',card_number='81',card_type='monster',job='jobless',level='80',
attack='50',health='80',lv_type='lalalala',lv_active_level='60',special_effect='')

card_05_85 = Monster(name = '',set_number='05',card_number='85',card_type='monster',job='jobless',level='70',
attack='40',health='60',lv_type='lalalala',lv_active_level='50',special_effect='')

card_05_86 = Monster(name = 'PUNCO',set_number='05',card_number='86',card_type='monster',job='jobless',level='67',
attack='60',health='70',lv_type='Spawn 40',lv_active_level='40',special_effect='')

card_05_87 = Monster(name = '',set_number='05',card_number='87',card_type='monster',job='jobless',level='80',
attack='80',health='50',lv_type='lalalala',lv_active_level='60',special_effect='')

card_05_88 = Tactic(name = '',set_number='05',card_number='88',card_type='tactic',job='jobless',level='1',
lv_type='lalalala',lv_active_level='20',special_effect='Dmg 20')

card_05_90 = Character(name = 'ZAVIER',set_number='05',card_number='90',card_type='character',job='jobless',level='0',
health='180',skill_1_lv = '10', skill_1_type = '',skill_2_lv = '20', skill_2_type = '',skill_3_lv = '30', skill_3_type = '')






#--
