#No.11
def tahunKabisat(tahun):    
    hasil = False
    if(tahun%4==0 and tahun%100!=0 and tahun%400!=0):
        hasil = True
    elif(tahun%100==0 and tahun%400!=0):
        hasil = False
    elif(tahun%400==0):
        hasil = True
    else:
        hasil = False
    return hasil

#No.12
import random
def tebakAngka():       
    a = random.randrange(1,101,1)
    b = -1
    n = 0
    print("Permainan Tebak Angka")
    print("Saya menyimpan sebuah Angka Bulat antara 1 sampai 100. Coba Tebak.")
    while a != b:
        n = n + 1
        b = int(input("Masukkan Tebakan ke- "+ str(n) + ":> "))
        if b < a:
            print("Itu Terlalu Kecil. Coba lagi")
        elif b > a:
            print("Itu Terlalu Besar. Coba lagi")
        else:
            print("Ya, Anda Benar.")
            break
#No.13
def katakan(bilangan):  
    angka = ["","Satu","Dua","Tiga","Empat","Lima",
             "Enam","Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil = " "
    n = int(bilangan)
    if n>=0 and n<=11:
        Hasil = Hasil+angka[n]
    elif n<2:
        Hasil = katakan(n%10) + "Belas"
    elif n<100:
        Hasil = katakan(n/10) + "Puluh" + katakan(n%10)
    elif n<200:
        Hasil = "Seratus" + katakan(n-100)
    elif n<1000:
        Hasil = katakan(n/100) + "Ratus" + katakan(n%100)
    elif n<2000:
        Hasil = "Seribu" + katakan(n-1000)
    elif n<10000:
        Hasil = katakan(n/1000) + "Ribu" + katakan(n%1000)
    elif n<20000:
        Hasil = "Sepuluh Ribu" + katakan(n-10000)
    elif n<100000:
        Hasil = katakan(n/10000) + "Puluh" + katakan(n%10000)
    elif n<200000:
        Hasil = "Seratus Ribu" + katakan(n-100000)
    elif n<1000000:
        Hasil = katakan(n/100000) + "Ratus" + katakan(n%100000)
    elif n<2000000:
        Hasil = "Satu Juta" + katakan(n-1000000)
    elif n<10000000:
        Hasil = katakan(n/1000000) + "Juta" + katakan(n%1000000)
    elif n==100000000:
        Haail = "Satu Milyar" + katakan(n%10000000)
    else:
        Hasil = "Angka Hanya Sampai Satu Milyar"
    return Hasil

#No.14
def formatRupiah(bilangan): 
    a = str(bilangan)
    if len(a)<=3:
        return "Rp "+a
    else:
        y = a[-3:]
        z = a[:-3]
        return formatRupiah(z)+"."+y
        print(("Rp ")+formatRupiah(z)+"."+y)

    
    
