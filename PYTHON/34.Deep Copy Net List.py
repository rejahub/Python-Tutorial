#Deep Copy Nested List

data_0 = [1,2]
data_1 = [3,4]
data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()
print("Data 2D = ", data_2D)
print("Data Copy = ",data_2D_copy)

#Mengambil data dari nested list

data = data_2D[1][0]
print("Data = ",data)

#address semuanya

print("Data 2D =",hex(id(data_2D)))
print("Data Copy = ", hex(id(data_2D_copy)))

print("Adress dari member ke-1")
print("Data 2D =",hex(id(data_2D[0])))
print("Data Copy = ", hex(id(data_2D_copy[0])))#maka hasil adressnya sama

data_2D[0][1] = 5
data_2D[2] = 9
print("Data 2D = ", data_2D)
print("Data Copy = ",data_2D_copy)

#Kita gunakan deep copy

from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print("Adress Asli = ", hex(id(data_2D)))
print("Adress Copy = ", hex(id(data_2D_copy)))

print("Adress dari member ke-1")
print("Data 2D =",hex(id(data_2D[0])))
print("Data Copy = ", hex(id(data_2D_copy[0])))

data_2D[0][1] = 30
print("Data 2D = ", data_2D)
print("Data Copy = ",data_2D_copy)
print("Data Deep = ",data_2D_deepcopy)