##======Operasi List=======##

data_angka = [1,2,3,4,5,6,7,8,9,1,2,3,4,3,4,2,5]
print("Data Angka = \n", data_angka)

#Count Data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print("jumlah angka 4 = ", jumlah_data_4)
print("jumlah angka 3 = ", jumlah_data_3)

#ambil posisi data
data = ["Asro", "Asri", "Andra", "Tarmizi"]
print("Data", data)

index_asro = data.index("Asro")
index_tarmizi = data.index("Tarmizi")
print("Index Asro = ", index_asro)
print("Index Tarmizi = ", index_tarmizi)

#Mengurutkan list
print("Data sebelum sort = ", data_angka)
data_angka.sort()
print("Data Sort = ", data_angka)

#Mengurutkan list String
print("Belum Sort = ", data)
data.sort()
print("Data Sort = ", data)

#Balik Urutan List
data_angka.reverse()
data.reverse()
print("Data di reverse =\n",data_angka,"\n",data)