# Nama : Shendy pratama n
# Kls : XI TKJ 2
# No : 27
# Soal : Deskripsi Pekerjaan: Seorang petani memiliki 100 ekor ayam di peternakannya. Setiap bulan, jumlah
#        ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung
#        berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.
#        Rumus: Jumlah ayam bulan ke-n = Jumlah ayam bulan ke-(n-1) + 5% dari Jumlah ayam bulan ke-(n-1)


jumlah_ayam_awal = 100
total_bulan = 0

while jumlah_ayam_awal <= 200:
    jumlah_ayam_awal = jumlah_ayam_awal + (jumlah_ayam_awal * 5/100)
    total_bulan = total_bulan + 1

print(f"Total bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor : {total_bulan} bulan")