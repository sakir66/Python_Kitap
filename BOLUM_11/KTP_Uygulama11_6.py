""" VERİTABANINDAN ilk 3 öğrencinin AD,SOYAD,TELEFON_NUMARASI bilgileri alınıyor """
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
db=isaretci.execute("SELECT adi,soyadi,telefon_numarasi FROM ogrenciler")
print(db.fetchmany(2))
baglanti.close()