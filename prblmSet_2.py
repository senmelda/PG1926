

uzunluk = int(input("Mail adresi uzantısı için uzunluk bilgisi giriniz : "))
def kontrol(str):
    count = 0
    
    for ch in str:
        if ch == '@':
            count = count + 1
    if count == 1:
        return True
    else:
        return False


mail = input('Mail : ')
if(kontrol(mail)==True):
    print("Doğru")
else:
    print("Yanlış")
