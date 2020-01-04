""" SQLLITE veritabanı oluşturuluyor """
import sqlite3
print(sqlite3.version)
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
isaretci.execute("""
CREATE TABLE ogrenciler(
    kayit_no INTEGER PRIMARY KEY,
    ogrenci_no INTEGER NOT NULL,
    adi VARCHAR(50),
    soyadi VARCHAR(50),
    cinsiyeti VARCHAR(1),
    sinifi VARCHAR(3),
    telefon_numarasi VARCHAR(12),
    velisi VARCHAR(75),
    dogum_yeri VARCHAR(25)
)""")
baglanti.commit()
baglanti.close()