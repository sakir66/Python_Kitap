class Ebeveyn:
    def annenin_sac_rengi(self):
        return 'sarı'
    def babanın_goz_rengi(self):
        return 'mavi'
class Amca:
    def amcanin_sac_tipi(self):
        return 'kıvırcık'
class Cocuk(Ebeveyn,Amca):
    def __init__(self,adi=''):
        self.adi=adi
    def sac_rengi(self):
        print(self.adi,"nin saç rengi muhtemelen",
        self.annenin_sac_rengi(),"olacaktır")
    def saci(self):
        print(self.adi,'nin saçı',self.annenin_sac_rengi(),'ve',self.amcanin_sac_tipi(),'olabilir')
nuri=Cocuk('Nuri')
nuri.saci()