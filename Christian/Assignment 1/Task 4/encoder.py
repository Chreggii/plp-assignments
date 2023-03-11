import math
import random
from rot_operator import RotOperator
from string_ascii_converter import StringAsciiConverter


class Encoder:

    def __init__(self, string_to_encode, offset, additional_string=None):
        self.string_to_encode = string_to_encode
        self.offset = offset
        self.additional_string = additional_string

    # Encodes string and returns value
    def encode_string(self):
        # Convert the string to a list of ASCII values
        ascii_values = StringAsciiConverter.to_ascii(self.string_to_encode)

        additional_values = self.__get_random_salt(len(
            ascii_values)) if self.additional_string is None else StringAsciiConverter.to_ascii(self.additional_string)

        # Insert additional values between each existing value
        listLength = len(ascii_values)
        # iterator for insert position
        i = 1
        # iterator for index of additional list
        x = 0
        while i < (listLength*2 - 1):
            ascii_values.insert(
                i, additional_values[x % len(additional_values)])
            i += 2
            x += 1

        # Convert ascii values to strings
        encoded_string = StringAsciiConverter.to_string(ascii_values)

        # Apply rot and return value
        return RotOperator(encoded_string, self.offset).apply_rot()

    def __get_random_salt(self, string_length):
        number_of_random_values = string_length - 1
        result = []

        # Add random values to list
        for _ in range(number_of_random_values):
            result.append(random.randint(97, 122))

        return result
