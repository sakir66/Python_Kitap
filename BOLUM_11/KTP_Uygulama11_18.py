""" VERİTABANINDAN 1 veri alınıyor """
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
db=isaretci.execute('UPDATE ogrenciler SET telefon_numarasi="668877" WHERE adi="Selim" AND soyadi="Yıldırım" AND sinifi="7B"')
baglanti.commit()