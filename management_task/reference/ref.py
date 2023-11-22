import flet
from flet import *


class REF_TAMBAH_TUGAS_VIEW:
    LIST_VIEW = Ref[ListView]()

class ITEM_CONTROL_VIEW:
    CONTAINER_TAMBAH_TUGAS = Ref[Container]()
    CONTAINER_DAFTAR_TUGAS = Ref[Container]()
    CONTAINER_PENTING_TUGAS = Ref[Container]()
    CONTAINER_TENGGAT_TUGAS = Ref[Container]()
    CONTAINER_HOME = Ref[Container]()
