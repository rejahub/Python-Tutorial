#Latihan Satuan Konversi Temperature

#Program konversi Celcius ke satuan lain


print("\nPROGRAM KONVERSI TEMPERATUR\n" )

#Celcius
celcius = float(input("Masukkan suhu dalam celcius = "))
print('suhu adalah =',celcius, "Celcius")

#Reamur
reamur = (4/5) * celcius
print('suhu dalam reamur adalah =',reamur, "reamur")

#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print('suhu dalam fahrenheit adalah =',fahrenheit, "fahrenheit")

#Kelvin
kelvin = celcius + 273
print('suhu dalam kelvin adalah =',kelvin, "kelvin")