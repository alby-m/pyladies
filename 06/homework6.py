def man_woman(question):
    answer = input(question)
    answer = answer[-1]
    if answer == 'a' or answer == 'á':
        return True
    else:
        return False

if man_woman('Write your surname: '):
    print('Woman.')
else:
    print('Man.')