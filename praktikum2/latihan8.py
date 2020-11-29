buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def rerata(buah):
    harga = list(buah.values())
    rataRata = sum(harga)/len(harga)
    return rataRata

print(rerata(buah))
