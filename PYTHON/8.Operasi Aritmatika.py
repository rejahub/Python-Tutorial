#Operasi Aritmatika

a = 15
b = 5

#Operasi Tambah +
hasil = a + b
print(a,"+",b,"=", hasil)

#Operasi Pengurangan -
hasil = a - b
print(a,"-",b,"=", hasil)

#Operasi Perkalian *
hasil = a * b
print(a,"*",b,"=", hasil)

#Operasi Pembagian /
hasil = a/b
print(a,"/",b,"=", hasil)

#Operasi Eksponen (pangkat) **
hasil = a ** b
print(a,"**",b,"=", hasil)

#Operasi Modulus (Sisa Pembagian) %
hasil = a % b
print(a,"%",b,"=", hasil)

#Operasi Floor Divison //
hasil = a // b
print(a,"//",b,"=", hasil)

#Prioritas Operasi Operational Predence
'''
    1.()
    2.Eksponen **
    3.Perkalian dan teman - teman * / ** % //
    4.pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - z % x // y
print(x,"**",y,"*",z,'+',x,'/',y,'-',z,'%',x,"//",y,"=", hasil)

#Kurung akan mengambil langkah pertama
hasil = (x + y) * z
print('(',x,'+',y,') *',z,"=",hasil)