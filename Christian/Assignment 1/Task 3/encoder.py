import math
import random
from rot_operator import RotOperator
from string_ascii_converter import StringAsciiConverter


class Encoder:

    def __init__(self, string_to_encode, offset):
        self.string_to_encode = string_to_encode
        self.offset = offset

    # Encodes string and returns value
    def encode_string(self):
        # Convert the string to a list of ASCII values
        ascii_values = StringAsciiConverter.to_ascii(self.string_to_encode)

        # Convert the additional string to a list of ASCII values
        additional_values = self.__get_random_salt(len(ascii_values))

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
        half_of_string_length = string_length / 2
        number_of_random_values = 0

        # Define number of random values
        if half_of_string_length % 2 == 0:
            number_of_random_values = half_of_string_length + 1
        else:
            number_of_random_values = math.ceil(half_of_string_length)

        print(number_of_random_values)

        result = []
        # Add random values to list
        for _ in range(number_of_random_values):
            result.append(random.randint(97, 122))

        return result
