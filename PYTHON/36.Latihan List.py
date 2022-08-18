#Program List Buku

list_buku = []
while True:
    print("Masukkan Data Buku")
    print("=="*10,"\t")
    Judul = input("Masukkan Judul Buku\t: ")
    Penulis = input("Masukkan Nama Penulis\t: ")

    buku_baru =[Judul,Penulis]
    list_buku.append(buku_baru)

    print("\n\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n\n","="*20)
    islanjut = input("Apakah dilanjutkan?(y/n) ")

    if islanjut =="n":
        break
    
print("PROGRAM SELESAI")