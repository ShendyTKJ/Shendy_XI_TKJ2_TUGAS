# Nama : Shendy pratama n
# Kls : XI TKJ 2
# No : 27
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.
#        Rumus: Jumlah digit dari bilangan n = jumlah dari setiap digit dalam n



def hitung_jumlah_digit_dari_bilangan(bilangan):
    jumlah_digit = 0

    for i in bilangan:
        if i.isdigit():
            jumlah_digit = jumlah_digit + int(i)
        else:
            return None

    return jumlah_digit

input_bilangan = input('Masukkan Digit Bilangan: ')
print(f'Jumlah digit dari {input_bilangan} adalah {hitung_jumlah_digit_dari_bilangan(input_bilangan)}')