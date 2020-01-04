""" Okul numarası 20 den büyük kız öğrenciler listeleniyor """
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
baglanti.row_factory=sqlite3.Row
isaretci=baglanti.cursor()
db=isaretci.execute('SELECT * FROM ogrenciler WHERE cinsiyeti="K" AND ogrenci_no > 20')
for i in db.fetchall():
    print(i["adi"],i["soyadi"],i["telefon_numarasi"])
baglanti.close()