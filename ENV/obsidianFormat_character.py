class character:
    def output(self):
        out = "h3. " + self.name + "\n"
        out += "*CR* " + str(self.challenge) + "\n"
        out += "*XP* " + str(self.xp_value) + "\n"
        out += "_" + self.gender + '_ _' + self.race + "_\n"
        out += self.class_string() + "\n"
        out += self.alignment_string() + " " + self.size
        out += " " + self.creature_type_string() + "\n"

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
                if subs <> "(":
                    subs += ", "
                subs += subtype
            out += subs + ")"

        return out


