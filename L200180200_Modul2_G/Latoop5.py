from Latoop3 import *
class SiswaSMA(Manusia):
    def __init__(self, nama, absen, alamat, saku):
        self.nama = nama
        self.absen = absen
        self.alamat = alamat
        self.saku = saku
    def __str__(self):
        s = self.nama + ', No.Absen' + str(self.absen) \
            + '. alamat ' + self.alamat \
            + '. uang saku ' + str(self.saku) \
            + 'tiap hari. '
        return s
    def ambilNama(self):
            return self.nama
    def ambilabsen(self):
            return self.absen
    def ambilsaku(self):
            return self.saku
    def ambilAlamat(self):
            return self.alamat
    def makan(self, m):
            print ("Saya baru saja makan ",m,"Sambil Balap f1. ")
            self.keadaan = 'kenyang'
    def perbaruiAlamat(self, p):
            self.alamat = p
    def tambahsangu(self, i):
            self.saku = self.saku + i
    
