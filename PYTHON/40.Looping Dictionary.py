#Looping Dictionary

data_dict = {
    'key':'value',
    'ro':'Asro',
    'ri':'Asri',
    'ra':'Andra'
}

#Looping 1

for t in data_dict:
    print(t)

#Operator untuk mengambil item/Iterables
keys = data_dict.keys()
print(keys)

for key in data_dict.keys():
    print(data_dict.get(key))#mau ngambil key

values = data_dict.values()#mau ngambil value
print(values)
for value in values:
    print(value)

items = data_dict.items()#mau ngambil item saja
print(items)
for item in items:
    print(item)

for key,value in data_dict.items():
    print("key =",key, "value =",value)#mau ngambil pisahhh