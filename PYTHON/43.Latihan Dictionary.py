
import datetime
import os

#Template Dictionary Mahasiswa

mahasiswa_template = {
    'Nama':'Nama',
    'Nim':'000000',
    'SKS':0,
    'Lahir':datetime.datetime(1111,1,11)
    }
    
data_mahasiswa = {}
os.system('cls')#Untuk Windows
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-"*20)
    
mahasiswa = dict.fromkeys(mahasiswa_template.keys())
mahasiswa['Nama'] = input("Nama Mahasiswa:")
mahasiswa['Nim'] = input("NIM Mahasiswa:")
mahasiswa['SKS'] = int(input("SKS Mahasiswa:"))
TAHUN_LAHIR = int(input("Tahun Lahir(YYYY): "))
BULAN_LAHIR = int(input("Bulan Lahir(1-12): "))
HARI_LAHIR = int(input("Tanggal Lahir(1-30): "))
mahasiswa['Lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,HARI_LAHIR)

print(mahasiswa)
