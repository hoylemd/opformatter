from obsidianFormat_character import character as character
import ply.yacc as yacc

class Parser:
    # error rule
    def __init__(self, lex):
        def p_obsidianFormat (p):
            'obsidianFormat : firstline'

        def p_firstline (p):
            'firstline : name challenge_rating EOL'
            self.character.name = p[1]
            self.character.challenge = p[2]

        def p_name (p):
            'name : words'
            p[0] = p[1]

        def p_words (p):
            'words : WORD'
            p[0] = p[1]

        def p_words_multiple (p):
            'words : words WORD'
            p[0] = p[1] + " " + p[2]

        def p_challenge_rating (p):
            'challenge_rating : CR NUMBER'
            p[0] = p[2]


        """def p_dice_definition (p):
            'dice_definition : NUMBER D NUMBER'
            if (p[1] <= 5):
                p[0] = dice(p[1], p[3])
            else:
                raise Exception("too many dice!")

        def p_single_dice_definition (p):
            'dice_definition : D NUMBER'
            p[0] = dice(1, p[2])

        def p_target_definition (p):
            'target_definition : optional_whitespace VERSUS optional_whitespace NUMBER'
            p[0] = p[4]

        def p_optional_whitespace (p):
            'optional_whitespace : WHITESPACE'

        def p_optional_whitespace_blank (p):
            'optional_whitespace : '
        """

        def p_error (p):
            print "syntax error in input!"
            self.error = True
            print p

        self.error = False;
        self.lexer = lex.lexer

        tokens = lex.tokens

        self.parser = yacc.yacc()

        self.character = character();

    def parse(self, s):
        result = self.parser.parse(s, lexer=self.lexer)
        return result
