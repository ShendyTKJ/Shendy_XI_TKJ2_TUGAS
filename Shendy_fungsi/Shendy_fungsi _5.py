# Nama : Shendy pratama n
# Kls  : XI TKJ 2
# No : 27
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.
#        Rumus: Bilangan Fibonacci ke-n = Bilangan Fibonacci ke-(n-1) + Bilangan Fibonacci ke-(n-2)



def fibonacci(bilangan):
    if bilangan <= 0:
        return 0
    elif bilangan == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, bilangan + 1):
            a, b = b, a + b
        return b



input_bilangan = int(input('Masukkan Angka Fibonacci: '))
print(f'Bilangan fibonacci dari {input_bilangan} = {fibonacci(input_bilangan)}')