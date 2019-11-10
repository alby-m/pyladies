#Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vypíše True nebo False)
while 1==1:
    number = input("Enter your birth number: ")
    number_digits = (number.replace('/',''))
    if len(number) != 11:
        print(False)
        continue
    elif not number_digits.isnumeric():
        print(False)
        continue
    elif number[6] != '/':
        print(False)
        continue
    elif int(number_digits) % 11 != 0:
        print(False)
    else:
        print(True)
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

  


#number of charactes is 11
#possible to divide by 11, modulo 11
#what is the date of the birth encoded in, year is 19+first two letters, month i
#what is the sex encoded in 
#Druhé dvojčíslí vyjadřuje měsíc narození, u žen zvýšené o 50, třetí dvojčíslí vyjadřuje den narození