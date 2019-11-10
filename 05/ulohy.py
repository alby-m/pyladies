velikost = 11
nasobilka = []
for a in range(velikost):
    radek = []
    for b in range(velikost):
        radek.append(a * b)
    nasobilka.append(radek)

print(nasobilka[2][3])  # dva krát tři
print(nasobilka[5][2])  # pět krát dva
print(nasobilka[8][7])  # osm krát sedm

# Vypsání celé tabulky
for radek in nasobilka:
    for cislo in radek:
        print(cislo, end=' ')
    print()