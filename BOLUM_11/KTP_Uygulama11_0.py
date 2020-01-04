import sqlite3
print(sqlite3.version)
def vtb_baglan(yol,vtb_adi):
    baglanti=sqlite3.connect("'"+yol+"/"+vtb_adi)
    isaretci=baglanti.cursor()
def tablo_Olustur(tablo_adi,alanlar):
    for item in alanlar:
class Ogrenci:
    def __init__(self,ogr_no,adi,soyadi,cinsiyeti,sinifi,telefon_numarasi,velisi,dogum_yeri):
        self.ogr_no=ogr_no
        self.adi=adi
        self.soyadi=soyadi
        self.cinsiyeti=cinsiyeti
        self.sinifi=sinifi
        self.telefon_numarasi=telefon_numarasi
        self.velisi=velisi
        self.dogum_yeri=dogum_yeri
    def alan_Turu(self,tur,uzunluk):
        self.tur=tur
        self.uzunluk=uzunluk

kayit=Ogrenci(27,'Fatih','Başer','E','7A','5673578','Mustafa','Antakya')
alan_Tipleri=["VARCHAR","INTEGER"]
alanlar=[
    (ogrenci_no,"INTEGER",50),
    (adi,"VARCHAR",50),
    (soyadi,"VARCHAR",50),
    (cinsiyeti,"VARCHAR",1),
    (sinifi,"VARCHAR",3),
    (telefon_numarasi,"VARCHAR",12),
    (velisi,,)
    ]
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
print(son_kayit)