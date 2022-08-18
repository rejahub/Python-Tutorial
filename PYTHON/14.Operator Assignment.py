#Operasi yang dapat dilakukan dengan penyingkatan
#operasi ditambah dengan assignment

a = 7 #ini adalah assignment
print('nilai a =', a)

a += 5 #ini artinya adalah a = a + 5
print('nilai a+= 5, nilai a menjadi', a)

a -= 2 #ini artinya adalah a = a - 2
print('nilai a -= 2, nilai a menjadi', a)

a *= 3 #ini artinya adalah a = a * 3
print('nilai a *= 3, nilai a menjadi', a)

a /= 10 #ini artinya adalah a = a / 10
print('nilai a /= 10, nilai a menjadi', a)


#Pangkat atau eksponen

b = 10
print('\nnilai b =', b)
b **= 4 #ini artinya adalah a = b ** 2
print('nilai a **= 2, nilai b menjadi', b)

#Modulus dan Floor division

b = 10
print('\nnilai b =', b)
b %= 3 #ini artinya adalah b = b % 3
print('nilai b %= 10, nilai b menjadi', b)

b = 10
print('\nnilai b =', b)
b //= 2 #ini artinya adalah b = b // 3
print('nilai b //= 2, nilai a menjadi', b)


#Operasi bitwise
#OR
c = True
print('\nnilai c =', c)
c|= False
print('nilai c|= False, maka nilai c =', c)

#AND
c = True
print('\nnilai c =', c)
c &= False
print('nilai c &= False, maka nilai c =', c)

#XOR
c = True
print('nilai c =', c)
c ^= False
print('nilai c ^= False, maka nilai c =', c)

#geser - geser
d = 0b0100
print('\nnilai d =', format(d,'04b'))
d >>=2
print('\nnilai d >>= 2, maka nilai d menjadi', format(d,"04b"))
d <<=1
print('\nnilai d <<= 1, maka nilai d menjadi', format(d,"04b"))