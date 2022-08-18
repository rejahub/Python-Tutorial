#Operasi Bitwise, Biner, dan Binary

a = 9
b = 5

#bitwise OR (\)
c = a|b

print('\n======OR=====')
print('nilai :',a,' , binary :', format(a,'08b'))
print('nilai :',b,' , binary :', format(b,'08b'))
print('------------------------------(|)')
print('nilai :',c,' , binary :', format(c,'08b'))

#bitwise AND (&)
c = a & b
print('\n=======AND=======')
print('nilai a :',a,' , binary :', format(a, '08b'))
print('nilai b :',a,' , binary : ', format(b, '08b'))
print('------------------------------(&)')
print('nilai c :',c,', binary : ', format(c, '08b'))

#bitwise XOR (^)
c = a ^ b
print('\n=======XOR=======')
print('nilai a :',a,' , binary :', format(a, '08b'))
print('nilai b :',b,' , binary : ', format(b, '08b'))
print('------------------------------(^)')
print('nilai c :',c,', binary : ', format(c, '08b'))

#bitwise NOT (~)
c = ~a 
print('\n=======NOT=======')
print('nilai a :',a,' , binary :', format(a, '08b'))
print('------------------------------(~)')
print('nilai c :',c,', binary : ', format(c, '08b'))
print('------------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :', e^d,' , binary : ',format(e^d,'08b'))

#Shifting

#Shift Right(>>)
c = a >> 1
print('\n======= >> =======')
print('nilai a :',a,' , binary :', format(a,'08b'))
print('------------------------------(>>)')
print('nilai c :',c,', binary : ', format(c,'08b'))

#Shift Left(<<)
c = a << 1
print('\n======= << =======')
print('nilai a :',a,' , binary :', format(a,'08b'))
print('------------------------------(<<)')
print('nilai c :',c,', binary : ', format(c,'08b'))
