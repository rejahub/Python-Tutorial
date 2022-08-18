#operasi logika atau boolean

# not, or, and, xor

#NOT
print("===== NOT =====")
a = False
c = not a
print('data a =', a)
print('===== NOT') #kebalikan dari atas
print('data c =', c)

#OR (Jika satu nilai false, maka hasilnya true)
print("===== OR =====")
a = False
b = False
c = a or b
print(a,'or', b,'=', c)
a = False
b = True
c = a or b
print(a,'or', b,'=', c)
a = True
b = False
c = a or b
print(a,'or', b,'=', c)
a = True
b = True
c = a or b
print(a,'or', b,'=', c)

#AND (Jika dua buah niai true, maka hasilnya true)
print("===== AND =====")
a = False
b = False
c = a and b
print(a,'and', b,'=', c)
a = False
b = True
c = a and b
print(a,'and', b,'=', c)
a = True
b = False
c = a and b
print(a,'and', b,'=', c)
a = True
b = True
c = a and b
print(a,'and', b,'=', c)

#XOR (Akan true jika salah satu true, sisanya false)
print("===== XOR =====")
a = False
b = False
c = a ^ b
print(a,'xor', b,'=', c)
a = False
b = True
c = a ^ b
print(a,'xor', b,'=', c)
a = True
b = False
c = a ^ b
print(a,'xor', b,'=', c)
a = True
b = True
c = a and b
print(a,'xor', b,'=', c)