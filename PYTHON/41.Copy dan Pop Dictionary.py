#Copy dan Pop Dictionary#

data_dict = {
    'key':'value',
    'ri':'Asri',
    'ro':'Asro',
    'ra':'Andra'
}

friends = data_dict.copy() #yang berubah hanya data_dict
print("Data Dict =", data_dict)
print("friends = ",friends)

data_dict['ro'] = "Asro Si Pemberani"
print("Data Dict =", data_dict)
print("friends = ",friends)

friends = data_dict #kerefence yang sama
print("Data Dict =", data_dict)
print("friends = ",friends)

data_dict['ro'] = "Asro Si Pemberani"
print("Data Dict =", data_dict)
print("friends = ",friends)

#Pop Dictionary
dataAsro = data_dict.pop('ro')
print("dataAsro =",dataAsro)
print("friends =",friends)

#popitem Dictionary
dataTerakhir = friends.popitem()
print("data terakhir",dataTerakhir)
print("friends =",friends)

