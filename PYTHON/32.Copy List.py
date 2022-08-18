##=====Copy di List======##

a = ["Asri", "Asro", "Andra"]
print("a = ", a)

b = a
print("b = ", b)

#Merubah member dari a

#Ini akan merubah kedua list
a[1] = "Sahril"
b.sort()
print("a = ", a)
print("b = ", b)

#Adress dari kedua list a dan b
print("Adress a = ", hex(id(a)))
print("Adress b = ", hex(id(b)))

#Menduplikat list dengan copy
print("Membuat list c dengan copy a()")
c = a.copy() #full duplikat
print("Adress a = ", hex(id(a)))
print("Adress b = ", hex(id(b)))
print("Adress c = ", hex(id(c)))

print("a",a)
print("b",b)
print("c",c)

print("Kita ubah data 0")
c[1] = "Carles"

print("a =",a)
print("b =",b)
print("c =",c)
