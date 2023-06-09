print("lütfen yapmak istediğiniz işlemi seçiniz")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("seçiminizi yapınız: (1/2/3/4):")

sayi1 = float(input("ilk sayıyı giriniz :"))
sayi2 = float(input("ikinci sayıyı giriniz :"))

def topla(x,y):
    return x+y
def carpma(x,y):
    return x*y
def cikarma(x,y):
    return x-y
def bolme(x,y):
    return x/y

if secim == "1":
    print("toplama işlemi sonucu :", topla(sayi1,sayi2))
elif secim == "2":
    print("carpma islemi sonucu :", carpma(sayi1,sayi2))
elif secim == "3":
    print("cikartma islemi sonucu :", cikarma(sayi1,sayi2))
elif secim == "4":
    if sayi2 == 0:
        print("sayilar 0a bölünemez")
    else:
        print("bolme islemi sonucu :", bolme(sayi1,sayi2))

else:
    print("geçersiz seçim")




