#!C:\Python38\python.exe
yas=input('Yaşınızı Giriniz: ')
try:
    yas=int(yas)
    print("Üç yıl sonra %d yaşında olacaksınız" % (yas+3))
except:
    print('Sayı değer girseydiniz üç yıl sonra hangi yaşta olacağınızı söyleyecektim')