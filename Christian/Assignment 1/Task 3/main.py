
from encoder import Encoder
from decode import Decoder

if __name__ == "__main__":

    # Encode
    encoder = Encoder('abcde', -5)
    encoder_result = encoder.encode_string()
    print('Encode result -->', encoder_result)

    # Decode
    decoder = Decoder(encoder_result, -5)
    print('Decode result -->', decoder.decode_string())
