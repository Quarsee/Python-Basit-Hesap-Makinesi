print("""
Hesap Makinesi

İşlemler;

1.Toplama İşlemi

2.Çıkarma İşlemi

3.Çarpma İşlemi

4.Bölme İşlemi
""")

a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))
islem = int(input("İşlemi Giriniz:"))

if islem == 1:
    print("{} + {} = {}".format(a,b,a+b))
elif islem == 2:
    print("{} - {} = {}".format(a,b,a-b))
elif islem == 3:
    print("{} X {} = {}".format(a,b,a*b))
elif islem == 4:
    if a == 0 and b == 0:
        print("Tanımsız")
    elif b == 0:
        print("Sıfıra Bölünemez")
    else:
        print("{} / {} = {}".format(a,b,a/b))
else:
    print("Geçersiz İşlem")
