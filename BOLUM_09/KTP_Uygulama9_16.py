class Vektor:
    """Bu bir vektör nesnesidir"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def boyu(self):
        boy1=self.x**2
        boy2=self.y**2
        boy=(boy1 + boy2)**0.5
        # boy=(self.x**2 + self.y**2)**0.5
        return boy
    def __repr__(self):
        return("%di+%dj" % (self.x,self.y))
    def __add__(self,oteki):
        return Vektor(self.x + oteki.x, self.y + oteki.y)
    def __gt__(self, oteki):
        if self.boyu() > oteki.boyu():
            return True
        else:
            return False
A=Vektor(6,8)
B=Vektor(3,4)
print(A>B)
print(B>A)
print(B<A)
print(A<B)
