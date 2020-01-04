def kareKok(x):
    if x<0:
        raise ValueError('Geçersiz Değer: karekökü alınacak sayı negatif olamaz')
    return (x)**0.5
print(kareKok(25))
print(kareKok(-25))