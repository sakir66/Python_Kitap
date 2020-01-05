""" VERİTABANINDAN 1 veri güncelleniyor """
import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
db=isaretci.execute('UPDATE ogrenciler SET sinifi="2C" WHERE sinifi="1C"')
baglanti.commit()