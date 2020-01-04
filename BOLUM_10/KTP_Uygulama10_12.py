class GecersizDeger(Exception):
    def __init__(self,hata_iletisi):
        self.hata_iletisi=hata_iletisi
    def __str__(self):
        return self.hata_iletisi
def kareKok(x):
    if x < 0:
        raise GecersizDeger('Geçersiz Değer: karekökü alınacak sayı negatif olamaz')
    return (x)**0.5
try:
    print(kareKok(-5))
except GecersizDeger as hata:
    print('İşlev karekök alamadı. İstisnası:',hata)