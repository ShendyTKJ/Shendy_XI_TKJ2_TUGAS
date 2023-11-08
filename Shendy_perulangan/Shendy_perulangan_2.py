# Nama : Shendy pratama n
# Kls : XI TKJ 2
# No : 27
# Soal : Deskripsi Pekerjaan: Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai
#        dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya. Buatlah program
#        yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10
#        kilometer.
#        Rumus: Jarak minggu ke-n = Jarak minggu ke-(n-1) + 10% dari Jarak minggu ke-(n-1)



awal_lari = 5
jumlah_minggu = 0

while awal_lari <= 10:
    awal_lari = awal_lari + (awal_lari * 10/100)
    jumlah_minggu = jumlah_minggu + 1

print(f'Pelari bisa menempuh jarak lebih dari 10 km, membutuhkan : {jumlah_minggu} minggu')