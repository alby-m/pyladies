variable_1 = input('Pick the letter:')
if variable_1 == 'a':
    letter_a = True
else:
    letter_a = False

variable_2 = input('Pick the letter again:')
if variable_2 == 'b':
    letter_b = True
else:
    letter_b = False

if letter_a and letter_b:
    print(letter_a and letter_b)
elif letter_a or letter_b:
    print(letter_a or letter_b)
else:
    print('False')

