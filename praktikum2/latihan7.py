buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def mahal(dictionary):
    key = list(dictionary.keys())
    values = tuple(dictionary.values())

    hargaTermahal = max(values)
    print(hargaTermahal)
    Harga = values.index(hargaTermahal)

    print(key[Harga])
mahal(buah)
