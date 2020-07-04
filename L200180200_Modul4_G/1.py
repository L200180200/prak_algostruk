class mhsTif(object):
	"""docstring for mhsTif"""
	def __init__(self, nama, nim, kota, saku):
		self.nama = nama
		self.nim = nim
		self.kota = kota
		self.saku = saku
	def __str__(self):
	 	s = self.nama + ', NIM' + str(self.nim) \
	 		+ '. Tinggal di ' + self.kota \
	 		+ '. Uang Saku RP ' + str(self.saku) \
	 		+ ' tiap bulan. '
	 	return s
c0 = mhsTif('ika', 100, 'sukoharjo', 290000)
c1 = mhsTif('ikal', 180, 'solo', 299000)
c2 = mhsTif('ahmad', 230, 'solotigo', 2900800)
c3 = mhsTif('fadhil', 200, 'solo', 7000)
daftar = [c0, c1, c2, c3]
daftar1 = [1,2,3,4,5,6,7,8,9]
daftar2 = [1,2,3,4,5,6,7,8,9,9,9]
target = 'solotigo'
for i in daftar:
	if i.kota == target:
		print(i.nama + ' tinggal di ' +target )
#No.1
def pencarian(list, target):
	hasil = []
	for i in list:
		if i.kota == target:
			hasil.append(list.index(i))
	print(hasil)
#No.2
def sakuTerkecil(list):
        terkecil = 9999999
        for i in list:
                if i.saku < terkecil:
                        terkecil = i.saku
        return terkecil
#No.3
def sakuTerkecilObj(obj):
        temp = [obj[0]]
        for i in obj:
                if i.saku < temp[0].saku:
                        temp = [i]
                elif i.saku == temp[0].saku:
                        temp.append(i)
        return temp
#No.4
def uangKurang(o):
        temp = []
        for i in o:
                if i.saku < 250000:
                        temp.append(i)
        return temp

#No.5
def Linsearch(data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

#No.6
def binSe(kumpulan,target):
    low = 0
    high = len(kumpulan) - 1
    #print(len(kumpulan))

    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

#No.7
def binSes(kumpulan,target):
    low = 0
    high = len(kumpulan) - 1
    listt = []
    #print(len(kumpulan))
    while low < high:
        if kumpulan[low] == target:
            listt.append(low)
            low+=1
        else:
            low+=1
    return listt



