#kita belajar Casting
#merubah dari satu tipe ke tipe lain
#tipe data = int,float,str,bool

#INTEGER
print("===INTEGER===")
data_int = 1
print("data =", data_int,", type =",type(data_int))
data_float = float(data_int)
print("data =", data_float,", type =",type(data_float))
data_str = str(data_int)
print("data =", data_str,", type =",type(data_str))
data_bool = bool (data_int) #akan false jika int = 0
print("data =", data_bool,", type =",type(data_bool))

#FLOAT
print("===FLOAT===")
data_float = 9.5
data_float = float(data_float)
print("data =", data_float,", type =",type(data_float))
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool (data_float) #akan false jika int = 0
print("data =", data_int,", type =",type(data_int))
print("data =", data_str,", type =",type(data_str))
print("data =", data_bool,", type =",type(data_bool))

#BOOLEAN
print("===BOOLEAN===")
data_bool = True
data_float = float(data_bool)
print("data =", data_bool,", type =",type(data_bool))
data_int = int(data_bool) #akan dibulatkan kebawah
data_str = str(data_bool)
data_float = float (data_bool) #akan false jika int = 0
print("data =", data_int,", type =",type(data_int))
print("data =", data_str,", type =",type(data_str))
print("data =", data_float,", type =",type(data_float))

#STRING
print("===STRING===")
data_str = ""
data_str = str(data_str)
data_bool = bool (data_str) #false jika string kosong
print("data =", data_str,", type =",type(data_str))
print("data =", data_bool,", type =",type(data_bool))