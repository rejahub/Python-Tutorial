#Format String

#Contoh Generic
#String


nama = "Asro!!!"
format_str = f"Hello {nama}"

print(format_str)

#Angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

#Boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

#bilangan bulat
angka = 15
format_str = f"angka bulat = {angka:d}"
print(format_str)

#bilangan ribuan
angka = 2000
format_str = f"ribuan = {angka}"
print(format_str)

#bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.4f}"
print(format_str)

#bilangan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:011.4f}"
print(format_str)

#menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"angka minus = {angka_minus:+d}"
format_plus = f"angka plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

#memformat persen
persentase = 0.045
format_persen = f"persentase = {persentase :.1%}"

print(format_persen)

#melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

#format angka lain

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"binary = {oct(angka)}"
format_hex = f"binary = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
