#Latihan Perulangan Membuat Segitiga

sisi = 18

#1. Menggunakan for

#dummy variabel
print("Awal For")
count = 1
for i in range (sisi):
    print("*"*count)
    count += 1

print("Akhir dari for")

#2. Menggunakan While

print("Awal dari while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count < sisi :
        break

print("akhir dari While")

#3. Hanya ganjil saja

print("Awal dari ganjil")
count = 1
while True:
   
    if count %2:
         #print jika ganjil
         print("*"*count)
         count += 1
    else :   
        #akan kembali ke atas jika ganjil
        count += 1
        continue

    #akan break jika melebihi sisi
    if count > sisi :
        break

print("akhir dari ganjil")

#4. Membuat Segitiga

print("Awal dari while")
count = 1
spasi = int(sisi*3)
while True:
   
    if count %2:
         #print jika ganjil
         print(" "*spasi, "+"*count)
         spasi -= 1
         count += 1
    else :   
        #akan kembali ke atas jika ganjil
        count += 1
        continue

    #akan break jika melebihi sisi
    if count > sisi :
        break
print("Akhir dari While")

#5. Membuat Layang2

print("Awal dari while")
count = 1
spasi = int(sisi*3)
while True:
   
    if count %2:
         #print jika ganjil
         print(" "*spasi, "+"*count)
         spasi -= 1
         count += 1
    else :   
        #akan kembali ke atas jika ganjil
        count += 1
        continue

    #akan break jika melebihi sisi
    if count > sisi :
        break

sisi = 1
count = 20
spasi = int(sisi*45)
while True:
   
    if count %2:
         #print jika ganjil
         print(" "*spasi, "+"*count)
         spasi += 1
         count -= 1
    else :   
        #akan kembali ke atas jika ganjil
        count -= 1
        continue

    #akan break jika melebihi sisi
    if count < sisi :
        break

print("akhir dari While")


