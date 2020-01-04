""" VERİTABANINDAN alan isimlerine göre ilk 3 öğrencinin
AD,SOYAD,TELEFON_NUMARASI verileri alınıyor. soyadından sıralı durumda"""
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
baglanti.row_factory=sqlite3.Row
isaretci=baglanti.cursor()
db=isaretci.execute("SELECT adi,soyadi,telefon_numarasi FROM ogrenciler ORDER BY soyadi")
for i in db.fetchmany(3):
    print(i["adi"],i["soyadi"],i["telefon_numarasi"])
baglanti.close()