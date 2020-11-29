dataNama = []
i = 1

while True :
    print('Masukan nama mahasiswa ke- ' + str(i) + ' : ' )
    x = str(input())
    dataNama.append(x)
    lanjut = str(input('Masuka nama lagi ? (y/n): ' ))
    if lanjut == 'y' :
        True
    elif lanjut == 'n' :
        break
    else :
        print('Inputan valid')
    i = i + 1

dataNama.sort()

for x in range(len(dataNama)):
    print(dataNama[x], '(', len(dataNama[x]), 'Karakter )')
