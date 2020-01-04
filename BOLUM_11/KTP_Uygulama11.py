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
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
s=isaretci.execute("""
INSERT INTO ogrenciler(
    ogrenci_no,
    adi,soyadi,
    cinsiyeti,
    sinifi,
    telefon_numarasi,
    velisi,
    dogum_yeri
) VALUES
    (27,'Fatih','Başer','E','7A','5673578','Mustafa','Antakya'),
    (19,'Dilek','Anyan','K','5B','9087234','Hasan','Çekerek'),
    (56,'Selim','Yıldırım','E','7B','1113345','Bedir','Samsun'),
    (16,'Tuğba','Tüysüz','K','1C','5556663','Cengiz','İzmir'),
    (52,'Aybüke','Abaylı','K','1C','9894323','Neşe','Yozgat')""")
baglanti.commit()
baglanti.close()
son_kayit=s.lastrowid
print("Tabloda %d adet kayıt vardır." % son_kayit)
print("Tabloda {} adet kayıt vardır." .format(son_kayit))
print("Tabloda {0} adet kayıt vardır." .format(son_kayit))