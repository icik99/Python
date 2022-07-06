import random

#user menebak angka random dari komputer
def tebak(x):
    angka_random = random.randint(1, x)
    tebak = 0

    while tebak != angka_random:
        tebak = int(input(f'Tebak angka antara 1 sampai {x}: '))
        if tebak < angka_random:
            print ('Salah, angka terlalu kecil')
        elif tebak > angka_random:
            print ('Salah, angka terlalu besar')

    print (f'Selamat, angka yang ditebak adalah {tebak} dan itu benar')


#komputer menebak angka random dari user
print ('PROGRAM TEBAK ANGKA, PILIH ANGKA RANDOM DARI 1 - 1000,\nKOMPUTER AKAN MENEBAK ANGKA TERSEBUT ')
def tebak_komputer(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            tebak = random.randint(low, high)
        else:
            tebak = low #bisa juga high, krn low = high
        feedback = input(f'apakah {tebak} terlalu tinggi (h), terlalu rendah (l), atau benar (c)? : ').lower()
        if feedback == 'h':
            high = tebak - 1
        elif feedback == 'l':
            low = tebak + 1
    print (f'Yey, komputer berhasil menebak angka kalian yaitu {tebak}')

tebak_komputer(1000)
