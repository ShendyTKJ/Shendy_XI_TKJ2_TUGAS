from flet import *
import flet

################ TAMBAH TUGAS ITEM
class Tambah_ItemView(UserControl):
    def build(self):
        return Container(
            margin=margin.all(10),
            content=Row(
            controls=[
                TextField(
                    hint_text='Nama Tugas',
                    border_radius=70,
                    bgcolor='white',
                    height=50,
                ),

                TextField(
                    hint_text='Deskripsi Tugas Anda',
                    border_radius=50,
                    bgcolor='white',
                    height=150
                )
            ]
        )
    )

################### DAFTAR TUGAS
class DaftarTugas_ItemView(UserControl):
    def __init__(self, nama_tugas):
        super().__init__()
        self.nama_tugas = nama_tugas

    def build(self):
        return ElevatedButton(
            text=self.nama_tugas,
        )


############## PENTING TUGAS
class Penting_ItemView(UserControl):
    def __init__(self, nama_tugas) -> None:
        super().__init__()
        self.nama_tugas = nama_tugas
    
    def build(self):
        return ElevatedButton(
            text=self.nama_tugas
        )

############### TENGGAT TUGAS
class Tenggat_ItemView(UserControl):
    def __init__(self, nama_tugas):
        super().__init__()
        self.nama_tugas = nama_tugas

    def build(self):
        return ElevatedButton(
            text=self.nama_tugas
        )
    