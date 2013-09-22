def modifier_string(modifier):
    out = str(modifier);

    if out == "0":
        out = ""
    elif out[0] != "-":
        out = "+" + out

    return out

def attack_string(attack):
    out = attack["name"] + " "
    out += modifier_string(attack["attack bonus"]) + " ("
    out += attack["roll"]
    if len(attack["type"]) > 0:
        out += " " + attack["type"]
    if attack["modifier"] != 0:
        out += modifier_string(attack["modifier"])
    if attack["critical"] > 0:
        out += "/&times;" + str(attack["critical"])
    if len(attack["effect"]) > 0:
        out += " " + attack["effect"]
    out += ")"
    return out

def attack_list_string(list):
    attacks = ""
    for atk in list:
        if attacks != "":
            attacks += " or\n%(indent-weapon) "

        attacks += attack_string(atk)
    return attacks

class character:
    def output(self):
        out = "h3. " + self.name + "\n"
        out += "*CR* " + str(self.challenge) + "\n"
        out += "*XP* " + str(self.xp_value) + "\n"
        out += "_" + self.gender + '_ _' + self.race + "_\n"
        out += self.class_string() + "\n"
        out += self.alignment_string() + " " + self.size
        out += " " + self.creature_type_string() + "\n"
        out += "*Initiative* " + self.initiative_string() + "\n"
        out += "*Senses* " + self.senses_string() + "\n"
        out += "\n"
        out += "h3. Defense\n"
        out += "*AC* " + self.ac_string() + "\n"
        out += "*HP* " + self.hp_string() + "\n"
        out += self.saves_string() + "\n"
        out += self.defensive_abilities_string() + "\n"
        out += "\n"
        out += "h3. Offense\n"
        out += "*Speed* " + str(self.speed) + " ft.\n"
        out += self.attacks_string() + "\n"
        out += "\n"
        out += "h3. Tactics\n"
        out += self.tactics_string() + "\n"

        return out;

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

    def initiative_string(self):
        return modifier_string(self.initiative)

    def senses_string(self):
        out = ""

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

        return str(total_ac) + alts + " " + components

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

    def attacks_string(self):
        out = ""
        if len(self.melee_attacks) > 0:
            out += "*Melee* " + attack_list_string(self.melee_attacks)
        if len(self.ranged_attacks) > 0:
            if out != "":
                out += "\n"
            out += "*Ranged* " + attack_list_string(self.ranged_attacks)
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
