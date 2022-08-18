###Type Hints Pada Fungsi###

#Bentuk Standar Fungsi yang telah kita pelajari

#Studi Kasus
#def fungsi(parameter):
#    """Fungsi dengan argument parameter"""
    #hasil = parameter**2
    #print(parameter)
#fungsi(1)
#fungsi("Asro")#error karena string tak dapat dibaca oleh integer parameter
# fungsi(True)

#Penggunaan Type Hints

import string


def lima_pangkat(argument:int) -> int:
    """Fungsi dengan Hints"""
    output = 5**argument
    return output

HASIL = lima_pangkat(3)
print(HASIL)

def display(argument:string):
    print(argument)

display("Asro")