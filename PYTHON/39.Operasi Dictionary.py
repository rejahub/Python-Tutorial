#Operator Dictionary
data_list = ["Asri","Asro","Andra","Tarmizi"]
data_dict = {
    'key':'value',
    'ro':'Asro',
    'ri':'Asri',
    'ra':'Andra',
    'nmbr' : 900,
}

#Panjang dictionary
Lendict = len(data_dict)
print("Panjang Dictionary =", Lendict)

#Mengecek key exist atau tidak
Key = "ri"
checkkey = Key in data_dict
print(f"Apakah {Key} ada di dict: {checkkey}")#True

Key = "ro"
checkkey = Key in data_dict
print(f"Apakah {Key} ada di dict: {checkkey}")#False

#Mengakses Value (read) dengan get
print(data_dict['ri'])
print(data_dict.get('ri'))
print(data_dict.get('ro','key tidak ditemukan'))#cek key dengan message none(tidak ditemukan)

#Mengupdate data 
data_dict['ro'] ='Asro Si Pemberani'
print(data_dict)
data_dict['ri'] = 'Asri Si Cerdas'
print(data_dict)

data_dict.update({'ro':'Asro'})#eksisting
print(data_dict)
data_dict.update({'ra':' Andra Pengacara Kece'})#kalau gak ada di add aja
print(data_dict)

#delete
del data_dict['ri']
print(data_dict)