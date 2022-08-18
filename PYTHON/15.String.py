data = 'ini adalah string'
print(data)
print(type(data))

#1.Cara membuat String
'''
    1. Dengan menggunakan single quote '....'
    2. Dengan menggunakan double quote "...."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan single quote"
print(data)

print("'Halo Apa Kabar?'")
print('"Halo Apa Kabar?"')
print("Ini adalah hari jum'at")

#2. Menggunakan tanda \
print('Ini adalah hari jum\'at')
print('g\'day, is\'n it?')

#backslash
print("C:\\User\\Asro")

#Tab \t
print ('Aku Cinta\t\t Kamu!') #jadinya jauh

#backspace \b
print('Aku cintaa\b kamu') #jadinya dekat

#newline .\n atau .\r
print('baris pertama.\nbaris kedua.') #LF --> Line Feed, dipakai di UNIX(Linux,MacOS)
print('baris pertama.\rbaris kedua.') #CR --> Carrier Return, dipakai di Commodor, Lsp
print('baris pertama.\n\rbaris kedua.') #CRLF --> Line Feed Carrier Return, dipakai di Windows

#3.String Literal atau Raw r'....'

#hati - hati
print('C:\nnew folder') #akan salah path nya

#menggunakan raw string r
print(r'C:\new folder')

#menggunakan literal string
print('''
    Nama    : Ucup
    Kelas   : 3 SD
''')

#Menggunakan literal string dan raw
print(r'''
    Nama    : Ucup
    Kelas   : 3 SD/New Normal
    Path    : C:/New Folder
''')
