# Nama : SHENDY PRATAMA N
# Kls : XI TKJ 2
# No : 27
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga
#        batas tertentu yang ditentukan pengguna.
#        Rumus: Total deret bilangan ganjil = 1 + 3 + 5 + ... + (2n-1)


def total_deret_bilangan_ganjil():
    input_user = int(input('Masukkan angka batas: '))

    list_bilangan_ganjil = []

    for i in range(input_user + 1):
        if i % 2 == 1:
            list_bilangan_ganjil.append(i)

    return sum(list_bilangan_ganjil)

print(f'Total deret bilangan ganjil : {total_deret_bilangan_ganjil()}')