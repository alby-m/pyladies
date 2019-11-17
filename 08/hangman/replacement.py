def new_field(letter, word_letters, underscores):
    position = word_letters.index(letter)
    underscores[position] = letter
    return underscores