
# class to preprocess input blocks
class InputBlock:

    def __init__ (self, raw_text):
        self.raw = raw_text

        # excise the tactics section
        tactics_index = raw_text.find("TACTICS")
        statistics_index = raw_text.find("STATISTICS")

        self.parsable = raw_text[:tactics_index] + raw_text[statistics_index:]
        self.tactics_block = raw_text[tactics_index:statistics_index];


