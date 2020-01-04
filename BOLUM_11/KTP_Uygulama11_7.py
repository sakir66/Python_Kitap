""" VERİTABANINDAN ilk 3 öğrencinin AD,SOYAD,TELEFON_NUMARASI verileri
 düzgün bir şekilde alınıyor. """
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
db=isaretci.execute("SELECT adi,soyadi,telefon_numarasi FROM ogrenciler")
for i in db.fetchmany(3):
    print("Adı, Soyadı: %s %s\nTelefon Numarası: %s\n" % i)
baglanti.close()