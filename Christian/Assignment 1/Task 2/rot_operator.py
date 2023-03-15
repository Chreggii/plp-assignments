class RotOperator:
    def __init__(self, phrase, offset):
        self.phrase = phrase
        self.offset = offset

    # Apply ROT
    def apply_rot(self, offset=None):
        abc = "abcdefghijklmnopqrstuvwxyz"
        out_phrase = ""

        offset = offset if offset is not None else self.offset

        for char in self.phrase:
            out_phrase += abc[(abc.find(char)+offset) % 26]
        return out_phrase

    # Reset ROT
    def reset_rot(self):
        return self.apply_rot(self.offset*(-1))
