# Nama : Shendy pratama n
# Kls : XI TKJ 2
# No : 27
# Soal : Deskripsi Pekerjaan: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari
#        jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa
#        apel kurang dari 20 buah.
#        Rumus: Sisa apel hari ke-n = Sisa apel hari ke-(n-1) - 10% dari Sisa apel hari ke-(n-1)


total_apel = 100
total_hari = 0

while total_apel >= 20:
    total_apel = total_apel - (total_apel * 10/100)
    total_hari = total_hari + 1

print(f'Untuk membuat sisa apel kurang dari 20 buah adalah : {total_hari} hari')