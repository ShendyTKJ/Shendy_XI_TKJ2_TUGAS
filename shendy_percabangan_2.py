#nama: shendy pratama n
#kelas: XI TKJ 2
#nomor absen: 27
#soal: Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. Jika


estimasi_selesai = input("Masukkan estimasi waktu selesai proyek (Tahun-Bulan-Tanggal): ")
tanggal_target_selesai = input("Masukkan tanggal target selesai (Tahun-Bulan-Tanggal): ")

if estimasi_selesai <= tanggal_target_selesai:
    print("Tepat waktu")
else:
    print("terlambat")    