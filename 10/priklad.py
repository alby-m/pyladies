print("Program zisti samohlasky v slovach.")

def vyhod_samohlasky(slovo):
    samohlasky = 'aeiouy'
    vystup = ''
    for znak in slovo:
        if not (znak in samohlasky):
            vystup += znak
    return vystup

slovo = input("Zadaj slova: ")
print(vyhod_samohlasky(slovo))