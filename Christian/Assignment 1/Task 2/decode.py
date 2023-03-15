from rot_operator import RotOperator
from string_ascii_converter import StringAsciiConverter


class Decoder:

    def __init__(self, string_to_decode, offset):
        self.string_to_decode = string_to_decode
        self.offset = offset

    def decode_string(self):

        # Reset ROT
        string = RotOperator(self.string_to_decode, self.offset).reset_rot()

        # Convert the string to a list of ASCII values
        ascii_values = StringAsciiConverter.to_ascii(string)

        # Delete very second entry (found here: https://stackoverflow.com/questions/22023107/how-to-first-remove-every-second-element-on-a-list-then-every-third-on-whats-re)
        del ascii_values[1::2]

        # Convert to string and return value
        return StringAsciiConverter.to_string(ascii_values)
