class Vektor:
    """Bu bir vektör nesnesidir"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def vektor_boyu(self,x,y):
        self.x=x
        self.y=y
        X=x**2
        Y=y**2
        V=(X+Y)**(1/2)
        return V
        # return (V.x**2 + V.y**2)**(1/2)
A=Vektor(8,6)
print("A vektörünün boyu=",A.vektor_boyu(A.x,A.y))