import datetime
import os
import string
import random

#Template Dictionary Mahasiswa
mahasiswa_template = {
    'key':'mahasiswa',
    'nama':'nama',
    'nim':'000000',
    'sks':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}
while True :
    os.system('cls')#Untuk Windows
    #os.system('clear')#Untuk UNIX
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)
    
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa:")
    mahasiswa['nim'] = input("NIM Mahasiswa:")
    mahasiswa['sks'] = int(input("Sks Mahasiswa:"))
    TAHUN_LAHIR = int(input("Tahun Lahir(YYYY): "))
    BULAN_LAHIR = int(input("Bulan Lahir(1-12): "))
    HARI_LAHIR = int(input("Tanggal Lahir(1-30): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,HARI_LAHIR)
    print(mahasiswa)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(5)))
    data_mahasiswa.update({KEY:mahasiswa})
    print(f"{'KEY':<6} {'Nama':<17} {'Nim':<9} {'Sks':<10}{'Lahir':<10}")
    print("-"*60)
    
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x") 
        
        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")
        
    is_done = input('Mau ditambah lagi (y/n)?')
    if is_done =='n':
        break
print("Akhir dari Program, Terimakasih")