""" VERİTABANINA bilgiler giriliyor """
import sqlite3
class Ogrenci:
    def __init__(self,ogr_no,ogr_adi,ogr_soyadi,ogr_cinsiyeti,ogr_sinifi,ogr_telefon_numarasi,ogr_velisi,ogr_dogum_yeri):
        self.ogrenci_no=ogr_no
        self.adi=ogr_adi
        self.soyadi=ogr_soyadi
        self.cinsiyeti=ogr_cinsiyeti
        self.telefon_numarasi=ogr_telefon_numarasi
        self.velisi=ogr_velisi
        self.dogum_yeri=ogr_dogum_yeri
ogr_no=int(input("Öğrenci No:"))
ogr_adi=input("Adı:")
ogr_soyadi=input("Soyadı:")
ogr_cinsiyeti=input("Cinsiyeti:")
ogr_sinifi=input("Sınıfı:")
ogr_telefon_numarasi=input("Telefon Numarası:")
ogr_velisi=input("Velisi:")
ogr_dogum_yeri=input("Doğum Yeri:")
Kayit=Ogrenci(ogr_no,ogr_adi,ogr_soyadi,ogr_cinsiyeti,ogr_sinifi,ogr_telefon_numarasi,ogr_velisi,ogr_dogum_yeri)
baglanti=sqlite3.connect('C:/Python/Python_Kitap/DB/ogrenciler.db')
isaretci=baglanti.cursor()
# s=isaretci.execute("""
# INSERT INTO ogrenciler(
#     adi,
#     soyadi,
#     cinsiyeti,
#     sinifi,
#     telefon_numarasi,
#     velisi,
#     dogum_yeri
# ) VALUES(
#     '"'+Kayit.adi+'"',
#     '"'+Kayit.soyadi+'"',
#     '"'+Kayit.cinsiyeti+'"',
#     '"'+Kayit.sinifi+'"',
#     '"'+Kayit.telefon_numarasi+'"',
#     '"'+Kayit.velisi+'"',
#     '"'+Kayit.dogum_yeri+'"'
#     )
# """)
# s=isaretci.execute("""
# INSERT INTO ogrenciler(
#     ogrenci_no,
#     adi,
#     soyadi,
#     cinsiyeti,
#     sinifi,
#     telefon_numarasi,
#     velisi,
#     dogum_yeri
# ) VALUES(
#     ogr_no,
#     '"'+ogr_adi+'"',
#     '"'+ogr_soyadi+'"',
#     '"'+ogr_cinsiyeti+'"',
#     '"'+ogr_sinifi+'"',
#     '"'+ogr_telefon_numarasi+'"',
#     '"'+ogr_velisi+'"',
#     '"'+ogr_dogum_yeri+'"'
#     )
# """)
# s=isaretci.execute("""
# INSERT INTO ogrenciler(
#     ogrenci_no,
#     adi,soyadi,
#     cinsiyeti,
#     sinifi,
#     telefon_numarasi,
#     velisi,
#     dogum_yeri
# ) VALUES
#     (27,'Fatih','Başer','E','7A','5673578','Mustafa','Antakya')""")
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
    (31,'Fatih','Başer','E','7A','5673578','Mustafa','Antakya')""")
baglanti.commit()
baglanti.close()
print("{0} {1} isimli öğrenci başarı ile kaydedildi." .format(Kayit.adi,Kayit.soyadi))