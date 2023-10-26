#nama: shendy pratama n
#kelas: XI TKJ 2
#nomor absen: 27
#soal: Buat program Python yang mengambil total belanjaan dan status anggota (biasa atau premium).
#Berikan diskon berdasarkan aturan berikut:
#Anggota premium: Jika total belanjaan lebih dari 500.000, berikan diskon 15%. Jika tidak, berikan diskon 10%.
#Anggota biasa: Jika total belanjaan lebih dari 300.000, berikan diskon 7%. Jika tidak, berikan diskon 0%.

def hitung_diskon(total_belanjaan, status_anggota):
    if status_anggota == "premium":
        if total_belanjaan > 500000:
            diskon = total_belanjaan * 0.15
        else:
            diskon = total_belanjaan * 0.10
    else:  # status_anggota == "biasa"
        if total_belanjaan > 300000:
            diskon = total_belanjaan * 0.07
        else:
            diskon = 0

    return diskon

total_belanjaan = float(input("Masukkan total belanjaan: "))
status_anggota = input("Masukkan status anggota (premium/biasa): ")

diskon = hitung_diskon(total_belanjaan, status_anggota)

if diskon > 0:
    print(f"Diskon yang diberikan: Rp {diskon:.2f}")
else:
    print("Maaf, tidak ada diskon yang diberikan.")
