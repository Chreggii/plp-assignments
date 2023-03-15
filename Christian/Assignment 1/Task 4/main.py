
from encoder import Encoder
from decode import Decoder

if __name__ == "__main__":

    allowed_keywords = ['encode', 'decode']

    is_quit = False

    while not is_quit:
        input_string = input("> ")
        if input_string == 'quit':
            is_quit = True
            break
        else:
            try:
                splitted_input = input_string.split()

                if len(splitted_input) >= 3:

                    if splitted_input[0] == 'encode':
                        # Encode
                        additional_string = splitted_input[3] if len(
                            splitted_input) == 4 else None
                        encoder = Encoder(
                            splitted_input[1], int(splitted_input[2]), additional_string)
                        encoder_result = encoder.encode_string()
                        print(encoder_result)

                    elif splitted_input[0] == 'decode':
                        # Decode
                        decoder = Decoder(
                            splitted_input[1], int(splitted_input[2]))
                        print(decoder.decode_string())

                    else:
                        raise
                else:
                    raise
            except:
                print('Invalid Input!')
