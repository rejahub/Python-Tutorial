##Default Argument Fungsi##

#def(argument):
#def(argument = nilai defaultnya):

#Contoh 1
def say_hello(nama = "Cantik"):
    '''fungsi default argument'''
    print(f"Hallo {nama}")

say_hello("Asro!")#jika argnya nama saja maka ini kan terbaca
say_hello()#jika argnya nama ="Cantik", maka ini kan terbaca

#Contoh 2
def sapa_dia(nama, pesan = "Apa Kabar?"):
    """Fungsi dengan satu input biasa dan satu default """
    print(f"Hai {nama}, {pesan}")

sapa_dia("Asro!", "Hai Cantikkk")
sapa_dia("Asri!")

#Contoh 3
def hitung_pangkat(angka, pangkat):
    """Fungsi dengan input biasa"""
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(3,4))

hasil = hitung_pangkat(pangkat = 2, angka = 3)
print(hasil)

#Contoh 4
def fungsi(input1=1,input2=2,input3=3,input4=4,input5=5):
    hasil = input1 + input2 + input3 + input4 + input5
    return hasil

print(fungsi())
print(fungsi(input3 = 10))#maka yang diubah hanya input3

