print('\nHOMEWORK TEMPERATURE\n')

#Kelvin
fahrenheit = float(input('Masukkan suhu dalam fahrenheit = '))
print('suhu adalah =', fahrenheit)

kelvin = 5/9 * (fahrenheit - 32) + 273
print('suhu dalam kelvin adalah =', kelvin)

#fahrenheit
kelvin = float(input('Masukkan suhu dalam kelvin = '))
print('suhu adalah =', kelvin)

fahrenheit = 9/5 * (kelvin - 273) + 32
print('suhu dalam fahrenheit adalah =', fahrenheit)