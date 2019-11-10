def evaluate(game):
    if 'xxx' in game:
        print('Player with "x" has won.')
    elif 'ooo' in game:
        print('Player with "o" has won.')
    elif '-' not in game:
        print('It is a tie.')
    else:
        print('Game is not finished yet.')
    return

evaluate('ooxxxoxxooxxooxx')