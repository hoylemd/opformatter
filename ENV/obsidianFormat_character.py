class character:
    def output(self):
        out = "h3. " + self.name + "\n"
        out += "*CR* " + str(self.challenge) + "\n"
        out += "*XP* " + str(self.xp_value) + "\n"

        return out;
