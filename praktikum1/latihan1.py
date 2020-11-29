a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#2. Sisipkan nilai di indeks ke 3 dari a & 2 dari b
a.insert(3 , 10)
print(a)
b.insert(2 , 15)
print(b)

#3. Sisipkan nilai di indeks terakhir dari a & b
a = a + [4]
print(a)

b = b + [8]
print(b)

#4. Sorting secara ascending pada a & b
a.sort()
print(a)

b.sort()
print(b)

#5. list c & list d
c = a[0 : 7]
print(c)

d = b [2 : 9]
print(d)

#6
e = []
for i in range(len(c)):
    jumlah = c[i] + d[i]
    e = e + [jumlah]

print (e)

#7 tuple

myTuple = tuple(e)
print (myTuple)

#8 min, maks, dan jumlah
#max
print(max(myTuple))

#min
print(min(myTuple))

#jumlah
print(sum(myTuple))


