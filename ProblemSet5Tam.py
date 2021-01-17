class Okul():
    def __init__(self,isim,tur):
        self.isim = isim
        self.tur = tur
    def bilgilerigoster(self):
        print("Okul ismi : {} \n Okul Türü : {}\n".format(self.isim,self.tur))

class Ogrenci():
    def __init__(self,adi_soyadi,sınıf,sube):
        self.adi_soyadi = adi_soyadi
        self.sınıf = sınıf 
        self.sube = sube
    def ogrenci_bilgileri(self):
        print("Adı Soyadı : {} \n Sınıfı : {}\n Şube : {}\n".format(self.adi_soyadi,self.sınıf,self.sube))

class Calisan():
    def __init__(self,isim,unvan,maas):
        self.isim = isim
        self.unvan = unvan
        self.maas = maas
    def calisan_bilgileri(self):
        print("Çalışan Bilgileri : \n Adı Soyadı : {}\n Unvanı : {}\n Maaş : {}\n".format(self.isim,self.unvan,self.maas))
    def maas_artir(self,yenimaas):
        self.maas+=yenimaas
        print("Çalışanın yeni maaşı : {}\n".format(self.maas))

class Ilkokul(Okul):
    def __init__(self,isim,sınıf_sayisi,ogrenci_sayisi,calisan_sayisi):
        self.isim = isim
        self.sınıf_sayisi = sınıf_sayisi
        self.ogrenci_sayisi = ogrenci_sayisi
        self.calisan_sayisi = calisan_sayisi
    
    def ogrenci_ekle(self,eklenen_ogrenci):
        self.ogrenci_sayisi+=eklenen_ogrenci
        print("Eklenen öğrenci ile birlikte yeni öğrenci sayısı : {}\n ".format(self.ogrenci_sayisi))
    def bilgilerigoster(self):
        print("Okul adı: {}\nSınıf sayısı : {}\nÖğrenci Sayısı : {}\nÇalışan Sayısı : {}\n".format(self.isim,self.sınıf_sayisi,self.ogrenci_sayisi,self.calisan_sayisi))

class Lise(Okul):
    def __init__(self,isim,sınıf_sayisi,ogrenci_sayisi,calisan_sayisi):
        self.isim = isim
        self.sınıf_sayisi = sınıf_sayisi
        self.ogrenci_sayisi = ogrenci_sayisi
        self.calisan_sayisi = calisan_sayisi
    def calisan_ekle(self,eklenen_calisan):
        self.calisan_sayisi+=eklenen_calisan
        print("Eklenen çalışan ile birlikte yeni çalışan sayısı : {}\n".format(self.calisan_sayisi))
    def bilgilerigoster(self):
        print("Okul adı: {}\n Sınıf sayısı : {}\n Öğrenci Sayısı : {}\n Çalışan Sayısı : {}\n".format(self.isim,self.sınıf_sayisi,self.ogrenci_sayisi,self.calisan_sayisi))
        
class Lise_Ogrenci(Ogrenci):
    def __init__(self,adi_soyadi,sınıf,sube,dal,yazılı_1,yazılı_2,sozlu_not):
        self.adi_soyadi = adi_soyadi
        self.sınıf = sınıf
        self.sube = sube
        self.dal = dal
        self.yazılı_1 = yazılı_1
        self.yazılı_2 = yazılı_2
        self.sozlu_not = sozlu_not
    def ogrenci_bilgileri(self):
        print("Öğrenci Adı : {}\n Sınıfı : {}\n Şubesi : {}\n Dalı : {}\n 1.yazılısı : {}\n 2.Yazılısı : {}\n Sözlü notu : {}\n ".format(self.adi_soyadi,self.sınıf,self.sube,self.dal,self.yazılı_1,self.yazılı_2,self.sozlu_not))
    def ogrenci_not(self):
        self.ort = ((((self.yazılı_1*0.3) + (self.yazılı_2*0.5))) + (self.sozlu_not*0.2))
        print("Öğrencinin ortalaması : {}".format(self.ort))

class Meslek_Lise(Ogrenci):
    def __init__(self,bolum):
        self.bolum = bolum
    def ogrenci_bilgileri(self):
        print("Öğrenci Adı : {}\n Sınıfı : {}\n Şubesi : {}\n Bölümü : {}\n".format(self.adi_soyadi,self.sınıf,self.sube,self.bolum))

class Ogretmen(Calisan):
    def __init__(self,kurum,dal):
        self.kurum = kurum
        self.dal = dal
    def calisan_bilgileri(self):
        print("Çalışan Bilgileri : \n Adı Soyadı : {}\n Unvanı : {}\n Maaş : {}\n Çalıştığı Kurum : {}\n Dal : {}\n".format(self.isim,self.unvan,self.maas,self.kurum,self.dal))

class Gorevli(Calisan):
    def __init__(self,kurum):
        self.kurum = kurum
    def calisan_bilgileri(self):
        print("Çalışan Bilgileri : \n Adı Soyadı : {}\n Unvanı : {}\n Maaş : {}\n ".format(self.isim,self.unvan,self.maas))

okul  = Okul(isim="",tur="")
ogrenci = Ogrenci(adi_soyadi="",sınıf="",sube="")
okul1 = Ilkokul(isim="Mareşal Mustafa Kemal İ.Ö.O.",sınıf_sayisi = 15,ogrenci_sayisi = 150,calisan_sayisi=21)
okul2 = Lise(isim="Zeki Özdemir Anadolu Lisesi",sınıf_sayisi = 25,ogrenci_sayisi = 300,calisan_sayisi=42)
ogrenci1 = Lise_Ogrenci(adi_soyadi="Lamia Adalı",sınıf = 9 , sube = "B",dal="Sayısal",yazılı_1=55,yazılı_2=80,sozlu_not=90)
okul1.ogrenci_ekle(15)
okul1.bilgilerigoster()
okul2.bilgilerigoster()
ogrenci.ogrenci_bilgileri()
ogrenci1.ogrenci_bilgileri()
ogrenci1.ogrenci_not()
