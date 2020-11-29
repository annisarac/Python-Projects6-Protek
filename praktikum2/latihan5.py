def kuadrat(bill):
    data = []
    for i in range (len(bill)):
        hitung = bill[i]**2
        data = data + [hitung]
    return data

bill = [2, 5, 6, 4]
print(kuadrat(bill))
