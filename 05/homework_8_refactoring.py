def length(number):
    if len(number) == 11:
        return True
    else:
        return False

def format(number):
    if number_digits.isnumeric():
        return True
    else:
        return False

def slash(number):
    if number[6] == '/':
        return True
    else:
        return False
            
def division(number):
    if int(number_digits) % 11 == 0:
        return True
    else:
        return False


number = input("Enter your birth number: ")
number_digits = (number.replace('/',''))

print(length(number))
print(format(number))
print(slash(number))
print(division(number))

