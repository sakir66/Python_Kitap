import sqlite3
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
db=isaretci.execute('ALTER TABLE okul_ogrenciler RENAME TO ogrenciler')
baglanti.commit()