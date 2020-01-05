import sqlite3
baglanti=sqlite3.connect('c:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
isaretci.execute('ALTER TABLE ogrenciler ADD dogum_tarihi FLOAT')
baglanti.commit()