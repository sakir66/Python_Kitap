#!C:/Python38/python.exe
import os
klasor=input('oluşturmak istediğiniz klasörü yazınız: ')
try:
    os.mkdir(klasor)
except:
    print('İstediğiniz klasör oluşturulamadı')