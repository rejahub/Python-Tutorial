###Args pada Fungsi###

#Memasukkan data/Argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")

fungsi("Asro",160,50)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")

fungsi(["Asri",165,50])

#Menampilkan Args (Mengambil banyak inout)

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")

fungsi("Andra",170,55)

#Studi Kasus 

def tambah(*data):
    #datanya adalah tuple sehingga bisa diiterasi
    output = 0
    for angka in data:
        output+=angka#ambil banyak input

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print("Hasil =", hasil)

hasil = tambah(15,5,10)
print("Hasil =", hasil)
