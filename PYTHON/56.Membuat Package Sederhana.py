###Mmebuat Package Sederhana###

import time
t_start = time.time()
import Modul_matematika

hasil_tambah = Modul_matematika.tambah(1,2,3,4,5)

print(f"Hasil tambah dari package adalah = {hasil_tambah}")
t_end = time.time()

print(f"Waktu Eksekusi = {t_end - t_start}")

import Fisika#1
from Fisika import gaya as force#2

gaya = Fisika.gaya(700,10) #1
print(f"Gaya = {gaya}")

gaya = force(700,10)#2
print(f"Gaya = {gaya}")

