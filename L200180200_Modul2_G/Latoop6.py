from Latoop4 import *
class MhsTIF(Mahasiswa):
	def __init__(self, nama, nim, kota, saku):
		self.nama = nama
		self.nim = nim
		self.kota = kota 
		self.saku = saku
	def __str__(self):
	 	s = self.nama + ', NIM' + str(self.nim) \
	 		+ '. Tinggal di ' + self.kota \
	 		+ '. Uang Saku RP ' + self.saku \
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
	def hapuskuliah(self, kuliah):
		self.listkuliah.append(kuliah)
	def katakanpy(self):
		print('Pyhon is cool')
		
	
       
