#Episode Inpput User

#data yang dimasukkan pasti string
data = input("Masukkan data=")

print("data =",data,",type =",type(data))

#Jika ingin mengambil int, maka :
data_int = int(input("Masukkan angka :"))

print("data =",data_int,",type =",type(data_int))

#Jika ingin mengambil float, maka :
data_float = float(input("Masukkan angka"))

print("data=",data_float, "type =", type(data_float))

#Jika ingin mengambil boolean, maka :
data_bool = bool(input("Masukkan nilai boolean ="))

print("data=", data_bool, "type =",type(data_bool))