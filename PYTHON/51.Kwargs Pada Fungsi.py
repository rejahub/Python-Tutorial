###Kwargs pada Fungsi###

def fungsi(nama,tinggi,berat):
    """Fungsi Biasa"""
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")

fungsi("Asri",165,45)

def fungsi(**kwargs):
    """Fungsi Kwargs"""
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")

fungsi(nama = "Asri", tinggi = 165, berat = 45)

#Studi Kasus

def math (*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak ada Operasi")

    return output

hasil = math(1,2,3,4,5,6,option ="tambah")
print(f"Hasil jumlah {hasil}")

hasil = math(1,2,3,4,5,6,option ="kali")
print(f"Hasil kali {hasil}")
