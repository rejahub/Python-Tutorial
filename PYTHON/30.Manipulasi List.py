##=======Manipulasi Data List=========##

#index  0(-3) 1(-2) 2(-1)
data = ["Asri","Asro","Andra"]

#mengambil data dari list
data_0 = data[0]
print(f"data pertama (index_0) = {data_0}")
data_2 = data[-1]
print(f"data terakhir(index-1) = {data_2}")
panjang_data = len(data)
print(f"Panjang data = ,{panjang_data}")

####Manipulasi data List####

#Menanmbahkan item pada list
print("Data sebelum ditambah = \n",data)
data.insert (2,"Tarmizi")
print("data sesudah ditambah = \n", data)
#Menambah di akhir list
data.append ("Salman")
print("data ditambah diakhir = \n", data)
#Menggabungkan list
data_baru = ["Carles","Sarton", "Somad"]
data.extend (data_baru)
print("data gabungan = \n", data)
#Merubah data
#Kita ubah data 3 menjadi Candra
data[3] = "Candra"
print("Data rubah = \n", data)
#Meremove data
data.remove("Sarton")
print("Data Remove = \n", data)
#Meremove data paling belakang
data.pop()
print("Data Akhir = \n", data)
data.sort()#Mengurutkan sesuai Abjad
print(f"Data Akhir = \n, {data}")