#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import subprocess
aktifKullanici = subprocess.getoutput("whoami")

if(aktifKullanici != "root"):
    print("\n lütfen yonetici yetkisi ile çalıştırın !... \n")
    exit()

try:
    portNo = int(input("\nlütfen port numarası giriniz: "))

except ValueError:

   print(" \n sayısal değer girmediniz. \n")
   portNo = 0

finally:

    if(portNo < 1):
        exit()

ss = subprocess.getoutput("lsof -i :"+str(portNo))
gel = ss.split(aktifKullanici)

print("\n " + ss)

dizi = str(gel[0]).split(" ")

if(len(dizi) > 21):

    pid = dizi[21]

    subprocess.getoutput("kill -9 "+pid)

    print("\n")

    print(pid + " öldürüldü tamamdır! ")

    print("\n")

else:
    print('"' + str(portNo) +'" portunda çalışan uygulama bulunamadı; '+ "\n")

