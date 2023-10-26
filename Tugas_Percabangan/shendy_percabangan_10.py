#nama: shendy pratama n
#kelas: XI TKJ 2
#nomor absen: 27
#soal: Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenispinjaman berdasarkan aturan berikut:
#Peminjaman 7 hari atau kurang: "Peminjaman Pendek"
#Peminjaman lebih dari 7 hari hingga 30 hari: "Peminjaman Menengah"
#Peminjaman lebih dari 30 hari: "Peminjaman Panjang"

def jenis_pinjaman(durasi):
    if durasi <= 7:
        return "Peminjaman Pendek"
    elif durasi <= 30:
        return "Peminjaman Menengah"
    else:
        return "Peminjaman Panjang"

durasi_peminjaman = int(input("Masukkan durasi peminjaman buku dalam hari: "))

jenis = jenis_pinjaman(durasi_peminjaman)
print(f"Jenis pinjaman: {jenis}")
