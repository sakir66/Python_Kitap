class Select:
    def __init__(self,adi='',secenekler=None,Secili=None):
        self.adi=adi
        self.secenekler=secenekler
        self.Secili=Secili
    def __repr__(self):
        eleman='<select name="%s">\n' % self.adi
        for s in self.secenekler:
            secim=' selected' if str(self.Secili)==str(s[0]) else ''
            eleman=eleman+'<option value="%s"%s>%s</option>\n'%(str(s[0]),secim,str(s[1]))
        eleman += '</select>'
        return eleman
