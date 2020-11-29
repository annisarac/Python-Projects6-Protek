nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80}, 	      {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	      {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
def nilaiTertinggi(namaMhs):

    mid = []
    uas = []
    nilaiAkhir = []
    tertinggi = []

    for i in namaMhs:
        rumus = (i['mid'] + (2* i ['uas']))/3
        nilaiAkhir.append(rumus)

    tertinggi = nilaiAkhir.index(max(nilaiAkhir))

    data = {'nim' : namaMhs[tertinggi]['nim'], 'nama' : namaMhs[tertinggi]['nama']}

    return data

a = nilaiTertinggi(nilaiMhs)
print('Mahasiswa dengan nilai tertinggi adalah ' , a['nama'] , 'NIM' , a['nim'])
