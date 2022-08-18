#operasi komparasi

#setiap hasil dari komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

#lebih besar dari >
print("======Lebih besar dari > =====")
hasil = a > 3
print (a,'>',3,'=', hasil)
hasil = b > 3
print (b,'>',2,'=', hasil)
hasil = b > 2
print (b,'>',2,'=', hasil)

#kurang dari <
print("======Lebih besar dari < =====")
hasil = a < 3
print(a,"<",3,"=", hasil)
hasil = b < 3
print(b,"<",3,"=", hasil)
hasil = b < 2
print(b,"<",2,"=", hasil)

#lebih besar sama dengan >=
print("======Lebih besar sama dengan >=======")
hasil = a >= 3
print(a,">=",3,'=', hasil)
hasil = b >= 3
print(b,">=",3,"=", hasil)
hasil = b >= 2
print(b,">=",2,"=", hasil)

#kurang dari sama dengan >=
print("======Kurang dari sama dengan >= ======")
hasil = a <= 3
print(a,"<=",3,'=', hasil)
hasil = b <= 3
print(b,"<=",3,"=", hasil)
hasil = b <= 2
print(b,"<=",2,"=", hasil)

#sama dengan ==
print("=====Sama dengan == =====")
hasil = a == 4
print(a,"==",4, hasil )
hasil = b == 4
print(b,"==",4, hasil)

#tidak sama dengan ==
print("=====Tidak sama dengan != =====")
hasil = a != 4
print(a,"!=",4, hasil )
hasil = b != 4
print(b,"!=",4, hasil)

# "is" sebagai komparasi object identity
print('===== Is sebagai komparasi Objek =====')
x = 5 #ini adalah assignment membuat objek
y = 5
print('nilai x =', x,', id =',hex(id(x)))
print('nilai y =', y,', id =', hex(id(x)))

hasil = x is 5
print('x is 5 =', hasil)

# "is not" sebagai komparasi object identity
print('===== Is not sebagai komparasi Objek =====')
x = 5 #ini adalah assignment membuat objek
y = 5
print('nilai x =', x,', id =',hex(id(x)))
print('nilai y =', y,', id =', hex(id(x)))

hasil = x is not 5
print('x is not 5 =', hasil)