class Vektor:
    """Bu bir vektör nesnesidir"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return("%di+%dj" % (self.x,self.y))
A=Vektor(6,8)
B=Vektor(3,4)
C=Vektor(0,0)
C.x=A.x+B.x
C.y=A.y+B.y
print("\t "+43*"-")
print("\t"+"|"+" A vektörü "+"|"+" + "+"|"+" B vektörü "+"|"+" = "+"|"+" C vektörü "+"|")
print("\t"+12*"-","\t",11*"-","\t",11*"-")
print("\t"+4*" "+str(A.x)+","+str(A.y)+"\t"+12*" ",
        str(B.x)+","+str(B.y)+"\t"+5*" "+str(C.x)+","+str(C.y))
print("\t"+2*" ",str(A),"\t"+4*" "+str(B)+"\t"+4*" "+str(C))
