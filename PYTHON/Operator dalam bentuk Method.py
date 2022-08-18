#Operator dalam bentuk Method

#Merubah case dari string

#Merubah semua ke upper case

salam = 'bro!'
print("normal = " + salam)
salam = salam.upper()
print('upper = ' + salam)

#Merubah semua ke lower case
alay = "AKu Kece ABIzzzzzzz"
alay = alay.lower()
print('lower = ' + alay)

##Pengecekan untuk isX Method

#Contoh Pengecekan Lower Case
salam = "sist"
apakah_lower = salam.islower() #Hasilnya boolean
print( salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() #Hasilnya boolean
print(salam + " is upper = " + str(apakah_upper))

#isalpha() --> untuk mengecek semua huruf
#isnumb() --> huruf dan angka
#isdecimal() --> angka saja
#isspace --> spasi, tab, newline \n
#istitle --> semua kata dimulai dengan huruf besar

#ngecek startswith() dan endswith
cek_start = 'Sangjangnim oppa'.startswith("sangjangnim")
print("start = " + str(cek_start))

cek_end = 'Sangjangnim oppa'.startswith("oppa")
print("start = " + str(cek_end))

#Penggabungan komponen (split)
pisah = ['Aku', 'Sayang', 'Kamu']
print(pisah)
gabungan = ' '.join(pisah) 
print(gabungan)

gabungan = ' ehm '.join(pisah) 
print(gabungan)

gabungan = 'akuehmsayangehmkamu'
print(gabungan.split('ehm'))

#Alokasi karakter rjust(), ljust(), center()
print(5*'=' + 'data' + '='*5)

kanan = "kanan".rjust(10)
print(kanan)

kiri = "kiri".ljust(10)
print(kiri)

tengah = "tengah".center(10,"-")
print("'"+tengah+"'")

#kebalikannya --> strip()
tengah = tengah.strip("-")
print("'"+tengah+"'")

