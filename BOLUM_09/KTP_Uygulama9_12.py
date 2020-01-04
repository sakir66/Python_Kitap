class Vektor:
    """Bu bir vektör nesnesidir"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def boyu(self):
        boy=(self.x**2 + self.y**2)**(0.5)
        return boy
A=Vektor(6,8)
print("A vektörünün boyu=",A.boyu(),"birimdir.")
A.x=24
print("A vektörünün boyu=",A.boyu(),"birimdir.")