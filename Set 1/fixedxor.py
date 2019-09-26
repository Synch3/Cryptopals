#  Write a function that takes two equal-length buffers and produces their XOR combination.

# If your function works properly, then when you feed it the string:

# 1c0111001f010100061a024b53535009181c

# ... after hex decoding, and when XOR'd against:

# 686974207468652062756c6c277320657965

# ... should produce:

# 746865206b696420646f6e277420706c6179

import codecs

def xorcombination(string1, string2):
    decoded1 = codecs.encode(codecs.decode(string1, 'hex'), 'base64').decode()
    decoded2 = codecs.encode(codecs.decode(string2, 'hex'), 'base64').decode()

    xored = ord(a) ^ ord(b) for a,b in zip(decoded1, decoded2)

    print(xored)
    return xored



xorcombination('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965')