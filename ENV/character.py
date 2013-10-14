# function to turn an integer into a printable modifier
def modifier_string(modifier):
    out = str(modifier);

    if out[0] != "-":
        out = "+" + out

    return out

# function to generate an attack string for an attack
def attack_string(attack):
    # start with the name and attack bonus
    out = attack["name"] + " "
    out += modifier_string(attack["attack bonus"]) + " ("

    # add the damage roll
    out += attack["roll"]

    # add the type and modifier, if they exist
    if len(attack["type"]) > 0:
        out += " " + attack["type"]
    if attack["modifier"] != 0:
        out += modifier_string(attack["modifier"])

    # add the critical
    if attack["critical"] > 2:
        out += "/&times;" + str(attack["critical"])

    # add the effect, if any
    if len(attack["effect"]) > 0:
        out += " " + attack["effect"]
    out += ")"

    return out

# function to generate an attack line from a list of attacks
def attack_list_string(list):
    attacks = ""

    # traverse the list
    for atk in list:
        # indent if this is not the first
        if attacks != "":
            attacks += " or\n%(indent-weapon) "

        # render the attack string
        attacks += attack_string(atk)

    return attacks

# list of ability scores in order
abilities = [
    "Str",
    "Dex",
    "Con",
    "Int",
    "Wis",
    "Cha",
]
# list of skills in order
skills = [
    "Acrobatics",
    "Appraise",
    "Bluff",
    "Climb",
    "Craft",
    "Diplomacy",
    "Disable Device",
    "Disguise",
    "Escape Artist",
    "Fly",
    "Handle Animal",
    "Heal",
    "Intimidate",
    "Knowledge (arcana)",
    "Knowledge (dungeoneering)",
    "Knowledge (engineering)",
    "Knowledge (geography)",
    "Knowledge (history)",
    "Knowledge (local)",
    "Knowledge (nature)",
    "Knowledge (nobility)",
    "Knowledge (planes)",
    "Knowledge (religion)",
    "Linguistics",
    "Perception",
    "Perform",
    "Profession",
    "Profession (sailor)",
    "Ride",
    "Sense Motive",
    "Sleight of Hand",
    "Spellcraft",
    "Stealth",
    "Survival",
    "Swim",
    "Use Magic Device",
]

