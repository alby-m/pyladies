#Function creates field containting number of underscores (representing empty spaces for letters)
#corresponding to number of characters in selected word
def blank(word_pc):
    underscore_list = []
    for i in range(len(word_pc)):
        underscore_list.append('_')
    return underscore_list
