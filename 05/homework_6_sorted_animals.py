animals = ['dog', 'cat', 'elephant', 'snake', 'bird']
second_letter = []
pairs = []
sorted_list = []

for animal in animals:
    second_letter.append(animal[1:])

for a, b in zip(second_letter, animals):
    pairs.append([a, b])

sorted_pairs = sorted(pairs)

for s in sorted_pairs:
    sorted_list.append(s[1])

print(sorted_list)



# test_list = [['bca', 'abc'], ['abc', 'cab']]
# print(test_list)
# print(sorted(test_list))