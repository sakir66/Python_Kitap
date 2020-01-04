#!C:\Python38\python.exe
from modul_9_2 import Ebeveyn
class Cocuk(Ebeveyn):
    def __init__(self,adi=''):
        self.adi=adi
    def sac_rengi(self):
        print(self.adi,"nin saç rengi muhtemelen",
        self.annenin_sac_rengi(),"olacaktır")
nuri=Cocuk('Nuri')
nuri.sac_rengi()