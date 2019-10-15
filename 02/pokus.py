#toto je kombinacia prikladu 8 a 9
#pri porovnavani je potreba zadat vzdy 2= nie len jedno, inak if nevie co ma porovnat
from random import randrange
cislo = randrange (3)
print(cislo)
if cislo == 0:
    print("kamen")
elif cislo == 1:
    print("noznice")
else:
    print("papier")