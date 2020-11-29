while True:
    try:
        data = int(input('Berapa banyak data angka yang akan anda masukan ?'))
        break
    except ValueError:
        print('Inputan vailid')
        continue
    
dataNilai = []
i = 1

while True:
    try :
        print('Masukan data angka ke- ' + str(i) + ' : ' )
        x = int(input())
        dataNilai.append(x)
        if i == data :
            break
        i = i + 1
    except ValueError:
        print('Inputan valid')
        
dataNilai.sort(reverse = True)
print(dataNilai)
