import ply.lex as lex

class Lexer:
    # build the lexer
    def __init__ (self):
        abbreviations = {
            'CR' : 'CR',
            'XP' : 'XP',
            'Init': 'INIT',
            'Senses': 'SENSES',
            'AC': 'AC',
            'Speed': 'SPEED',
            'feet': 'FEET',
        }

        ability_abbreviations = {
            'Str' : 'STR',
            'Dex' : 'DEX',
            'Con' : 'CON',
            'Int' : 'INT',
            'Wis' : 'WIS',
            'Cha' : 'CHA'
        }

        blocks = {
            'DEFENSE' : 'DEFENSE',
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
        }

        #token list
        tokens = [
            'EOL',
            'SOLIDUS',
            'LPAREN',
            'RPAREN',
            'COMMA',
            'PLUS',
            'SEMICOLON',
            'NUMBER',
            'D',
            'WORD',
        ] + list(abbreviations.values()) + list(blocks.values());
        tokens += list(ability_abbreviations.values()) + list(special_words.keys());

        self.tokens = tokens

        # Regular expression rules for simple tokens
        t_EOL           = '[\n\r]+'
        t_D             = '[dD]'
        t_SOLIDUS       = '[/]'
        t_LPAREN        = '\('
        t_RPAREN        = '\)'
        t_COMMA         = ','
        t_PLUS          = r'\+'
        t_SEMICOLON     = ';'

        #function to disambiguate special words
        def t_WORD(t):
            r'[a-zA-Z\-]+'
            # Check for abbreviations words
            if t.type == 'WORD':
                t.type = abbreviations.get(t.value,'WORD')

            # Check for ability abbreviations words
            if t.type == 'WORD':
                t.type = ability_abbreviations.get(t.value,'WORD')

            # Check for blocks words
            if t.type == 'WORD':
                t.type = blocks.get(t.value,'WORD')

            if t.type == 'WORD':
                for special in special_words:
                    if t.value in special_words[special]:
                        t.type = special
                        break;
            return t

        # Regex rule w/ action code
        def t_NUMBER(t):
            r'\d+'
            t.value = int(t.value)
            return t

        # Define a rule so we can track line numbers
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += 1;
            t.type = "EOL";
            return t

        # ignore
        t_ignore = ' \t'

        # error handler
        def t_error(t):
            print "Illegal character '%s'" % t.value[0]
            t.lexer.skip(1)

        self.lexer = lex.lex()

    def readTokens(self, input_string):
        self.lexer.input(input_string);
        for tok in self.lexer:
            print tok

