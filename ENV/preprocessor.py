
import re

# class to preprocess input blocks
class InputBlock:

    # function to parse out the tactics
    def ingest_tactics(self, tactics_block):
        # initialize stuff
        sections = re.compile(r'\n(During Combat|Morale) ')
        self.tactics = {}
        found = sections.search(tactics_block)

        # keep grabbing tactic sections
        while (found):
            # grab the tactic name
            name = tactics_block[found.start() + 1:found.end() - 1]

            # find the next one
            next = sections.search(tactics_block, found.end())

            # extract the tactic text
            if next :
                value = tactics_block[found.end():next.start()]
            else:
                value = tactics_block[found.end():]

            # strip newlines
            self.tactics[name] = value.replace('\n', ' ').rstrip()

            # stage the next tactic
            found = next

    def __init__ (self, raw_text):
        self.raw = raw_text
        self.parsable = raw_text

        # excise the tactics section
        tactics_index = self.parsable.find("TACTICS")
        if (tactics_index > 0):
            stats_index = self.parsable.find("STATISTICS")

            parsable = self.parsable[:tactics_index]
            if (stats_index > 0):
                parsable += self.parsable[stats_index:]
            self.tactics_block = self.parsable[tactics_index:stats_index];
            self.parsable = parsable
            self.ingest_tactics(self.tactics_block)
        else:
            self.tactics_block = ""
            self.tactics = {};

