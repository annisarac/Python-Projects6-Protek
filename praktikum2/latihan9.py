buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def beliBuah(buahBuahan):
    namaBuah = list(buahBuahan.keys())
    hargaBuah = tuple(buahBuahan.values())

    beli = input('Nama buah yang di beli : ')
    banyak = int(input('Berapa kg : '))
    print('----------------------------------')

    urutan = namaBuah.index(beli)
    harga = hargaBuah[urutan] * banyak
    print('Total harga : ' , harga)

beliBuah(buah)


