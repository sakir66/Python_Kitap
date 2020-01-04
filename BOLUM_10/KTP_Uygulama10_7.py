import os
try:
    os.mkdir('c:/windows')
except:
    print("os.mkdir('c:/windows') ==> WindowsError (Windows hatası) sınıfından bir hata")
