""" VERİTABANINDAN tüm veriler alınıyor """
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
db=isaretci.execute("SELECT * FROM ogrenciler")
print(db.fetchall())
baglanti.close()