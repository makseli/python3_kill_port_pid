#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import subprocess
import sys

try:
    portNo = int(input("\nlütfen port numarası giriniz: "))

except ValueError:

   print(" \n sayısal değer girmediniz. \n")
   portNo = 0

finally:

    if(portNo < 1):
        sys.exit()

ss = subprocess.getoutput("lsof -i :"+str(portNo))
aktifKullanici = subprocess.getoutput("whoami")
gel = ss.split(aktifKullanici)

print("\n")

print(ss)

dizi = str(gel[0]).split(" ")

if(len(dizi) > 21):

    pid = dizi[21]

    subprocess.getoutput("kill -9 "+pid)

    print("\n")

    print(pid + " öldürüldü tamamdır! ")

    print("\n")

else:
    print('"' + str(portNo) +'" portunda çalışan uygulama bulunamadı; '+ "\n")

