import drawing, util_word, empty_field, replacement
# Modules import

underscores = empty_field.blank(util_word.word_pc)
print(' '.join(underscores))
# Creating field for game with number of empty spaces corresponding to number of characters in selected word

failed_attempt = 0
#Number of failed attempt of guessing a letter when the game starts
word_letters = list(util_word.word_pc)
# Transforming randomly selected word in the list of its characters

while underscores.count('_') > 0 and failed_attempt <= 9: 
#This condition describes a state when game is not finshed
    letter = input('Pick a letter: ') #User's guest 
    if letter in word_letters:
        underscores = replacement.new_field(letter, word_letters, underscores)
        #When the guess is correct, program will replace empty space with the letter
    else:
        failed_attempt = failed_attempt + 1 
        #When the guess is incorrect, program will raise number of failed attempts
    print(drawing.drawings[failed_attempt])
    #Program will draw a picture of hangman corresponsing to current number of failed attempts
    print(' '.join(underscores))
    #Field with empty spaces and already correctly guessed letters will be written after every guess

if underscores.count('_') == 0:
    print('You won.')
    #Condition is met when all the empty spaces are replaced and number of failed attempts is not bigger than 9
else:
    print('You lost.')
    #Condition is met when number of failed attempts is bigger than 9


    


