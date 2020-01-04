""" Sadece ERKEK öğrenciler listeleniyor """
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
baglanti.row_factory=sqlite3.Row
isaretci=baglanti.cursor()
db=isaretci.execute('SELECT * FROM ogrenciler WHERE cinsiyeti="E" AND sinifi="7B"')
for i in db.fetchmany(3):
    print(i["adi"],i["soyadi"],i["telefon_numarasi"])
baglanti.close()