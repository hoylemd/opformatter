import ply.lex as lex

class Lexer:
    # build the lexer
    def __init__ (self):
        abbreviations = {
           'CR' : 'CR',
           'XP' : 'XP',
        }

        genders = ['Male', 'Female']

        #token list
        tokens = [
            'EOL',
            'SOLIDUS',
            'NUMBER',
            'D',
            'WORD',
            'GENDER',
        ] + list(abbreviations.values())

        self.tokens = tokens

        # Regular expression rules for simple tokens
        t_EOL           = '[\n\r]+'
        t_D             = '[dD]'
        t_SOLIDUS       = '[/]'

        #function to disambiguate special words
        def t_WORD(t):
            r'[a-zA-Z]+'
            # Check for abbreviations words
            t.type = abbreviations.get(t.value,'WORD')
            if t.type == 'WORD' and t.value in genders:
                t.type = 'GENDER'
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
        t_ignore = '[ \t]+'

        # error handler
        def t_error(t):
            print "Illegal character '%s'" % t.value[0]
            t.lexer.skip(1)

        self.lexer = lex.lex()

    def readTokens(self, input_string):
        self.lexer.input(input_string);
        for tok in self.lexer:
            print tok

