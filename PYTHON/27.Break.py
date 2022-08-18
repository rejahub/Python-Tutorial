#Break

angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") #aksi 1

    if angka == 3:
        print("Niceee!!")
        break#akan membuat loop menghakhiri step selanjutnya

    print("Whatsappppp") #aksi 2
print("Cukup masss finish")

data_int = int(input("Hitung sampai = "))

angka = 0

while True:
    angka += 1
    print(f"count = {angka}") #aksi 1

    if angka == data_int:
        print("Niceee!!")
        break#akan membuat loop menghakhiri step selanjutnya

    print("Whatsappppp") #aksi 2
print("Cukup masss finish")


