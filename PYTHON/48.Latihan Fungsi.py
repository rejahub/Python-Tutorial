###Latihan Fungsi###

import os

#Program menghitung luas dan keliling persegi panjang

#Membuat Header Program
#os.system("cls")
#print(f"{'PROGRAM MENGGHITUNG LUAS':^40} ")
#print(f"{'DAN KELILING PERSEGI PANJANG':^40} ")
#print(f"{'-'*40:^40}")

#Mengambil user input
#PANJANG = int(input("Masukkan panjang = "))
#LEBAR = int(input("Masukkan lebar = "))

#Tampilan luas dan keliling
#Luas = PANJANG * LEBAR
#Keliling = 2*(PANJANG + LEBAR)

#Tampilan Hasilnya
#print("Hasil Luas =", Luas)
#print("Hasil Keliling =", Keliling)

def header():
    """Fungsi Header"""
    os.system("cls")
    print(f"{'PROGRAM MENGGHITUNG LUAS':^40} ")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40} ")
    print(f"{'-'*40:^40}")

def input_user():
    """Fungsi Input User"""
    #Mengambil user input
    Panjang = int(input("Masukkan panjang = "))
    Lebar = int(input("Masukkan lebar = "))

    return Panjang,Lebar

def display(message,value):
    """Fungsi Display"""
    print(F"Hasil Perhitungan, {message} = {value}")

#Hitung Luas
def hitung_luas(Panjang,Lebar):
    """Fungsi Luas"""
    return Panjang*Lebar

#Hitung Keliling
def hitung_keliling(Panjang,Lebar):
    """Fungsi Keliling"""
    return 2*(Panjang+Lebar)

#Program Utamanya
while True:
    header()

    Panjang,Lebar = input_user()
    Luas = hitung_luas(Panjang,Lebar)
    Keliling = hitung_keliling(Panjang,Lebar)

    display("Luas", Luas)
    display("Keliling", Keliling)

    isContinue = input("Apakah masih lanjut y/n ? ")
    if isContinue == "n":
        break
print("Program telah selesai, Terima Kasih")
