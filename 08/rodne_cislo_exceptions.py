while 1 == 1:
    number = input("Enter your birth number: ")
    number_digits = (number.replace('/',''))
    try:
        if len(number) != 11:
            print('Number has insufficient length.')
            continue
        elif number[6] != '/':
            print('Slash is missing on 7th position.')
            continue
        elif int(number_digits) % 11 != 0:
            print('Number is not divisible by 11.')
            continue
    except ValueError:
        print('Entered input is not number, try again.')
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
