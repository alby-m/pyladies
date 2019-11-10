from random import randrange

def game(person):
    cube = randrange(6) + 1
    counter = 0
    while cube != 6:
        print('Person',person,'threw',cube)        
        cube = randrange(6) + 1
        counter = counter + 1
    print('Person',person,'threw',cube,',person threw',str(counter+1),'times to reach 6.')
    return (counter + 1)

# count_0 = (game(0))
# count_1 = (game(1))
# count_2 = (game(2))

# if count_0 >= count_1 and count_0 >= count_2:
#     print('Player 0 won.')
# if count_1 >= count_2 and count_1 > count_0:
#     print('Player 1 won.')
# if count_2 > count_1 and count_2 > count_0:
#     print('Player 2 won.')

list = []

for i in range(3):
    list.append(game(i))

maximum_count = max(list)

for j, val in enumerate(list):
    if val == maximum_count:
        print(j)
        break
    
    