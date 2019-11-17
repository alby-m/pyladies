from util_word import word_pc

def blank(word_pc):
    underscore_list = []
    for i in range(len(word_pc)):
        underscore_list.append('_')
    return underscore_list

print(blank('rock'))
