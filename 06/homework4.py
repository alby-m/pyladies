from random import randrange
pc_turn = randrange (3)
#0 represents rock, 1 represents scissors, 2 represents paper
human_turn = input('rock, scissors, or paper? ')

while human_turn != 'end':
    if pc_turn == 0:
        print('PC has picked the rock.')
    elif pc_turn == 1:
        print('PC has picked the scissors.')
    elif pc_turn == 2:
        print('PC has picked the paper.')

    if   (human_turn == 'rock' and pc_turn == 0) or (human_turn == 'scissors' and pc_turn == 1) or (human_turn == 'paper' and pc_turn == 2):
        print('Draw.')
    elif (human_turn == 'rock' and pc_turn == 2) or (human_turn == 'scissors' and pc_turn == 0) or (human_turn == 'paper' and pc_turn == 1):
        print('PC wins.')
    elif (human_turn == 'rock' and pc_turn == 1) or (human_turn == 'scissors' and pc_turn == 2) or (human_turn == 'paper' and pc_turn == 0):
        print('Human wins.')
    else:
        print('I do not understand.')
    
    human_turn = input('rock, scissors, or paper? ')

print('Game over.')