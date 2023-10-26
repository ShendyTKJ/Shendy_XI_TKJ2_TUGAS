#nama: surya
#kelas: XI TKJ 2
# nomor absen: 23
#soal: Buat program Python yang mengambil total belanjaan pelanggan dan memberikan diskon berdasarkan aturan berikut:
#Jika total belanjaan lebih dari 500.000, berikan diskon 10%.
#Jika total belanjaan antara 300.000 dan 500.000, berikan diskon 5%.
#Jika total belanjaan kurang dari 300.000, tidak ada diskon.

total_belanjaan = float(input("Total belanjaan Anda: "))
if total_belanjaan > 500000:
    diskon = total_belanjaan * 0.10
elif total_belanjaan >= 300000:
    diskon = total_belanjaan * 0.05
else:
    diskon = 0
total_pembayaran = total_belanjaan - diskon
print("Total pembayaran setelah diskon: {total_pembayaran}")
