import ply.lex as lex

class Lexer:
    # build the lexer
    def __init__ (self):
        reserved = {
           'CR' : 'CR',
           'XP' : 'XP',
        }

        #token list
        tokens = [
            'EOL',
            'NUMBER',
            'D',
            'WORD',
        ] + list(reserved.values())

        self.tokens = tokens

        # Regular expression rules for simple tokens
        t_EOL            = "[\n\r]+"
        #t_WHITESPACE    = '[ \t]+'
        t_D                = '[dD]'

        #function to disambiguate special words
        def t_WORD(t):
            r'[a-zA-Z]+'
            # Check for reserved words
            t.type = reserved.get(t.value,'WORD')
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

