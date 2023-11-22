from flet import *
import flet as ft

from frontend.appbar_view import appbar_widget
# from frontend.sidebar_view import SideBar
from frontend.gabungan_view import show_content_merge


def main(page: Page):
    # print(type(AppBarWidget))
    page.appbar = appbar_widget(page)

    page.add(
        show_content_merge(page)
        # Text("Hello World")
    )

    #TODO : SAAT ICON TAMBAH TUGAS DIKLIK HARUSNYA DI LISTVIEW, ISI KONTENNYA DI CLEAR() DULU DAN DI TAMBAH DENGAN ISI SESUAI YANG DIPENCET. MISAL TAMBAH TUGAS YANG DIPENCET MAKA MEMANGGIL TAMBAHTUGAS_ITEMVIEW. KITA AKAN MENYIMPANNYA DALAM LIST. TAPI MASALAHNYA JIKA ICON TAMBAH TUGAS DIKLIK LAGI, MAKA ISI KONTEN AKAN MENGHILANG. OLEH KARENA ITU LAKUKAN PENGECEKAN TERLEBIH DAHULU APAKAH ITEM TERAKHIR DI LIST ADALAH TAMBAH JADWAL, JIKA IYA BUAT LAGI. JIKA BUKAN, BUAT KOSONGAN


ft.app(target=main)
