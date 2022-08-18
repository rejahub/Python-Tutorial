###Fungsi dengan Argument###

#def fungsi(input):#argument/parameter
    #badan Fung

#String
def halo_dunia(nama):
    #fungsi halo dunia menerima input dengan variabel nama#
    print("Selamat Datang Wahai", nama)

halo_dunia("Asri!!!!!!")
halo_dunia('Asro!!!!!!!')

#Integer
def tambah(angka_1,angka_2):
    #fungsi tambah menerima input dengan variabel angka_1 dan angka_2#
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
tambah(2,7)
tambah(10,2)

#List
def list(buah):
    #fungsi list menerima input dengan variabel buah#
    data_buah = buah.copy()
    for b in data_buah:#looping
        print("Buah yang enak itu", b)

nama_buah = ["Durian","Mangga","Rambutan"]

list(nama_buah)