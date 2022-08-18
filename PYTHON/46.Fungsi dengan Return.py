##Return Value##

#Template fungsi dengan return
#def nama_fungsi(argument):
#   badan fungsi
#   return output

#Fungsi Kuadrat

def kuadrat(input_angka):
    """Fungsi Kuadrat"""
    output_kuadrat = input_angka**2
    return output_kuadrat#mengembalikan

y = kuadrat(6)
print(y)
print (kuadrat(6))

x = 15 + kuadrat (7)
print(x)

#Fungsi Tambah(+)

def fungsi_tambah(angka_1,angka_2):
    """Fungsi tambah dengan multi input pakai return"""
    return angka_1 + angka_2
a = fungsi_tambah(2,5)
print(a)
print(fungsi_tambah(2,5))

#Fungsi dengan banyak data

def operasi_aritmatika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    modulus = angka_1 % angka_2
    sisabagi = angka_1 // angka_2
    return tambah,kurang,kali,bagi,modulus,sisabagi
b,c,d,e,f,g = operasi_aritmatika(10,2)

print(f"Hasil tambah = {b}")
print(f"Hasil kurang = {c}")
print(f"Hasil kali = {d}")
print(f"Hasil bagi = {e}")
print(f"Hasil modulus = {f}")
print(f"Hasil sisa bagi = {g}")

