# Nama : Shendy pratama n
# Kls : XI TKJ 2
# No : 27
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.
#        Rumus: Faktorial n = n * (n-1) * (n-2) * ... * 1



def factorial(a):
    if a < 0:
        return "Angka yang anda masukkan harus positif"
    elif a == 0:
        return 1
    else:
        return a * factorial(a - 1)

input_user = int(input("Masukkan Angka Faktorial: "))
print(f'Faktorial dari {input_user} = {factorial(input_user)}')