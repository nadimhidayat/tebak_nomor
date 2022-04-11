import random

def tebak(x):
    angka_tebak = random.randint(1, x)
    angka_pilih = 0
    while angka_pilih != angka_tebak:
        angka_pilih = int(input(f'Tebak angka antara 1 dan {x}: '))
        if angka_tebak < angka_pilih:
            print('Angkanya terlalu tinggi. Coba lagi!')
        elif angka_tebak > angka_pilih:
            print('Angkanya terlalu rendah. Coba lagi')

    print(f'Betul!! Angkanya adalah {angka_tebak}!')

def komputer_tebak(x):
    rendah = 1
    tinggi = x
    jawaban = ''
    while jawaban != 'b':
        if rendah != tinggi:
            angka_pilih = random.randint(rendah, tinggi)
        else:
            angka_pilih = rendah
        jawaban = input(f'Apakah {angka_pilih} lebih tinggi (t), lebih rendah(r), atau benar (b)?').lower()
        if jawaban == 't':
            tinggi = angka_pilih - 1
        elif jawaban == 'r':
            rendah = angka_pilih + 1

    print(f'Betul! angkanya adalah {angka_pilih}')


komputer_tebak(10)