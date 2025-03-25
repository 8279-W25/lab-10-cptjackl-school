import time

morseDict = {
    'a': '. -',
    'b': '- . . .',
    'c': '- . - .',
    'd': '- . .',
    'e': '.',
    'f': '. . - .',
    'g': '- - .',
    'h': '. . . .',
    'i': '. .',
    'j': '. - - -',
    'k': '- . -',
    'l': '. - . .',
    'm': '- -',
    'n': '- .',
    'o': '- - -',
    'p': '. - - .',
    'q': '- - . -',
    'r': '. - .',
    's': '. . .',
    't': '-',
    'u': '. . -',
    'v': '. . . -',
    'w': '. - -',
    'x': '- . . -',
    'y': '- . - -',
    'z': '- - . .',
    '0': '- - - - -',
    '1': '. - - - -',
    '2': '. . - - -',
    '3': '. . . - -',
    '4': '. . . . -',
    '5': '. . . . .',
    '6': '- . . . .',
    '7': '- - . . .',
    '8': '- - - . .',
    '9': '- - - - .'
}

def userInput():
   message = input('input a message \n').lower()
   clean_message = ''

   for letter in message:
    if letter in morseDict or letter==' ':
        clean_message = clean_message + letter

   return clean_message.split()


def convertToMorse(message):
   morse = ''

   for word in message:
    for letter in word:
        morse = morse + morseDict[letter] + '   '
    morse = morse + '/'

    return morse




print(convertToMorse(userInput()))
