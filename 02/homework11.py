a = input("Zadaj a:")
b = input("Zadaj b:")
sedi_to = a == b
nesedi_to = a != b
if sedi_to:
    print("a je rovnake ako b")
elif nesedi_to:
    print("a a b maju svoje odlisnosti")
print("Dokazem porovnavat pomocou IF. Cool.")