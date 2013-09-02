#coding: utf-8
abbreviations = {
    'CR' : 'CR',
    'XP' : 'XP',
    'Init': 'INIT',
    'Senses': 'SENSES',
    'AC': 'AC',
    'hp': 'HP',
    'HD': 'HD',
    'd': 'D',
    'vs.' : 'VS',
    'Defensive' : 'DEFENSIVE',
    'Abilities' : 'ABILITIES',
    'Speed': 'SPEED',
    'feet': 'FEET',
    'Melee': 'MELEE',
}

ability_abbreviations = {
    'Str' : 'STR',
    'Dex' : 'DEX',
    'Con' : 'CON',
    'Int' : 'INT',
    'Wis' : 'WIS',
    'Cha' : 'CHA',
}

conjunctions = {
    'or' : 'OR',
}

blocks = {
    'DEFENSE' : 'DEFENSE',
    'OFFENSE' : 'OFFENSE',
}

special_words = {
    "GENDER" : [
        'Male',
        'Female',
    ],
    "CLASS" : [
        'barbarian',
        'bard',
        'cleric',
        'druid',
        'fighter',
        'monk',
        'paladin',
        'ranger',
        'rogue',
        'sorcerer',
        'wizard',
        'arcane archer',
        'arcane trickster',
        'assassin',
        'dragon disciple',
        'eldrich knight',
        'loremaster',
        'mystic theurge',
        'pathfinder chronicler',
        'shadowdancer',
        'adept',
        'aristocrat',
        'commoner',
        'expert',
        'warrior',
    ],
    "CREATURE_TYPE" : [
        'abberation',
        'animal',
        'construct',
        'dragon',
        'fey',
        'humanoid',
        'magical beast',
        'monstrous humanoid',
        'ooze',
        'outsider',
        'plant',
        'undead',
        'vermin',
    ],
    "ALIGNMENT" : [
        'LG',
        'NG',
        'CG',
        'LN',
        'TN',
        'NN',
        'CN',
        'LE',
        'NE',
        'CE',
    ],
    "SIZE" : [
        'Fine',
        'Diminutive',
        'Tiny',
        'Small',
        'Medium',
        'Large',
        'Huge',
        'Gargantual',
        'Colossal',
    ],
    "SIZE_MOD" : [
        'tall',
        'long'
    ],
    "AC_TYPE" : [
        'touch',
        'flat-footed',
    ],
    "SAVING_THROW" : [
        'Fort',
        'Ref',
        'Will',
    ],
    "DAMAGE_TYPE" : [
        'nonlethal',
    ],
}

#token list
tokens = [
    'EOL',
    'SOLIDUS',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'PLUS',
    'TIMES',
    'SEMICOLON',
    'NUMBER',
    'WORD',
] + list(abbreviations.values()) + list(blocks.values()) + list(ability_abbreviations.values())

tokens += list(conjunctions.values()) + list(special_words.keys())


