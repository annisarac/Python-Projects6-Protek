print('----------------------------------')
print('PROGRAM DATA BUAH')
print('----------------------------------')

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
namaBuah = list(buah.keys())
hargaBuah = tuple(buah.values())
dataBuah = []

print('Menu')
print('A = Tambah data buah')
print('B = Beli buah')
print('C = Hapus data buah')
print('0 = keluar')

while True :
    try:
        pilih = str(input('Pilihan anda ? (masukan a/b/c/0) :'))
        if pilih == 'a' or pilih == 'A':
            tambah = str(input('Masukan nama buah : '))
            if (tambah in buah):
                print('Buah sudah terdaftar')
                tambah = str(input('Masukan nama buah : '))
            harga = int(input('Maukan harga satuan : '))
            buah[tambah] = harga
            print(buah)
            
        elif pilih == 'b' or pilih == 'B':
            while True :
                try:
                    beli = input('Nama buah yang di beli : ')
                    if(beli in buah.keys()):
                        banyak = int(input('Berapa kg : '))
                        urutan = namaBuah.index(beli)
                        hargaDua = hargaBuah[urutan] * banyak
                        dataBuah.append(hargaDua)
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
        elif pilih == 'c':
            hapus = input('Masukan nama buah yang ingin anda hapus :')
            if hapus not in buah:
                print('Nama buah tidak di temukan ')
                hapus = input('Masukan nama buah yang ingin anda hapus :')
            del buah[hapus]
            print(buah)
            
        elif pilih == '0':
            break
            
        else:
            print('Inputan valid')
            break
    except ValueError :
        print('buah tidak di temukan')
            
            
