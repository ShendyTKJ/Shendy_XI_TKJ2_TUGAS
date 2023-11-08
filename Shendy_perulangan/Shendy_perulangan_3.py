# Nama : Shendy pratama n
# Kls : XI TKJ 2
# No : 27
# Soal : Deskripsi Pekerjaan: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap
#        tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi
#        melebihi 20.000 dollar.
#        Rumus: Nilai investasi tahun ke-n = Nilai investasi tahun ke-(n-1) + 6% dari Nilai investasi tahun ke-(n-1)



total_investasi_awal = 10000
total_tahun = 0

while total_investasi_awal <= 20000:
    total_investasi_awal = total_investasi_awal + (total_investasi_awal * 6/100)
    total_tahun = total_tahun + 1

print(f'Total tahun yang diperlukan agar nilai investasi melebihi 20.000 dolar : {total_tahun} tahun')