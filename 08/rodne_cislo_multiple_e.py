while 1 == 1:
    number = input("Enter your birth number: ")
    try:
        number_digits = int(number.replace('/',''))
    except ValueError:
        print('Entered input is not number, try again.')
        continue
    try:
        if len(number) != 11:
            raise IndexError
    except IndexError:
        print('Number has not correct length.')
        continue      
    try:
        if number[6] != '/':
            raise TypeError
    except TypeError:
        print('Slash is missing on 7th position.')
        continue
    try:
        if number_digits % 11 != 0:
            raise ValueError
    except ValueError:
        print('Number is not divisible by 11.')
        continue
    else:
        print('Entered number is valid.')
        break

day = number[4:6]
month_characters = number[2:4]
month_int = int(month_characters)
month = month_int%50

year = number[:2]
print('Date of birth is',day+'.'+str(month)+'.'+year)

if month_int > 12:
    print('The sex is female.')
else:
    print('The sex is male.')
