strana = float(input("Zadaj stranu stvorca v cm:"))
strana_je_spravne = strana > 0
if strana_je_spravne:
    print("Obvod stvorca so stranou", strana, "cm je", 4*strana, "cm.")
    print("Obsah stvorca so stranou", strana, "cm je", strana*strana, "cm2.")
else:
    print("Zadaj kladne cislo.")