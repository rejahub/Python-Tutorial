#Date and Time (Latihan)

import datetime as dt

print("Silahkan masukkan Nama, Tanggal, Bulan, Tahun lahir anda")
tanggal = int(input("tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("tahun \t\t: "))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal Lahir saya adalah : {tanggal_lahir}")
print(f"Hari nya adalah hari : {tanggal_lahir:%A}")

hari_ini = dt.date.today()

print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(1997,8,18)
print(tanggal)
print(f"Hari ini adalah hari = {tanggal:%A}")

hari_ini = dt.date.today()
print(f"hari_ini adalah hari = {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_bulan = umur_hari.days/30
umur_tahun = umur_hari.days//365
umur_bulan_sisa = (umur_hari.days %365) // 30
print(f"Umur saya adalah = {umur_hari}")
print(f"Umur saya adalah = {umur_bulan} bulan")
print(f"Umur saya adalah = {umur_tahun} tahun, {umur_bulan_sisa} bulan")


