""" VERİTABANINDAN 1 veri alınıyor """
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
db=isaretci.execute("SELECT * FROM ogrenciler WHERE sinifi LIKE '7%'")
print(db.fetchall())
baglanti.close()