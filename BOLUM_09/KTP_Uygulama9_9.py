class Vektor():
    """Bu bir vektör nesnesidir"""
    def __init__(self,x,y):
        print("Bir vektör nesnesi oluşturuldu")
        print(x,y)
        self.x=x
        self.y=y
        print(self.x)
        print(self.y)
A=Vektor(6,8)
print("A.x=",A.x)
print("A.y=",A.y)