class character:
    def __init__ (self):
        self.name = "Nobody"
        self.challenge = 0
        self.xp_value = 0
        self.gender = "None"
        self.race = "Human"
        self.classes = {}
        self.alignment = {'moral' : 0, 'ethical' : 0}
        self.size = "Medium"
        self.creature_type = {'primary': 'Humanoid', 'subtypes': []}
        self.initiative = 0;
        self.senses = {"Perception" : 0}
        self.ac = {"alternates" : [{'type' : "touch", 'value': 10}, {'type': "flat-footed", 'value': 10}], "sources" : {}}
        self.hp = 8
        self.hit_dice = 1
        self.hit_dice_list = ["1d8"]
        self.hp_modifier = 0
        self.saves = {"Fort" : 0, "Ref" : 0, "Will" : 0}
        self.save_modifiers = []
        self.defensive_abilities = {}
        self.speed = 30
        self.melee_attacks = [{
            'name': 'Unarmed',
            'attack bonus' : 0,
            'roll' : '1d3',
            'type' : 'nonlethal',
            'modifier' : 0,
            'critical' : 2,
            'effect' : ''
        },]
        self.ranged_attacks = []
        self.special_attacks = []
        self.tactics = {}
        self.abilities = {"Str": 10, "Dex": 10, "Con": 10, "Int": 10, "Wis": 10, "Cha": 10}
        self.base_attack_bonus = 0
        self.combat_maneuver_bonus = 0
        self.combat_maneuver_defense = 10
        self.feats = []
        self.skills = {}

    def output(self):
        out = "h3. " + self.name + "\n"
        out += "*CR* " + str(self.challenge) + "\n"
        out += "*XP* " + str(self.xp_value) + "\n"
        out += "_" + self.gender + '_ _' + self.race + "_\n"
        out += self.class_string() + "\n"
        out += self.alignment_string() + " " + self.size
        out += " " + self.creature_type_string() + "\n"
        out += "*Initiative* " + modifier_string(self.initiative) + "\n"
        out += "*Senses* " + self.senses_string() + "\n"
        out += "\n"
        out += "h3. Defense\n"
        out += "*AC* " + self.ac_string() + "\n"
        out += "*HP* " + self.hp_string() + "\n"
        out += self.saves_string() + "\n"
        defensive_abilities = self.defensive_abilities_string()
        if len(defensive_abilities) > 0:
            out += defensive_abilities + "\n"
        out += "\n"
        out += "h3. Offense\n"
        out += "*Speed* " + str(self.speed) + " ft.\n"
        out += self.attacks_string() + "\n"
        out += "\n"
        tactics = self.tactics_string()
        if (len(tactics) > 0):
            out += "h3. Tactics\n"
            out += tactics + "\n"
            out += "\n"
        out += "h3. Statistics\n"
        out += self.abilities_string() + "\n"
        out += self.combat_modifiers_string() + "\n"
        out += self.feats_string() + "\n"
        out += self.skills_string() + "\n"

        return out;

    # method to generate a string representing this character's classes
    def class_string(self):
        out = ""
        for char_class in self.classes:
            if len(out) > 0:
                out += " / "

            out += "*" + char_class['class'] + "* " + str(char_class['level'])

        return out

    def alignment_string(self):
        out = "*"
        if self.alignment['moral'] > 0:
            out += "Lawful "
        elif self.alignment['moral'] < 0:
            out += "Chaotic "
        else:
            out += "Neutral "

        if self.alignment['ethical'] > 0:
            out += "Good"
        elif self.alignment['ethical'] < 0:
            out += "Evil"
        else:
            if out == "*Neutral ":
                out = "*True Neutral"
            else:
                out += " Neutral"

        out += "*"

        return out

    def creature_type_string(self):
        out = "" + self.creature_type['primary']

        if len(self.creature_type['subtypes']) > 0:
            subs = "("
            for subtype in self.creature_type['subtypes']:
                if subs != "(":
                    subs += ", "
                subs += subtype
            out += subs + ")"

        return out

    # method to print out the Senses line
    def senses_string(self):
        out = ""

        # iterate over the senses and print them
        for sense in self.senses.keys():
            if out != "":
                out += ", "
            out += sense + " " + modifier_string(self.senses[sense])

        return out

    def ac_string(self):
        # build the alternate ac string
        alts = ""
        for ac in self.ac["alternates"]:
            alts += " / " +  ac["type"] + " " + str(ac["value"])

        # builld the components string, and calculate the total ac
        total_ac = 10;
        components = "";
        for component in self.ac["sources"]:
            total_ac += component["value"]
            if components != "":
                components += ", "
            else:
                components += "("
            components += modifier_string(component["value"]) + " " + component["name"]
        if len(components) > 0:
            components +=")"

        out = str(total_ac) + alts
        if len(components) > 0:
            out += " " + components

        return out

    # method to print out the hit points line
    def hp_string(self):
        out = str(self.hp) + " "

        if (self.hit_dice):
            out += "("
            out += str(self.hit_dice) + " HD"
            dice_string = ""
            for dice in self.hit_dice_list:
                if (dice_string != ""):
                    dice_string += " +"
                dice_string += " " + dice
            out += dice_string  + " " + modifier_string(self.hp_modifier)
            out += ")"

        return out

    def saves_string(self):
        out = ""
        out += "*Fort* " + modifier_string(self.saves["Fort"]) + ", ";
        out += "*Ref* " + modifier_string(self.saves["Ref"]) + ", ";
        out += "*Will* " + modifier_string(self.saves["Will"]);

        if len(self.save_modifiers) > 0:
            out += " ("
            specials = ""
            for special in self.save_modifiers:
                if specials != "":
                    specials += ", "
                specials += modifier_string(self.save_modifiers[special]) + " vs. " + special
            out += specials + ")"

        return out

    def defensive_abilities_string(self):
        out = ""
        if len(self.defensive_abilities) > 0:
            abilities = ""
            for ability in self.defensive_abilities:
                if abilities != "":
                    abilities += ", "
                abilities += ability
                val = self.defensive_abilities[ability];
                if (val):
                    abilities += " " + modifier_string(val)

            out += "*Defensive Abilities* " + abilities

        return out

    # method t generate the attacks lines
    def attacks_string(self):
        out = ""
        # generate the melee lines
        if len(self.melee_attacks) > 0:
            out += "*Melee* " + attack_list_string(self.melee_attacks)
        # generate the ranged lines
        if len(self.ranged_attacks) > 0:
            if out != "":
                out += "\n"
            out += "*Ranged* " + attack_list_string(self.ranged_attacks)
        # generate the special lines
        if len(self.special_attacks) > 0:
            if out != "":
                out += "\n"
            attacks = ""
            for atk in self.special_attacks:
                if attacks != "":
                    attacks += ", "
                attacks += atk["name"] + " " + modifier_string(atk["value"])
            out += "*Special Attacks* " + attacks

        return out

    def tactics_string(self):
        out = ""
        for tactic in self.tactics:
            if len(out) :
                out += "\n"
            out += "*" + tactic + "*: " + self.tactics[tactic]

        return out;

    # method to print out the ability scores of a character
    def abilities_string(self):
        out = ""
        for ability in abilities:
            if len(out) > 0:
                out += ", "
            out += "*" + ability + "* " + str(self.abilities[ability])

        return out;

    # method to print out combat modifiers
    def combat_modifiers_string(self):
        out = ""
        out += "*BAB* " + modifier_string(self.base_attack_bonus) + ", "
        out += "*CMB* " + modifier_string(self.combat_maneuver_bonus) + ", "
        out += "*CMD* " + str(self.combat_maneuver_defense)

        return out

    # method to print out the list of feats
    def feats_string(self):
        out = "*Feats*:"
        for feat in self.feats:
            out += "\n * " + feat

        return out

    # method to print out the skills dict
    def skills_string(self):
        out = "*Skills*:"
        for skill in skills:
            if skill in self.skills:
                out += "\n * " + skill + " " + modifier_string(self.skills[skill])

        return out
