# coding: utf-8
from character import character as character
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
                | defense_block
                | offense_block
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

        def p_defense_block (p):
            '''
            defense_block : DEFENSE EOL defenses
                | DEFENSE defenses
            '''

        def p_defenses (p):
            '''
            defenses : defenses defense
                | defense
            '''

        def p_defense (p):
            '''
            defense : defense EOL
                | ac_definition
                | hp_definition
                | saves_definition
                | defensive_abilities
            '''

        def p_ac_definition (p):
            '''
            ac_definition : AC NUMBER COMMA alternate_acs ac_sources
                | AC NUMBER
            '''
            self.character.ac = {"alternates" : p[4], "sources" : p[5]}

        def p_alternate_acs (p):
            '''
            alternate_acs : alternate_acs COMMA alternate_ac
                | alternate_ac
                |
            '''
            if len(p) == 4:
                p[0] = p[1] + [p[3]]
            elif len(p) == 2:
                p[0] = [p[1]]
            else:
                p[0] = []

        def p_alternate_ac (p):
            '''
            alternate_ac : AC_TYPE NUMBER
            '''
            p[0] = {"type" : p[1], "value" : p[2]};

        def p_ac_sources (p):
            '''
            ac_sources : LPAREN ac_source_list RPAREN
                |
            '''
            p[0] = p[2];

        def p_ac_source_list (p):
            '''
            ac_source_list : ac_source_list COMMA ac_source
                | ac_source
            '''
            if len(p) == 4:
                p[0] = p[1] + [p[3]]
            else:
                p[0] = [p[1]]

        def p_ac_source (p):
            '''
            ac_source : modifier words
                | modifier DEX
            '''
            p[0] = { "name" : p[2], "value" : p[1] }

        def p_hp_definition (p):
            '''
            hp_definition : HP NUMBER hit_dice_def
            '''
            self.character.hp = p[2]

        def p_hit_dice_def (p):
            '''
            hit_dice_def : LPAREN NUMBER HD SEMICOLON hit_dice_list modifier RPAREN
            '''
            self.character.hit_dice = p[2]
            self.character.hit_dice_list = p[5]
            self.character.hp_modifier = p[6]

        def p_hit_dice_list (p):
            '''
            hit_dice_list : hit_dice_list PLUS dice_def
                | dice_def
            '''
            if len(p) == 4:
                p[0] = p[1] + [p[3]]
            elif len(p) == 2:
                p[0] = [p[1]]

        def p_saves_definition (p):
            '''
            saves_definition : saves_list SEMICOLON special_saves
            '''
            self.character.saves = p[1]
            self.character.save_modifiers = p[3]

        def p_saves_list (p):
            '''
            saves_list : saves_list COMMA save
                | save
            '''
            if len(p) == 4:
                p[0] = dict(p[1].items() + p[3].items())
            else:
                p[0] = p[1]

        def p_save (p):
            '''
            save : SAVING_THROW modifier
            '''
            p[0] = {p[1]: p[2]}

        def p_special_saves (p):
            '''
            special_saves : special_saves COMMA special_save
                | special_save
            '''
            if len(p) == 4:
                p[0] = dict(p[3].items() + p[1].items())
            else :
                p[0] = p[1]

        def p_special_save (p):
            '''
            special_save : modifier VS WORD
            '''
            p[0] = {p[3] : p[1]}

        def p_defensive_abilities (p):
            '''
            defensive_abilities : DEFENSIVE ABILITIES def_abilities_list
            '''
            self.character.defensive_abilities = p[3]

        def p_def_abilities_list (p):
            '''
            def_abilities_list : def_abilities_list COMMA defensive_ability
                | defensive_ability
            '''
            if len(p) == 4:
                p[0] = dict(p[3].items() + p[1].items())
            else:
                p[0] = p[1]

        def p_defensive_ability (p):
            '''
            defensive_ability : WORD modifier
                | WORD
            '''
            if len(p) == 3:
                p[0] = { p[1]  : p[2]}
            else:
                p[0] = { p[1]  : None}

        def p_offense_block (p):
            '''
            offense_block : OFFENSE EOL offenses
                | OFFENSE offenses
            '''

        def p_offenses (p):
            '''
            offenses : offenses offense
                | offense
            '''

        def p_offense (p):
            '''
            offense : offense EOL
                | speed
                | melee_definition
                | ranged_definition
                | special_attacks_definition
            '''

        def p_speed (p):
            '''
            speed : SPEED NUMBER FEET
            '''
            self.character.speed = p[2]

        def p_melee_definition (p):
            '''
            melee_definition : MELEE attacks
            '''
            self.character.melee_attacks = p[2]

        def p_ranged_definition (p):
            '''
            ranged_definition : RANGED attacks
            '''
            self.character.ranged_attacks = p[2]

        def p_attacks (p):
            '''
            attacks : attacks OR EOL attack
                | attack
            '''
            if len(p) == 5:
                p[0] = p[1] + [p[4]]
            else:
                p[0] = [p[1]]

        def p_attack (p):
            '''
            attack : words modifier damage_specification
            '''
            full_attack_spec = p[3]
            full_attack_spec["name"] = p[1]
            full_attack_spec["attack bonus"] = p[2]
            p[0] = full_attack_spec

        def p_special_attacks_definition (p):
            '''
            special_attacks_definition : SPECIAL ATTACKS special_attacks
            '''
            self.character.special_attacks = p[3]

        def p_special_attacks (p):
            '''
            special_attacks : special_attacks COMMA special_attack
                | special_attack
            '''
            if len(p) == 4:
                p[0] = p[1] + [p[3]]
            else :
                p[0] = [p[1]]

        def p_special_attack (p):
            '''
            special_attack : words optional_modifier
            '''
            p[0] = {"name" : p[1], "value" : p[2]}

        def p_damage_specification (p):
            '''
            damage_specification : LPAREN dice_def damage_type optional_modifier crit_spec effect_spec RPAREN
            '''
            p[0] = {
                "roll" : p[2],
                "type" : p[3],
                "modifier" : p[4],
                "critical" : p[5],
                "effect" : p[6]
            }

        def p_damage_type (p):
            '''
            damage_type : DAMAGE_TYPE
                |
            '''
            if len(p) == 2:
                p[0] = p[1]
            else :
                p[0] = ""

        def p_crit_spec (p):
            '''
            crit_spec : SOLIDUS TIMES NUMBER
                |
            '''
            if len(p) == 4:
                p[0] = p[3]
            else:
                p[0] = 0

        def p_effect_spec (p):
            '''
            effect_spec : words
                |
            '''
            effect_string = ""
            if len(p) == 2:
                effect_string = p[1]

            p[0] = effect_string;

        # utility rules

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

        def p_optional_modifier (p):
            '''
            optional_modifier : modifier
                |
            '''
            if len(p) == 2:
                p[0] = p[1]
            else:
                p[0] = 0

        def p_modifier (p):
            '''
            modifier : PLUS value
            '''
            p[0] = p[2]

        def p_value (p):
            '''
            value : NUMBER
                | dice_def
            '''
            p[0] = p[1]

        def p_dice_def (p):
            '''
            dice_def : NUMBER D NUMBER
            '''
            p[0] = str(p[1]) + "d" + str(p[3])


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
            if p:
                print "syntax error at " + str(p.type) + " token '" + str(p.value),
                print  "' at position " + str(find_column(p)) + ", line " + str(p.lineno),
                print " in rule " + str(self.rule)
                #self.lex.readTokens(self.input)

                self.error = True

        self.error = False
        self.lex = lex
        self.rule = ""

        tokens = lex.tokens

        self.parser = yacc.yacc()

        self.character = character()

    def parse(self, s):
        self.input = s
        result = self.parser.parse(s, lexer=self.lex.lexer)
        return result
