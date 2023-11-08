# Nama : Shendy pratama n
# Kls : XI TKJ 2
# No : 27
# Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan
#        dengan eksponen tertentu.
#        Rumus: Bilangan^Eksponen



def pangkat_dari_bilangan(bilangan, eksponen):
    return bilangan ** eksponen

input_bilangan = int(input("Masukkan Bilangan: "))
eksponen_bilangan = int(input("Masukkan Eksponen: "))

print(f"{input_bilangan} pangkat {eksponen_bilangan} : {pangkat_dari_bilangan(input_bilangan, eksponen_bilangan)}")