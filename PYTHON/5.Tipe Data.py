
#tipe data : angka satuan (integer)
data_integer = 1
print("data =", data_integer)
print("- bertipe =",type(data_integer))

#tipe data : angka koma (float)
data_float = 2.5
print("data =", data_float)
print("- bertipe =",type(data_float))

#tipe data : tulisan/teks (string)
data_string = "Kia"
print("data =", data_string)
print("- bertipe =",type(data_string))

#tipe data : biner true/false (boolean)
data_bool = False
print("data =", data_bool)
print("- bertipe =",type(data_bool))

#tipe data khusus

#bilangan kompleks
data_complex = complex(5,6)
print("data =", data_complex)
print("- bertipe =",type(data_complex))

#tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data =", data_c_double)
print("- bertipe =",type(data_c_double))
