##========LIST==========##

#Kumpulan data numbers

data_angka = [1,2,3]
print(data_angka)

#Kumpulan data string

data_nama = ["Asri", "Asro", "Andra"]
print(data_nama)

#Kumpulan data boolean

data_boolean = [True, False, True]
print(data_boolean)

#Kumpulan data campuran
data_campuran = ["Panggelong", "Beteng-beteng", "Muara", 1, True]
print(data_campuran)

##Cara alternatif membuat list
data_range = range(0,10,3) #angka kelipatan tiga antara 0 sampai 10
print(data_range)
data_list = list(data_range)
print(f"data list = {data_list}")

##Membuat list dengan for loop
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)

#Membuat list pake for dan if
#ganjil
list_pake_for_if = [i for i in range (0,10) if i!= 5]
print(f"list pake for if = {list_pake_for_if}")
#genap
list_pake_for_if = [i for i in range (0,10) if i%2 ==0]
print(f"list pake for if = {list_pake_for_if}")
#ganjil
list_pake_for_if = [i for i in range (0,10) if i%2 !=0]
print(f"list pake for if = {list_pake_for_if}")
