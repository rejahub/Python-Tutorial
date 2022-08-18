#Width dan Multiline

#Data
data_nama = "Asro Siregar"
data_umur = 24
data_tinggi = 160.5
data_nomor_sepatu = 38

#string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print(5*"="+"data_string"+5*"=")
print(data_string)

#string multiline
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print(5*'=' + "data_string" + 5*'=')
print(data_string)

#String Multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
nomor sepatu = {data_nomor_sepatu}
"""
print(5*'=' + "data_string" + 5*'=')
print(data_string)

#Mengatur Lebar
data_nama = "Asro Siregar"
data_tinggi = 160.5
data_string = f"""
nama            =  {data_nama}
umur            =  {data_umur}
tinggi          =  {data_tinggi}
nomor sepatu    =  {data_nomor_sepatu}
"""
print(5*'=' + "data_string" + 5*'=')
print(data_string)