def modifier_string(modifier):
        out = ""

        if modifier > 0:
            out += "+"

        out += str(modifier);

        return out

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
        out += "*AC* " + str(self.ac_string()) + "\n"
        out += "*Speed* " + str(self.speed) + " ft.\n"


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

