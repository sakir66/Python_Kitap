#!C:/Python38/python.exe
import os
klasor=input('oluşturmak istediğiniz klasörü yazınız: ')
try:
    os.mkdir(klasor)
except WindowsError as hata:
    print("İstediğiniz klasor oluşturulamadı. Sebebi:",hata.args[0],"--->",hata.args[1])
