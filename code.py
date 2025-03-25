ffrom adafruit_circuitplayground import cp
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

def askColour():
    while True:
        try:
            color = input('pick a colour to display the morse code in. input 3 numbers for rgb sperated by a space \n')
            
            colors = color.split()

            cp.pixels.fill((int(colors[0]),int(colors[1]),int(colors[2])))
            cp.pixels.fill((0,0,0))
            return (int(colors[0]),int(colors[1]),int(colors[2]))
        except:
          print('That is an invalid color')

def askTime():
    try:
        timing = float(input('input the time between words in milliseconds. eg 100 = 100ms \n'))/1000
        time.sleep(timing)
        return timing
    except:
       print('that was not a valid number')

def displayPixels(colors,timing):
    cp.pixels.fill(colors)
    time.sleep(timing)
    cp.pixels.fill((0,0,0))

def displayMorse(morse):
    cp.pixels.brightness = 0.03
    colors = askColour()
    timing = askTime()/3

    print(f'The message in morse is {morse}')
    print(f'The color is {colors}')
    print(f'The timing per dot is{timing}s ({timing*3}s/3)')

    for char in morse:
        if char == ' ':
            displayPixels((0,0,0),timing*3)
        elif char == '/':
           displayPixels((0,0,0),timing*7)
        elif char == '.':
           displayPixels(colors,timing)
        elif char == '-':
           displayPixels(colors,timing*2)


displayMorse(convertToMorse(userInput()))