#Nest List
data_0 = [1,2]
data_1 = [3,4]
data_list = [1,2,3,4]
print("data list = ",data_list)

list_2D = [data_0,data_1,data_list,0,7]

print("list_2D = ",list_2D)

#Contoh Penggunaan
peserta_0 = ["Asri",27,"Laki-laki"]
peserta_1 = ["Andra",23,"Laki-laki"]
peserta_2 = ["Asro",24,"Perempuan"]
list_peserta = [peserta_0,peserta_1,peserta_2]
print("List Peserta = ",list_peserta)

for peserta in list_peserta:
    print("Nama\t:",peserta[0])
    print("Umur\t:",peserta[1])
    print("Gender\t:",peserta[2],"\n")

#dengan reference
list_copy = list_peserta.copy();
print("Peserta = ",list_copy)
peserta_1[0] = "Tarmizi"
print("List Peserta = ",list_peserta)
print("Peserta = ",list_copy)

