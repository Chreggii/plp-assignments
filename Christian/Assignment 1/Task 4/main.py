
from encoder import Encoder
from decode import Decoder

if __name__ == "__main__":

    allowed_keywords = ['encode', 'decode']

    isQuite = False

    while not isQuite:
        input_string = input("> ")
        if input_string == 'quit':
            isQuite = True
            break
        else:
            splitted_input = input_string.split()

            if len(splitted_input) >= 3:

                if splitted_input[0] == 'encode':
                    try:
                        # Encode
                        optional_parameter = splitted_input[3] if len(
                            splitted_input) == 4 else None
                        encoder = Encoder(
                            splitted_input[1], int(splitted_input[2]), optional_parameter)
                        encoder_result = encoder.encode_string()
                        print(encoder_result)
                    except:
                        print('Invalid Input!')

                elif splitted_input[0] == 'decode':
                    try:
                        # Decode
                        decoder = Decoder(
                            splitted_input[1], int(splitted_input[2]))
                        print(decoder.decode_string())
                    except:
                        print('Invalid Input!')
                else:
                    print('Invalid Input!')
            else:
                print('Invalid Input!')
