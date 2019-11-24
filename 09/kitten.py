class Kitten: #trieda / trieda je predpis 
    def meow(self): #trieda ma jednu metodu, metodu meow// atribut/parameter self
        print("Meow!") #metoda robi jednu vec, printuje Meow

kitten = Kitten() #tvorba objektu(instance) kitten v triede Kitten 

kitten.meow() #volani metody na objekte 

mourek = Kitten() #tvorba objektu mourek v triede Kitten 
mourek.name = 'Mourek' #priradenie atributu name objektu mourek a hodnoty k tomu "Mourek"

micka = Kitten()
micka.name = 'Micka'

print(mourek.name)
print(micka.name)