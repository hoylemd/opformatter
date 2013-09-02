# coding: utf-8
import ply.lex as lex
from tokens import *

class Lexer:
    # build the lexer
    def __init__ (self):
        self.tokens = tokens

        # Regular expression rules for simple tokens
        t_EOL           = '[\n\r]+'
        t_D             = '[dD]'
        t_SOLIDUS       = '[/]'
        t_LPAREN        = '\('
        t_RPAREN        = '\)'
        t_COMMA         = ','
        t_PLUS          = r'\+'
        t_TIMES         = '×'
        t_SEMICOLON     = ';'

        #function to disambiguate special words
        def t_WORD(t):
            r'[a-zA-Z\-\.]+'
            # Check for abbreviations words
            if t.type == 'WORD':
                t.type = abbreviations.get(t.value,'WORD')

            # Check for abbreviations words
            if t.type == 'WORD':
                t.type = conjunctions.get(t.value,'WORD')

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
