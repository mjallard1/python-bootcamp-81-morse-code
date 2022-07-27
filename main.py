MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

LETTER_SPACE = '   '
WORD_SPACE = '       '

string = input("Enter a text to translate to Morse Code: ").upper()

chars_in_word = []
words_in_string = []

for word in string.split():
  for char in word:
    chars_in_word.append(MORSE_CODE_DICT[char])
  result = LETTER_SPACE.join(chars_in_word)
  words_in_string.append(result)
  chars_in_word = []

code = WORD_SPACE.join(words_in_string)
print(f"Morse code: {code}")