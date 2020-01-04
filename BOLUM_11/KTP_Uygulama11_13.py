""" Fatih Başer in sadece telefon numarası listeleniyor """
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
baglanti.row_factory=sqlite3.Row
isaretci=baglanti.cursor()
db=isaretci.execute('SELECT * FROM ogrenciler WHERE adi="Fatih" AND soyadi= "Başer"')
for i in db.fetchall():
    print(i["telefon_numarasi"])
baglanti.close()
