animals = ['dog', 'cat', 'elephant', 'snake', 'bird']
second_letter = []
sorted_list = []

for animal in animals:
    second_letter.append(animal[1])

pairs = zip(second_letter, animals)
pairs_transf = dict(pairs)

sorted_pairs = sorted(pairs_transf.items())

for animal2 in sorted_pairs:
    sorted_list.append(animal2[1])

print(sorted_list)


