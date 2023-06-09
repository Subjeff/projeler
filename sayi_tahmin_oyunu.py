from random import randint
rand = randint(1,100)
sayac = 0

while True:
    sayac +=1
    sayi = int(input("1 ile 10 arasında bir değer giriniz (0 çıkış):"))
    
    if(sayi==0):
        print("oyunu kapattınız.")
        break
    elif sayi<rand:
        print("Daha yüksek bir sayi giriniz !!!")
        continue
    elif sayi>rand:
        print("Daha düşük bir sayi giriniz !!!")
        continue
    else:
        print("Rastgele seçilen sayi{0}!".format(rand))
        print("{0} tahminde bulundunuz".format(sayac))    