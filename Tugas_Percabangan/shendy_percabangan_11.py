#nama: shendy pratama n
#kelas: XI TKJ 2
#nomor absen: 27
#soal: Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagai performa terbaik) dan menghitung bonus tahunan berdasarkan aturan berikut:
#Performa 5: Bonus 20% dari gaji tahunan.
#Performa 4: Bonus 10% dari gaji tahunan.
#Performa 3: Bonus 5% dari gaji tahunan.
#Performa 2: Bonus 2% dari gaji tahunan.
#Performa 1: Tidak ada bonus.
#Buatlah program menggunakan percabangan ternary untuk menghitung bonus tersebut.

def hitung_bonus(performa, gaji_tahunan):
    bonus = (
        0.20 * gaji_tahunan if performa == 5 else
        0.10 * gaji_tahunan if performa == 4 else
        0.05 * gaji_tahunan if performa == 3 else
        0.02 * gaji_tahunan if performa == 2 else
        0
    )
    return bonus

performa = int(input("Masukkan nilai performa karyawan (1-5): "))
gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

bonus = hitung_bonus(performa, gaji_tahunan)
print(f"Bonus tahunan yang diterima: {bonus:.2f}")
