
from encoder import Encoder
from decode import Decoder

if __name__ == "__main__":

    # Encode
    encoder = Encoder('abcde', -5, 'jjh')
    print('Encode result -->', encoder.encode_string())

    # Decode
    decoder = Decoder('vewexcyez', -5)
    print('Decode result -->', decoder.decode_string())
