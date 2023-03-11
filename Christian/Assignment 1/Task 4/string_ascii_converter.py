class StringAsciiConverter:

    # Convert string to ascii
    def to_ascii(string):
        return [ord(character) for character in string]

    # Convert ascii to string
    def to_string(ascii_list):
        return ''.join([chr(x) for x in ascii_list])
