#nama: shendy pratama n
#kelas: XI TKJ 2
#nomor absen: 27
#soal:Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori produk berdasarkan penjualan:
#Jika penjualan lebih dari 1000 unit, kategorikan sebagai "Produk Terlaris."
#Jika penjualan antara 500 hingga 1000 unit, kategorikan sebagai "Produk Populer."
#Jika penjualan kurang dari 500 unit, kategorikan sebagai "Produk Biasa."

def kategorikan_produk(penjualan):
    if penjualan > 1000:
        kategori = "Produk Terlaris"
    elif penjualan >= 500:
        kategori = "Produk Populer"
    else:
        kategori = "Produk Biasa"
    return kategori

penjualan = int(input("Masukkan jumlah penjualan bulanan produk: "))

kategori_produk = kategorikan_produk(penjualan)
print(f"Kategori produk: {kategori_produk}")
