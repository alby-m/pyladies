first_number = int(input("Select first number: "))
second_number = int(input("Select second number: "))
symbol = input("Enter symbol: ")
calculation = '{} {} {}' .format(first_number, symbol, second_number)

if symbol == '+':
    result = (first_number + second_number)
elif symbol == '-':
    result = (first_number - second_number)
elif symbol == '*':
    result = (first_number * second_number)
elif symbol == '/':
    result = (first_number / second_number)

print(calculation, '=', result)

#print(eval('2+3'))
#print(eval('{} {} {}' .format(first_number, symbol, second_number)))
#print(eval(eval('calculation')))
#print(eval(calculation))


