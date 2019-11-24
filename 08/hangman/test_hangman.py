import random, word_selection, empty_field, replacement

def test_select():
    word =  word_selection.select()
    assert word in ['sunday', 'flower', 'garden', 'rock', 'house', 'apple', 'banana']
    #test for random choice of word from the list


def test_blank():
    field = empty_field.blank('example')
    assert len(field) == 7
    assert field.count('_') == 7
    #test for creation of empty field containing number of underscores corresponding to number of characters

def test_new_field():
    field = replacement.new_field('a', ['c', 'a', 'r'], ['_', '_', '_'])
    assert field[1] == 'a'
    assert len(field) == 3
    assert field.count('_') == 2
    #test for replacement of underscore with letter 'a' from the word 'car'
    field = replacement.new_field('a', ['b', 'a', 'n', 'a', 'n', 'a'], ['_', '_', '_', '_', '_', '_'])
    assert field[1] == 'a' and field[3] == 'a' and field[5] == 'a'
    assert len(field) == 6
    assert field.count('_') == 3
    assert field[1] != 'b'
    #test for replacement of all corrensponsing underscores with letter 'a' from the word 'banana'




