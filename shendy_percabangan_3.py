#nama: shendy pratama n
#kelas: XI TKJ 2
#nomor absen: 27
#soal: Buat program Python yang memeriksa apakah suatu file sudah ada di direktori server. Jika file sudah

nama_file = "data.txt"
daftar_file_di_server = ["file1.txt", "file2.txt", "data txt", "file3.txt"]

if nama_file in daftar_file_di_server:
    print("File sudah ada")
else:
    print("File belum ada")