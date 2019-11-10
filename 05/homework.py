#selected_animal = input('Select animal: ')
animals_me = ['dog', 'cat', 'rabbit', 'snake']
animals_you = ['dog', 'horse', 'cow', 'snake']
animal_list_both = []
animal_list_only_me = []
animal_list_only_you = []

print(animals_me)
print(animals_you)

for animal_me in animals_me:
    for animal_you in animals_you:
        if animal_me == animal_you:
            animal_list_both.append(animal_me) 

print(animal_list_both)

for animal_me in animals_me:
    if animal_me not in animals_you:
        animal_list_only_me.append(animal_me)

print(animal_list_only_me)

for animal_you in animals_you:
    if animal_you not in animals_me:
        animal_list_only_you.append(animal_you)

print(animal_list_only_you)



#for animal in animals:
#    if len(animal) <= 5:
#        print(animal)

#for animal in animals:
#    if animal[0] == 'r':
#        print(animal)

#if selected_animal in animals:
 #   print(True)
    #print(selected_animal.capitalize(), 'is in the list.')
#else:
 #   print(False)
   # print(selected_animal.capitalize(),'is not in the list.')