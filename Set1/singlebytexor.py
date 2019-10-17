#  The hex encoded string:

# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

# ... has been XOR'd against a single character. Find the key, decrypt the message.

# You can do this by hand. But don't: write code to do it for you.

# How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score. 

import binascii

def singlebytexor(code):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pointarray = []
    for letter in LETTERS:
        print(letter)
        xoredstring = str(int(code, 16) ^ int(hex(ord(letter)), 16))
        print(xoredstring)
        pointarray.append(scoring(xoredstring))
    print(pointarray, 'pointarray')
    return pointarray


def scoring(message):
    ETAOIN = 'ETAOINSHRDLUCMWFGYPBVKJXQZ'
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] +=1

    frequency = {}
    for letter, number in letterCount.items():
        frequency[number] = frequency.get(number, [])
        frequency[number].append(letter)

    freqPairs = list(frequency.items())
    freqPairs.sort(reverse=True)
    stringOrder = []
    for freqPair in freqPairs:
        stringOrder.append(freqPair[1])
    
    stringJoined = [item for sublist in stringOrder for item in sublist]
    print ('stringjoined', stringJoined)
    stringJoined = ''.join(stringJoined)

    points = 0
    for commonLetter in ETAOIN[:6]:
        if commonLetter in stringJoined[:6]:
            points += 1
    
    for blehletter in ETAOIN[-6:]:
        if blehletter in stringJoined[-6:]:
            points += 1
    
    print(points)
    return points


singlebytexor('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')