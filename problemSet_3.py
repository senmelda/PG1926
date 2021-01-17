
sayilar = [] 
girdi = int(input("Kaç sayı girilecek ? : "))
for i in range(girdi):
    sayi = int(input("{}. sayıyı giriniz :".format(i+1)))
    sayilar+=[sayi]
print(sayilar)

"""rakamlar = []
rakam = 0
while rakam <= 7 :
    sayi = int(input("Lütfen bir sayı giriniz : "))
    rakam = sayi+1
    rakamlar.append(rakam)

print(rakamlar)"""
def siralama(x):
    zero = []
    otherNum = list()
    for i in x:
        if i == 0:
            zero.append(i)
        else:
            otherNum.append(i)

    result = zero + otherNum
    return(result)

x = siralama(sayilar)
print(x)




