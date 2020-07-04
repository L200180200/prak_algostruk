#No.6
lower = 2   
upper = 1000
print("Bilangan prima dari",lower,"sampai",upper,":")
for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

#No.7
def faktorPrima(x): 
    a = []
    b = []
    hasil = 0
    bil = x
    prima =True
    for i in range(2,x):
        prima = True
        for u in range(2, i):
            if i % u == 0:
               prima = False
        if prima:
            a.append(i)
    idx = 0
    while bil > 1:
        try:
            if (bil%a[idx]) == 0:
                hasil = bil/a[idx]
                bil = hasil
                b.append(a[idx])
            else:
                idx = idx + 1
        except IndexError:
            break
    print (b)

#No.8
def apakahTerkandung(x,y):  
    a = True
    for i in range(len(y)):
        if x in y:
            a = True
        else:
            a = False
    return a

#No.9
def mencetak(a):        
    for i in range(a):
        if(i<=0):
            pass
        elif(i%3==0 and i%5==0):
            print("Python UMS")
        elif(i%3==0):
            print("Python")
        elif(i%5==0):
            print("UMS")
        else:
            print(i)

#No.10
from math import sqrt as detr
def selesaikanABC(a,b,c):       
    a = float(a)
    b = float(b)
    c = float(c)
    D = float(b*2 - 4*a*c)
    if(D<0):
        hasil = "Determinan negatif, persamaan tidak mempunyai akar real"
        return hasil
    else:
        x1 = (-b+detr(D))/(2*a)
        x2 = (-b+detr(D))/(2*a)
        return hasil




