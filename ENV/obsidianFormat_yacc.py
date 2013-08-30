from obsidianFormat_character import character as character
import ply.yacc as yacc

class Parser:
    # error rule
    def __init__(self, lex):
        def p_obsidianFormat (p):
            '''
            obsidianFormat : blocks
            '''

        def p_blocks (p):
            '''
            blocks : blocks block
                | block
            '''

        def p_block (p):
            '''
            block : overview
            '''

        def p_overview (p):
            '''
            overview : name statlist
            '''

        def p_statlist (p):
            '''statlist : statlist stat
                        | stat'''

        def p_stat (p):
            '''
            stat : stat EOL
                | stat SEMICOLON
                | challenge_rating
                | xp_value
                | core
                | bio
                | initiative
                | senses
            '''

        def p_name (p) :
            'name : words'
            self.character.name = p[1]

        def p_challenge_rating (p) :
            'challenge_rating : CR NUMBER'
            self.character.challenge = p[2]

        def p_xp_value (p) :
            'xp_value : XP NUMBER'
            self.character.xp_value = p[2]

        def p_core (p) :
            'core : race_definition class_definitions'
            self.character.classes = p[2]

        def p_race (p) :
            'race_definition : GENDER words'
            self.character.gender = p[1]
            self.character.race = p[2]

        def p_class_definitions (p) :
            '''
            class_definitions : class_definitions SOLIDUS class_definition
                | class_definition
            '''
            if len(p) > 2:
                class_list = p[1]
                class_list.append(p[3])
                p[0] = class_list
            else:
                p[0] = [p[1]];

        def p_class_definition (p) :
            'class_definition : CLASS NUMBER'
            p[0] = {'class' : p[1], 'level' : p[2]}

        def p_bio (p) :
            'bio : alignment size_definition type_definition'
            self.character.alignment = p[1]
            self.character.size = p[2]
            self.character.creature_type = p[3]

        def p_alignment (p) :
            'alignment : ALIGNMENT'
            moral = p[1][:1]
            ethical = p[1][1:]
            p[0] = {'moral' : 0, 'ethical' : 0}
            if moral == 'L':
                p[0]['moral'] = 1
            elif moral == 'C':
                p[0]['moral'] = -1

            if ethical == 'G':
                p[0]['ethical'] = 1
            elif ethical == 'E':
                p[0]['ethical'] = -1

        def p_size_definition (p) :
            '''
            size_definition : SIZE LPAREN SIZE_MOD RPAREN
                | SIZE
            '''
            if len(p) == 5:
                p[0] = p[1] + " (" + p[3] + ")"
            else:
                p[0] = p[1]

        def p_type_definition (p) :
            '''
            type_definition :  CREATURE_TYPE LPAREN wordlist RPAREN
                | CREATURE_TYPE
            '''
            if len(p) == 5:
                p[0] = {'primary' : p[1], 'subtypes' : p[3]}
            else :
                p[0] = {'primary' : p[1], 'subtypes' : []}

        def p_initiative (p):
            '''
            initiative : INIT modifier
            '''
            self.character.initiative = p[2]

        def p_senses (p):
            '''
            senses : SENSES WORD modifier
            '''
            self.character.senses = {p[2] : p[3]}

        def p_wordlist (p) :
            '''
            wordlist : wordlist COMMA words
                |  words
            '''
            if len(p) == 4:
                p[0] = p[1]
                p[0].append(p[3])
            else:
                p[0] = [p[1]]

        def p_words (p) :
            '''
            words : words WORD
                | WORD
            '''
            if len(p) == 3:
                p[0] = p[1] + " " + p[2]
            else :
                p[0] = p[1]

        def p_dice_definition (p):
            '''
            dice_definition : NUMBER D NUMBER
                | D NUMBER
            '''
            if len(p) == 4:
                p[0] = p[1] + "d" + p[3]
            else :
                p[0] = "1d" + p[2]

        def p_modifier (p):
            '''
            modifier : PLUS NUMBER
            '''
            p[0] = p[2]

        # Compute column.
        # token is a token instance
        def find_column(token):
            last_cr = self.input.rfind('\n',0,token.lexpos)
            if last_cr < 0:
                last_cr = 0
            column = (token.lexpos - last_cr) + 1
            return column

        # error rule
        def p_error (p):
            print "syntax error at position " + str(find_column(p)) + ", line " + str(p.lineno)
            print str(p) + " << current token"

            for tok in lex.lexer:
                print str(tok)

            self.error = True

        self.error = False;
        self.lexer = lex.lexer

        tokens = lex.tokens

        self.parser = yacc.yacc()

        self.character = character();

    def parse(self, s):
        self.input = s;
        result = self.parser.parse(s, lexer=self.lexer)
        return result
