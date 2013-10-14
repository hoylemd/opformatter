
import re

# class to preprocess input blocks
class InputBlock:

    # function to parse out the tactics
    def ingestTactics(self, tactics_block):
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

    # method to ingest a feats list
    def ingestFeats (self, feats_block):
	self.feats = []

	# sanitize the string to just the feats
	feats_string = feats_block[6:].replace('\n', ' ').rstrip()

	# split the string
	self.feats += feats_string.split(", ")

	# store the feats list, and empty it properly if there aren't any
	if (len(self.feats) == 1 and self.feats[0] == ''):
		self.feats= [];

    # method to ingest a skills list
    def ingestSkills (self, skills_block):
	self.skills = {}

    # method to ingest a languages list
    def ingestLanguages (self, languages_block):
	self.languages = []

    # method to ingest SQs
    def ingestSpecialQualities (self, sq_block):
	self.special_qualities = []

    # method to ingest Combat Gear
    def ingestCombatGear (self, combat_gear_block):
	self.combat_gear = []

    # method to ingest Other Gear
    def ingestOtherGear (self, other_gear_block):
	self.other_gear = []

    # function to excise a string from the stored string
    # removes it from the stored string, and returns it
    # params:
    #   start: string that starts the substring
    #   end: string that ends the substring, optional
    def exciseBlock(self, start, end=None):
	block = ""

	# find the beginning
	start_index = self.parsable.find(start)
        if (start_index > -1):
	    # store the prefix in a temp variable
            parsable = self.parsable[:start_index]

	    # find the end index, if a string for it has been defined
	    end_index = -1
	    if end != None:
		end_index = self.parsable.find(end)

	    # store the suffix in the temp
	    if (end_index > -1):
                parsable += self.parsable[end_index:]

	    # extract the target string
            block = self.parsable[start_index:end_index];

	    # store the cut-down string back in the object
            self.parsable = parsable

	return block

    def __init__ (self, raw_text):
        self.raw = raw_text
        self.parsable = raw_text

        # excise the tactics section
	self.ingestTactics(self.exciseBlock("TACTICS", "STATISTICS"))

	# excise the Feats section
	self.ingestFeats(self.exciseBlock("Feats", "Skills"))

	# excise the Skills section
	self.ingestSkills(self.exciseBlock("Skills", "Languages"))

	# excise the Languages section
	self.ingestLanguages(self.exciseBlock("Languages", "SQ"))

	# excise the Special Qualities section
	self.ingestSpecialQualities(self.exciseBlock("SQ", "Combat Gear"))

	# excise the Combat Gear section
	self.ingestCombatGear(self.exciseBlock("Combat Gear", "; Other Gear"))

	# excise the Other Gear section
	self.ingestOtherGear(self.exciseBlock("; Other Gear"))
