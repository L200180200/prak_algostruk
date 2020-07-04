from Latoop3 import *
class Mahasiswa(Manusia):
	"""docstring for Mahasiswa"""
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

	def ambilNama(self):
		return self.nama
	def ambilnim(self):
		return self.nim
	def ambilsaku(self):
		return self.saku
	def ambilKota(self):
		return self.kota
	def makan(self, m):
		print ("Saya baru saja makan ",m,"Sambil Balap f1. ")
		self.keadaan = 'kenyang'
	def perbaruiKota(self, p):
		self.kota = p
	def tambahsangu(self, i):
		self.saku = self.saku + i
	listkuliah = []
	def ambilkuliah(self,kuliah):
		self.listkuliah.append(kuliah)
	def kurangikuliah(self, kuliah):
		self.listkuliah.remove(kuliah)

a = Mahasiswa('fadhil',200,'Solo',2500000)
print(a.nama)

print ('Nama: ')
nama = input()
print ('NIM: ')
nim = input()
nim = int(nim)
print ('Kota: ')
kota = input()
print ('Uang Saku: ')
saku = input()
saku = int(saku)

mhsbaru = Mahasiswa(nama, nim, kota, saku)








		
		
	
	
