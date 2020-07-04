class Manusia(object):
	"""docstring for Manusia"""
	keadaan = 'lapar'
	def __init__(self, nama):
		self.nama = nama
	def ucapSalam(self):
		print ("Salam", self.nama)
	def makan(self, m):
		print ("Saya baru makan ", m)
		self.keadaan = 'kenyang'
	def olahraga(self, o):
		print ("Saya baru saja olahraga", o)
		self.keadaan = 'lapar'
	def mengalikan2(self, n):
		return n*2
p1 = Manusia('fadhil')
p1.ucapSalam()















		
		
