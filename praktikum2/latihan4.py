print('----------------------------------')
print('PROGRAM MEMILIH DATA SAYUR')
print('----------------------------------')

print('Menu')
print('A = Tambah data sayur')
print('B = Hapus data sayur')
print('C = Tampilkan data sayur')
print('0 = keluar')

dataSayur =['bayam','kangkung','wortel','selad']
while True :
    try:
        pilih = str(input('Pilihan anda ? (masukan a/b/c/0) :'))
        if pilih == 'a' or pilih == 'A':
            tambah = str(input('Tambahkan data sayur : '))
            dataSayur.append(tambah)
        elif pilih == 'b' or pilih == 'B':
            hapus = str(input('Hapus data sayur : ' ))
            dataSayur.remove(hapus)
        elif pilih == 'c' or pilih == 'C':
            print(dataSayur)
        elif pilih == '0':
            break
            
        else:
            print('Inputan valid')
            break
    except ValueError :
        print('Sayur tidak di temukan')
