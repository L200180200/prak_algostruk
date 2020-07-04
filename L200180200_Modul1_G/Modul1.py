#No.1
def cetaksiku(x):  
	str = ""
	baris = 1
        # Looping Baris
	while baris <=x:
		kolom = baris
		while kolom > 0 :
			str = str + "*"
			kolom = kolom - 1
		str = str + "\n"
		baris = baris + 1
	print (str)
cetaksiku(5)

#No.2
def persegipanjantg(x,y):  
	for i in range(x):
		if i == 0 or i == x - 1:
		     print ("@" * y)
		else :
		     print ("@"+" "*(y-2)+"@")
persegipanjantg(4,5)

#No.3a
def vokal(x):  

        hvokal=['a','i','u','e','o','A','I','U','E','O']
        hitung=0
        b = len(x)
        for i in x:
                if i in hvokal:
                        hitung+=1
        return (b,hitung)

#No.3b
def konsonan(x):  

        hvokal=['a','i','u','e','o','A','I','U','E','O']
        hitung=0
        b = len(x)
        for i in x:
                if i not in hvokal:
                        hitung+=1
        return (b,hitung)
#No.4
def rata(x):    
    jmlX = 0
    for i in x:
        jmlX += i
    hasil = jmlX/len(x)
    print(hasil)
rata([1,2,3,4,4,3,5])

#No.5
from math import sqrt as sq     
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if (n % i) == 0:
                print (n,"bukan bilangan prima")
                break
            else:
                print (n,"bilangan prima")

print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))



































