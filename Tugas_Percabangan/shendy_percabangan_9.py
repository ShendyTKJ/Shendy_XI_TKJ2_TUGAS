#nama: shendy pratama n
#kelas: XI TKJ 2
#nomor absen: 27
#soal: Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek tersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyek diluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."

def evaluasi_proyek(status_persiapan):
    if status_persiapan.lower() == "siap":
        return "Proyek diluncurkan."
    elif status_persiapan.lower() == "tunda":
        return "Proyek ditunda."
    else:
        return "Status persiapan tidak valid."

status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ")

hasil_evaluasi = evaluasi_proyek(status_persiapan)
print(hasil_evaluasi)
