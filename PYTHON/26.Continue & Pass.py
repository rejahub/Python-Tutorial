#Continue, Pass, Break

#pass-> berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0

while angka < 5:

    angka += 1
    if angka == 3:
        pass #Ini tidak akan dieksekusi

    print(angka)

angka = 0

while angka < 5:

    angka += 1
    print(f"angka sekarang -> {angka}") #aksi 1

    if angka == 3:
        print("Whatsapp!!")
        continue#akan membuat loop meloncat ke step selanjutnya

    print("nice") #aksi 2
print("Cukup masss")