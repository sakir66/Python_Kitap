class Vektor:
    """Bu bir vektör nesnesidir"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def boyu(self):
        boy=(self.x**2 + self.y**2)**0.5
        return boy
    def __repr__(self):
        return("%di + %dj" % (self.x,self.y))
A=Vektor(6,8)
print(A)
print("")