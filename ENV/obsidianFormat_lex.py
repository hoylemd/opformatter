import ply.lex as lex

class Lexer:
    # build the lexer
    def __init__ (self):
        abbreviations = {
            'CR' : 'CR',
            'XP' : 'XP',
            'Init': 'INIT',
            'Senses': 'SENSES',
        }

        blocks = {
            'DEFENSE' : 'DEFENSE',
        }

        genders = ['Male', 'Female']

        classes = [
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
        ]

        creature_types = [
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
        ]

        alignments = [
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
        ]

        sizes = [
            'Fine',
            'Diminutive',
            'Tiny',
            'Small',
            'Medium',
            'Large',
            'Huge',
            'Gargantual',
            'Colossal',
        ]

        size_modifiers = [
            'tall',
            'long'
        ]

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
            'GENDER',
            'CLASS',
            'ALIGNMENT',
            'SIZE',
            'SIZE_MOD',
            'CREATURE_TYPE',

        ] + list(abbreviations.values()) + list(blocks.values())

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
            r'[a-zA-Z]+'
            # Check for abbreviations words
            if t.type == 'WORD':
                t.type = abbreviations.get(t.value,'WORD')

            # Check for blocks words
            if t.type == 'WORD':
                t.type = blocks.get(t.value,'WORD')

            if t.type == 'WORD':
                if t.value in genders:
                    t.type = 'GENDER'
                elif t.value in classes:
                    t.type = 'CLASS'
                elif t.value in alignments:
                    t.type = 'ALIGNMENT'
                elif t.value in sizes:
                    t.type = 'SIZE'
                elif t.value in size_modifiers:
                    t.type = 'SIZE_MOD'
                elif t.value in creature_types:
                    t.type = 'CREATURE_TYPE'

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

