def length(number):
    if len(number) == 11:
        return 'Entered number has 11 characters.'
    else:
        return 'Entered number has not 11 characters.'

def format(number):
    if number_digits.isnumeric():
        return 'Entered number includes 10 numbers.'
    else:
        return 'Entered number does not include 10 numbers.'

def slash(number):
    if number[6] == '/':
        return 'Entered number includes slash on 7th position.'
    else:
        return 'Entered number does not include slash on 7th position.'
            
def division(number):
    if int(number_digits) % 11 == 0:
        return 'Entered number is divisible by 11.'
    else:
        return 'Entered number is not divisible by 11.'


number = input("Enter your birth number: ")
number_digits = (number.replace('/',''))

print(length(number))
print(format(number))
print(slash(number))
print(division(number))

