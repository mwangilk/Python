# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.
    shift: 0 <= int < 26
    returns: dict
    """
    result = {}
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    for letter in upper:
        result[letter] = upper[(upper.index(letter) + shift) % 26]
    for letter in lower:
        result[letter] = lower[(lower.index(letter) + shift) % 26]
    return result

## Result
# buildCoder(11)
# {'A': 'L', 'C': 'N', 'B': 'M', 'E': 'P', 'D': 'O', 'G': 'R', 'F': 'Q', 
# 'I': 'T', 'H': 'S', 'K': 'V', 'J': 'U', 'M': 'X', 'L': 'W', 'O': 'Z', 
# 'N': 'Y', 'Q': 'B', 'P': 'A', 'S': 'D', 'R': 'C', 'U': 'F', 'T': 'E', 
# 'W': 'H', 'V': 'G', 'Y': 'J', 'X': 'I', 'Z': 'K', 'a': 'l', 'c': 'n', 
# 'b': 'm', 'e': 'p', 'd': 'o', 'g': 'r', 'f': 'q', 'i': 't', 'h': 's', 
# 'k': 'v', 'j': 'u', 'm': 'x', 'l': 'w', 'o': 'z', 'n': 'y', 'q': 'b', 
# 'p': 'a', 's': 'd', 'r': 'c', 'u': 'f', 't': 'e', 'w': 'h', 'v': 'g', 
# 'y': 'j', 'x': 'i', 'z': 'k'}

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.
    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    cipher = str()
    for i in text:
        if i not in string.ascii_uppercase and i not in string.ascii_lowercase:
            cipher += i
        else:
            cipher += coder[i]
    return cipher

## Result
# applyCoder('Hello, world!', buildCoder(11))
# 'Spwwz, hzcwo!'

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))
    
## Result
# applyShift('mebgqfkwsjpvuy', 11)
# 'xpmrbqvhduagfj'

#
# Problem 2: Decryption
#
wordList = loadWords()
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    text: string
    returns: 0 <= int < 26
    """
    realWords = 0
    bestShift = 0
    for p in string.punctuation:
        text = text.replace(p, '')
    for shift in range(0, 26):
        textList = applyShift(text, shift).split()
        validWords = 0
        for word in textList:
            if word in wordList:
                validWords += 1
            if validWords > realWords:
                realWords = validWords
                bestShift = shift
    return bestShift

## Result
# findBestShift(wordList, 'Vw, jcb bPMzm qa i BI viumL Itdqv!')
# 18

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.
    returns: string - story in plain text
    """
    story = getStoryString()
    wordList = loadWords()
    bestShift = findBestShift(wordList, story)
    return applyShift(story, bestShift)

#

if __name__ == '__main__':
    wordList = loadWords()
    decryptStory()

s = 'Pmttw, ewztl!'
print findBestShift(wordList, s)

print decryptStory()
