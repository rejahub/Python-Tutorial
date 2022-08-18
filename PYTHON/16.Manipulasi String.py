#Operasi dan Manipulasi String

#1. Menyambung string (concatenate)

nama_pertama = 'Asro'
nama_tengah = 'D'
nama_belakang = 'Siregar'
nama_lengkap = nama_pertama +' '+ nama_tengah +' '+ nama_belakang
print(nama_lengkap)

#2. Menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

#3. Operator untuk String

#mengecek apakah ada komponen  char atau string di string

D = "D"
status = D in nama_lengkap
print (D + " ada di " + nama_lengkap + " = " + str(status))

D = "D"
status = D not in nama_lengkap
print (D + " tidak ada di " + nama_lengkap + " = " + str(status))

#Mengulang string
print('wk'*10)
print(15*'wk')

#indexing
print("index ke-0 = " + nama_lengkap[0])
print("index ke-5 = " + nama_lengkap[5])
print("index ke-(-1) = " + nama_lengkap[-1]) #hitungnya dari belakang
print("index ke-(-3) = " + nama_lengkap[-3])
print("index ke- [0,4] = " + nama_lengkap[0:4]) # tanda : artinya sampai
print("index ke- [6,14] = " + nama_lengkap[6:14])
print("index ke- [0,2,4,6,8,10,12,14] = " + nama_lengkap[0:14:2]) #dengan lompatan 2 angka

#Item paling kecil
print("paling kecil = " + min(nama_lengkap))
#Item paling besar
print("paling besar = " + max(nama_lengkap))


ascii_code = ord(" ")
print('Ascii code untuk spasi adalah = ' + str(ascii_code))
data = 117
print('character untuk spasi adalah = ' + chr(data))

#Operator dalam bentuk method part 1

data = 'otong surotong marodong'
jumlah = data.count('o')
print('jumlah o pada' + data + ' = ' + str(jumlah))