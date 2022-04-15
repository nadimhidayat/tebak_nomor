import random

def tebak(x):
    angka_tebak = random.randint(1, x)
    angka_pilih = 0
    while angka_pilih != angka_tebak :
        angka_pilih = int(input(f'Tebak angka antara 1 dan {x}: '))
        if angka_tebak < angka_pilih:
            print('Angkanya terlalu tinggi. Coba lagi!')
        elif angka_tebak > angka_pilih:
            print('Angkanya terlalu rendah. Coba lagi!')

    print(f'Betul! Angkanya adalah {angka_pilih}')

tebak(15)