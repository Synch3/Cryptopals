#This challenge is converting hex to base 64.

# The string:

#49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

# Should produce:

# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

import codecs

def hexto64(string):
    thefinalactualstring = codecs.encode(codecs.decode(string, 'hex'), 'base64').decode()
    print(thefinalactualstring)
    return thefinalactualstring

hexto64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')