import drawing, util_word, empty_field, replacement

underscores = empty_field.blank(util_word.word_pc)
print(' '.join(underscores))

failed_attempt = 0
word_letters = list(util_word.word_pc)

while underscores.count('_') > 0 and failed_attempt <= 9:
    letter = input('Pick a letter: ')
    if letter in word_letters:
        underscores = replacement.new_field(letter, word_letters, underscores)
    else:
        failed_attempt = failed_attempt + 1 
    print(drawing.drawings[failed_attempt])
    print(' '.join(underscores))

if underscores.count('_') == 0:
    print('You won.')
else:
    print('You lost.')


    


