import random, word_selection, empty_field, replacement

def test_select():
    word =  word_selection.select()
    assert word in ['sunday', 'flower', 'garden', 'rock', 'house']

def test_blank():
    field = empty_field.blank('example')
    assert len(field) == 7
    assert field.count('_') == 7

def test_new_field():
    field = replacement.new_field('a', ['c', 'a', 'r'], ['_', '_', '_'])
    assert field[1] == 'a'
    assert len(field) == 3
    assert field.count('_') == 2


