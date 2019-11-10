plaintext = input('Enter message to encode: ')
key = input('Select key: ')

while not key.isdigit():
    print('Select number.')
    key = input('Select key: ')
    continue

work_text = []
for letter in plaintext:
    work_text.append(ord(letter))

ciphertext = []
for p in work_text:
    if (p > 96 and p < 123):
        ci = ((p-97) + int(key))%26 + 97
        ciphertext.append(ci)
    elif (p > 64 and p < 91):
        ci = ((p-65) + int(key))%26 + 65
        ciphertext.append(ci)
    elif (p > 47 and p < 58):
        ci = ((p-48) + int(key))%26 + 48
        ciphertext.append(ci)
    else:
        ci = p
        ciphertext.append(ci)

solution = []
for s in ciphertext:
    solution.append(chr(s)) 

print(''.join(solution))

    

