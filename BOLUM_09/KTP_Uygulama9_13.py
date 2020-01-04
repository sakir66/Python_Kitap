class Vektor:
    """Bu bir vektor nesnesidir"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def boyu(self):
        boy=(self.x**2 + self.y**2)**0.5
        return boy
    def yazdir(self):
        print("%di + %dj" % (self.x,self.y))
A=Vektor(6,8)
A.yazdir()