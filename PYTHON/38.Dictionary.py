#List -> Array, mengakses dengan 
# #menggunakan index

data_list = ["Asri","Asro","Andra","Tarmizi"]

print(data_list[3])


#dictionary (dict) -> assosiative array
#identifier -> key

data_dictionary = {
    'key':'value',
    'ri':'Asri',
    'ro':'Asro',
    'zi':'Tarmizi',
    'nmbr' : 900,
    'list':data_list
}
print("Key Asri adalah", data_dictionary['ri'])
print("Key Number adalah", data_dictionary['nmbr'])
print("Key List adalah", data_dictionary['list'])
