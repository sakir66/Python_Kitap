""" VERİTABANINDAN 1 veri siliniyor """
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
db=isaretci.execute("SELECT * FROM ogrenciler WHERE sinifi='2C'")
print(db.fetchall())
baglanti.close()