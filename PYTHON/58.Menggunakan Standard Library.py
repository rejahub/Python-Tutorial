###Standard Libarary###

import datetime
from itertools import count
from re import A, M
data_waktu = datetime.datetime.now()
print(f"Datetime now : {data_waktu}")
print(f"Tahun : {data_waktu.year}")
print(f"Bulan : {data_waktu.strftime('%m')}")
print(f"Hari : {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a","b","c","d","a","d","e"]
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"data count a = {data_count['a']}")#mengambil a saja

#Cara Panjangnya
count = 0
for i in data:
    if i == "a":
        count += 1

print(count)

import io

file = io.open("file_text.txt","r")
print(file.read())