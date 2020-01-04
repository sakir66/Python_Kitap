class Ebeveyn:
    def annenin_sac_rengi(self):
        return 'sarı'
    def babanın_goz_rengi(self):
        return 'mavi'
class Cocuk(Ebeveyn):
    def __init__(self,adi=''):
        self.adi=adi
    def sac_rengi(self):
        print(self.adi,"nin saç rengi muhtemelen",
        self.annenin_sac_rengi(),"olacaktır.")
nuri=Cocuk('Nuri')
nuri.sac_rengi()