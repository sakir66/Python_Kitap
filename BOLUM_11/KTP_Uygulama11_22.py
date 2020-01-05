""" VERİTABANINDA Tablo ismi değiştiriliyor """
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
db=isaretci.execute("ALTER TABLE ogrenciler RENAME TO okul_ogrenciler")
baglanti.commit()