from obsidianFormat_character import character as character
import ply.yacc as yacc

class Parser:
    # error rule
    def __init__(self, lex):
        def p_obsidianFormat (p):
            'obsidianFormat : name statlist'

        def p_statlist_recursive (p):
            'statlist : statlist stat'

        def p_statlist_single (p):
            'statlist : stat'

        def p_stat_eol (p):
            'stat : stat EOL'

        def p_stat_challenge (p) :
            'stat : challenge_rating'

        def p_stat_xp_value (p) :
            'stat : xp_value'

        def p_stat_core (p) :
            'stat : core'

        def p_stat_bio (p) :
            'stat : bio'

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

        def p_class_definitions_list (p) :
            'class_definitions : class_definitions SOLIDUS class_definition'
            class_list = p[1]
            class_list.append(p[3])
            p[0] = class_list

        def p_class_definitions (p) :
            'class_definitions : class_definition'
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
            'size_definition : SIZE'
            p[0] = p[1]

        def p_size_definition_refined (p) :
            'size_definition : SIZE LPAREN SIZE_MOD RPAREN'
            p[0] = p[1] + " (" + p[3] + ")"

        def p_type_definition (p) :
            'type_definition : CREATURE_TYPE'
            p[0] = {'primary' : p[1], 'subtypes' : []}

        def p_type_definition_subs (p) :
            'type_definition : CREATURE_TYPE LPAREN wordlist RPAREN'
            p[0] = {'primary' : p[1], 'subtypes' : p[3]}

        def p_wordlist_list (p):
            'wordlist : wordlist COMMA words'
            p[0] = p[1]
            p[0].append(p[3])

        def p_wordlist (p) :
            'wordlist : words'
            p[0] = [p[1]]

        def p_words (p) :
            'words : WORD'
            p[0] = p[1]

        def p_words_multiple (p):
            'words : words WORD'
            p[0] = p[1] + " " + p[2]

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
