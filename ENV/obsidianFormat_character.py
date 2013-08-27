class character:
    def output(self):
        out = "h3. " + self.name + "\n"
        out += "*CR* " + str(self.challenge) + "\n"
        out += "*XP* " + str(self.xp_value) + "\n"
        out += "_" + self.gender + '_ _' + self.race + "_\n"
        out += self.class_string() + "\n"

        return out;

    def class_string(self):
        out = ""
        for char_class in self.classes:
            if len(out) > 0:
                out += " / "

            out += "*" + char_class['class'] + "* " + str(char_class['level'])

        return out
