
from encoder import Encoder


def to_ascii(string):
    return [ord(character) for character in string]


def to_string(ascii_list):
    return ''.join([chr(x) for x in ascii_list])


def rot(phrase, offset):
    abc = "abcdefghijklmnopqrstuvwxyz"
    out_phrase = ""
    for char in phrase:
        out_phrase += abc[(abc.find(char)+offset) % 26]
    return out_phrase


def encode_string(string_to_encode, offset, additional_string):

    # Convert the string to a list of ASCII values
    ascii_values = to_ascii(string_to_encode)

    # Insert additional values between each existing value
    additional_values = to_ascii(additional_string)
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
    encoded_string = to_string(ascii_values)

    # Apply rot and return value
    return rot(encoded_string, offset)


if __name__ == "__main__":
    a = Encoder.encode_string('abcde', -5, 'jjh')
    print(a)

    # # Example usage
    # encoded = encode_string('abcde', -5, 'jjh')
    # print(encoded)  # Output: vewexcyez
