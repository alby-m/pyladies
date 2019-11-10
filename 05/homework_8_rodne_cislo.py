while 1==1:
    number = input("Enter your birth number: ")
    number_digits = (number.replace('/',''))
    number_1 = number_digits[:6]
    number_2 = number_digits[6:]
    if len(number) != 11:
        print('Your number does not have required number of characters, try again.')
        continue
    elif not number_1.isnumeric():
        print('Your number does not include required characters, try again.')
        continue
    elif not number_2.isnumeric():
        print('Your number does not include required characters, try again.') 
        continue
    elif number[6] != '/':
        print('Your number is missing "/" on 7th position, try again.')
        continue
    elif int(number_digits) % 11 != 0:
        print('Your number is not divisible by 11, try again.')
        continue
    else:
        break 

print(number,'is correct birth number.')