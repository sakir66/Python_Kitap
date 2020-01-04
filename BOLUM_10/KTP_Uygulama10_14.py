class GecersizDeger(Exception):
    def __init__(self,hata_iletisi):
        self.hata=hata_iletisi
    def __str__(self):
        return self.hata
def kareKok(x):
    if x < 0:
        raise GecersizDeger('Geçersiz Değer: karekökü alınacak sayı negatif olamaz')
    return (x)**0.5
try:
    print(kareKok(25))
except:
    print('Bir hatadan dolayı karekök alınamadı')
else:
    print('Herhangi bir hata yakalanmadı')