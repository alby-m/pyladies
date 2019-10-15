from random import randint
number_of_points = 0
user_move = input('Do you want a card? Write "YES" or "NO" .')

while user_move == 'YES':
    card = randint(2,10)
    number_of_points = number_of_points + card
    print('Your card has value', card, 'points.')
    if number_of_points > 21:
        print("You lost with", number_of_points, 'points.')
        break
    print('You have', number_of_points, 'points.')
    user_move = input('Do you want another card? Write YES or NO. ')

if user_move == 'NO':
    print('You finished with', number_of_points, 'points.')
elif user_move != 'YES':
    print('I do not understand.')

