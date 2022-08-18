###Global and Local Scope###

nama_global = "Asri"# <- Variabel Global

#akses variabel global dalam fungsi
def fungsi():
    print(f"Fungsi menampilkan {nama_global}")

fungsi()

#Akses variabel global dalam loop
for i in range (0,5):
    print(f"loop{i} - {nama_global}")

#Percabangan
if True:
    print(f"if menampilkan {nama_global}")

##Variabel Local Scope##

def fungsi2():
    nama_local = "Asro"# <- Variabel Local Scope

fungsi2()
#print(nama_local) <- Tidak bisa dilakukan

##Contoh 1 -> Penggunaan Variabel Local##

def say_andra():
    print(f"Hello {nama}")

nama = "Andra!"
say_andra()

##Contoh 2 -> Merubah Variabel Local##

angka = 0
name = "Asri"

def ubah(nilai_baru, nama_baru):
    global angka#Fungsi ini dapat akses merubah
    global name
    angka = nilai_baru
    name = nama_baru

print(f"Sebelum {angka,name}")
ubah(10,"Asro")
print(f"Sesudah {angka,name}")

##Contoh 3 : Loop
angka = 0

for i in range(0,5):
    angka+=i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka_dummy = 10

print(angka)
print(angka_dummy)
