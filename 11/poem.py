# file_ = open('poem.txt', encoding='utf-8')
# content = file_.read()
# file_.close()

# print(content)

# with open('poem.txt', encoding='utf-8') as file_: # v tele je subor otvoreny ale ako nahle sa posuniem z neho von, subor sa automaticky zatvori bez nutnosti zavolat metodu close 
#     content = file_.read()

# print(content)

# print('I heard this poem:')
# print()

# with open('poem.txt', encoding='utf-8') as file_:
#     for line in file_:
#         line = line.rstrip()
#         print('    ' + line)

# print()
# print('Do you like it?')

with open('second-poem.txt', mode='w', encoding='utf-8') as file_:
    print('Nase stare hodiny', file=file_)
    print('Biji', 2+2, 'hodiny', file=file_)

with open('second-poem.txt', encoding='utf-8') as file_:
    content = file_.read()
print(content)