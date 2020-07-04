class Pesan(object):
	"""docstring for Pesan"""
	def __init__(self, string):
		self.string = string
	def cetakIni(self):
		print (self.string)
	def kapital(self):
		print (str.upper(self.string))
	def lower(self):
		print (str.lower(self.string))
	def jumKar(self):
		return len(self.string)
	def cetakjumkar(self):
		print ('kalimat', len(self.string),' karakter')
	def perbarui(self, stringbaru):
		self.string = stringbaru
	def apakahTerkandung(self, x):
		if x in self.string:
			print ('true')
		else:
			print ('false')
	def vokal(self):
		hvokal=['a','i','u','e','o','A','I','U','E','O']
		count=0
		for i in self.string:
			if i in hvokal:
				count+=1
		return (count)
	
	def konsonan(self):
		hvokal=['a','i','u','e','o','A','I','U','E','O']
		count=0
		for i in self.string:
			if i not in hvokal:
				count+=1
		return (count)
                
                
                
			
		
        
	
