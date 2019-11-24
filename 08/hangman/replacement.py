#Function will replace underscore/s in the field with correctly guessed letter corresponding to its position/s in the word

def new_field(letter, word_letters, underscores):
    for i in range(len(word_letters)):
        if letter == word_letters[i]:
            underscores[i] = letter
            #Replacement of the underscore with the letter
    return underscores
    #New field with already replaced underscore 
