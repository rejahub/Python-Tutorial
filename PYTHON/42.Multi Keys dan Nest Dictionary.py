#Multi Keys dan Nest Dictionary

import datetime
mahasiswa1 = {
    'Nama': 'Asri',
    'Nim': '221000',
    'SKS_lulus': 120,
    'Beasiswa': False,
    'lahir': datetime.datetime(1995,5,12)
}

print(mahasiswa1)

mahasiswa2 = {
    'Nama': 'Asro',
    'Nim': '221001',
    'SKS_lulus': 130,
    'Beasiswa': True,
    'lahir': datetime.datetime(1997,6,10)
}

print(mahasiswa2)

mahasiswa3 = {
    'Nama': 'Andra',
    'Nim': '221003',
    'SKS_lulus': 120,
    'Beasiswa': True,
    'lahir': datetime.datetime(1998,5,11)
}

print(mahasiswa3)

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3

}

print('='*57)

print(f"{'KEY':<6} {'Nama':<17} {'Nim':<9} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")

print('='*57)

for mahasiswa in data_mahasiswa:
    
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['Nama']
    NIM = data_mahasiswa[KEY]['Nim']
    SKS = data_mahasiswa[KEY]['SKS_lulus']
    BEASISWA = data_mahasiswa[KEY]['Beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")#menampilkan semua tanggal lahir

    print(f"{KEY:<6} {NAMA:<17} {NIM:<9} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")