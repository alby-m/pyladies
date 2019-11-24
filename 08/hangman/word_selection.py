#Function will randomly choose a word from the list and return it
import random

def select():
    word_list = ['sunday', 'flower', 'garden', 'rock', 'house', 'apple', 'banana']
    word = random.choice(word_list)
    return word