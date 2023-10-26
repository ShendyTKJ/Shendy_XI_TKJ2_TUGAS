#nama: shendy pratama n
#kelas: XI TKJ 2
#nomor absen: 27
#soal: Buat program Python yang mengambil informasi pembaruan perangkat lunak dan menentukan apakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, program harus mencetak "Sistem perlu di-restart." Jika tidak, program harus mencetak "Sistem tidak perlu di-restart."

def periksa_pembaruan(pembaruan):
    if pembaruan.lower() == "yes" or pembaruan.lower() == "ya":
        return "Sistem perlu di-restart."
    else:
        return "Sistem tidak perlu di-restart."

pembaruan = input("Apakah Anda telah melakukan pembaruan perangkat lunak (yes/no)? ")

status_restart = periksa_pembaruan(pembaruan)
print(status_restart)
