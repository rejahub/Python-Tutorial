###Anonymous dan Lambda Python###

#Lambda Function

def fungsi_kuadrat(angka):
    """Fungsi kuadrat dengan argument angka"""
    return angka**2#expression

print("Hasil Fungsi Kuadrat =", fungsi_kuadrat(3))

#kita coba dengan lambda
#output = lambda argument:expression
kuadrat = lambda angka : angka**2
print(f"Hasil dari lambda kuadrat = {kuadrat(9)}")

#2 output

pangkat = lambda num,pow : num**pow
print(f"Hasil dari lambda kuadrat = {pangkat(4,2)}")

#Kegunaannya Lambda apa bang?

#Sorting untuk list biasa

data_list = ["Asri","Asro","Andra"]
data_list.sort()
print(f"sorted list = {data_list}")

#Sorting dia pakai panjang

def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by panjang = {data_list}")

#Sort pakai Lambda

data_list = ["Asri","Asro","Andra"]
data_list.sort( key = lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")

#filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
def kurang_dari_lima(angka):
    return angka < 7

data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x:x<7,data_angka))
print(data_angka_baru)

#Kasus genap
data_genap = list(filter(lambda x : (x % 2 == 0), data_angka))
print(data_genap)

#Kasus Ganjil
data_ganjil = list(filter(lambda x : (x % 2 != 0), data_angka))
print(data_ganjil)

#Kelipatan 3
data3 = list(filter(lambda x : (x % 3 == 0), data_angka))
print(data3)

#Anonymous Function
#Currying <- Haskell Curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,3)
print(f"Fungsi biasa = {data_hasil}")

#dengan currying akan menjadi

def pangkat(n):
    return lambda angka : angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat 3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(4)(5)}")