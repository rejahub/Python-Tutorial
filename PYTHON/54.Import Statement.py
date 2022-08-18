###Import Statement###

#Fungsinya adalah mengambil program dari dari file eksternal.py

#1. Menyambung program dari file eksternal.py
import programprint
import KAbar

#2. Import dengan data
import Variabel
import Variabel1

#data ada di name-space Variabel
print(Variabel.data)
print(Variabel1.Data)

#Import dengan Fungsi
import Matematika1#namespace

hasil = Matematika1.tambah(4,5)
print(hasil)