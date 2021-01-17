'''lst = []
largest = None
adet = int(input('Kaç Sayı Girilecek: '))
for n in range(adet):
    sayi = int(raw_input('Enter integer #%d: ' % i))
    #lst.append(sayi)

 
  if sayi % 2 != 0 and (not largest or sayi > largest):
        largest = sayi

if largest is None:
    print("You didn't enter any odd numbers")
else:
    print("Your largest odd number was:", largest)'''


from __future__ import print_function
try:  
    raw_input
except NameError:  
    raw_input = input


enTek_Sayi = []

alinacakSayi = int(input("Kaç sayı girilecek ? : "))
for i in range(alinacakSayi):
    sayi = int(raw_input('Bir tamsayı giriniz #%d: ' % i))
    if sayi % 2 != 0 and (not enTek_Sayi or sayi > enTek_Sayi):
        enTek_Sayi = sayi

if enTek_Sayi is None:
    print("Hiçbir tek tamsayı girişi yapmadınız!")
else:
    print("En büyük tek tamsayı:", enTek_Sayi)





'''liste = []
for eleman in liste:
    print(liste)

liste.append(input("Listeye Eklenecek Sayıları Giriniz: "))
print(liste)'''

   
