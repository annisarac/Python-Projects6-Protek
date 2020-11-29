def dataStat (x):
    dataTuple = tuple(x)

    a = sum(x)/len(x)
    b = max(dataTuple)
    c = min(dataTuple)

    datax = [a, b, c]
    
    return datax

while True:
    try:
        data = int(input('Masukan berapa banyak data angka yang ingin anda masukan(harus berupa angka) : '))
        break
    except ValueError:
        print('Inputan vailid')
        continue

dataNilai = []
i = 1

while True:
    try:
        print('Masukan bilangan bulat ke - ' + str(i) + ' : ' )
        x = int(input())
        dataNilai.append(x)
        if i == data :
            break
        i = i + 1

    except ValueError:
        print('Inputan valid')

urutan = dataStat(dataNilai)
print(urutan)

    
    
    
    
