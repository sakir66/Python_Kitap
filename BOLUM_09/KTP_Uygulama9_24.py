class Ebeveyn:
    def annenin_sac_rengi(self):
        return 'sarı'
    def babanin_goz_rengi(self):
        return 'mavi'
class Cocuk(Ebeveyn):
    def __init__(self,adi=''):
        self.adi=adi
    def sac_rengi(self):
        print(self.adi,"nin saç rengi muhtemelen",
        self.annenin_sac_rengi(),"olacaktır.")
    def babanin_goz_rengi(self):
        print("Şimdi bunu bilmiyoruz")
nuri=Cocuk('Nuri')
nuri.babanin_goz_rengi()