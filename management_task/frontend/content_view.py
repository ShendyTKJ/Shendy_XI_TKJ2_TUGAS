from flet import *
import flet
from frontend.item_control_view import *
from reference.ref import *

#TAMBAH TUGAS PAGE
def page_tambah_tugas():
    Container(
            ref=ITEM_CONTROL_VIEW.CONTAINER_TAMBAH_TUGAS,
            content=ListView(
            expand=True,
            controls=[
                Text("PAGE TAMBAH TUGAS")
            ]
        ),
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        expand=True,
        bgcolor=colors.GREEN_300,
    )

    # page.add(ITEM_CONTROL_VIEW.CONTAINER_TAMBAH_TUGAS.current)

    return ITEM_CONTROL_VIEW.CONTAINER_TAMBAH_TUGAS.current
    

def page_daftar_tugas():
    Container(
        ref=ITEM_CONTROL_VIEW.CONTAINER_DAFTAR_TUGAS,
        content=ListView(
            expand=True,
            controls=[
                Text("PAGE DAFTAR TUGAS")
            ]
        ),
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        expand=True,
        bgcolor=colors.GREEN_300,
    )

    # page.add(ITEM_CONTROL_VIEW.CONTAINER_DAFTAR_TUGAS.current)

    return ITEM_CONTROL_VIEW.CONTAINER_DAFTAR_TUGAS.current

def page_penting():
    Container(
        ref=ITEM_CONTROL_VIEW.CONTAINER_PENTING_TUGAS,
            content=ListView(
            expand=True,
            controls=[
                Text("PAGE PENTING")
            ]
        ),
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        expand=True,
        bgcolor=colors.GREEN_300,
    )

    # page.add(ITEM_CONTROL_VIEW.CONTAINER_PENTING_TUGAS.current)

    return ITEM_CONTROL_VIEW.CONTAINER_PENTING_TUGAS.current

def page_tenggat():
    Container(
        ref=ITEM_CONTROL_VIEW.CONTAINER_TENGGAT_TUGAS,
        content=ListView(
            expand=True,
            controls=[
                Text("PAGE TENGGAT")
            ],
        ),
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        expand=True,
        bgcolor=colors.GREEN_300,
    )

    # page.add(ITEM_CONTROL_VIEW.CONTAINER_TENGGAT_TUGAS.current)

    return ITEM_CONTROL_VIEW.CONTAINER_TENGGAT_TUGAS.current


def page_home():
    Container(
        ref=ITEM_CONTROL_VIEW.CONTAINER_HOME,
        content=ListView(
        expand=True,
        ),
        offset=transform.Offset(0,0),
        animate_offset=animation.Animation(500, AnimationCurve.DECELERATE),
        bgcolor=colors.GREY_300
    )

    # page.add(ITEM_CONTROL_VIEW.CONTAINER_HOME.current)

    return ITEM_CONTROL_VIEW.CONTAINER_HOME.current
