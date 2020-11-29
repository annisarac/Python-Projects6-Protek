buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def beliBuah(buahBuahan):
    namaBuah = list(buahBuahan.keys())
    hargaBuah = tuple(buahBuahan.values())
    
    dataBuah = []
    while True :
        try:
            beli = input('Nama buah yang di beli : ')
            if(beli in buah.keys()):
                banyak = int(input('Berapa kg : '))
                urutan = namaBuah.index(beli)
                harga = hargaBuah[urutan] * banyak
                dataBuah.append(harga)
            else:
                print('Maaf, buah yang anda masukan tidak ada')
                continue

            lagi = input('Beli buah yang lain (y/n) ? ')
            if lagi == 'y':
                continue
            elif lagi == 'n':
                break
            else:
                print('inputan valid')
                continue

        except ValueError:
            print('Silahkan masukan jumlah dengan benar')
            continue
        
    print('----------------------------------')

    hargaDua = sum(dataBuah)
    print('Total harga : ' , hargaDua)

beliBuah(buah)
