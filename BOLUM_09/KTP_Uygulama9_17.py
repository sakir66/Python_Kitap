class Select:
    def __init__(self,adi="",secenekler=None):
        self.adi=adi
        self.secenekler=secenekler
secim_kutusu=Select("renk",[(1,"Mavi"),(2,"Sarı"),(3,"Kırmızı")])
print(secim_kutusu.adi,secim_kutusu.secenekler)