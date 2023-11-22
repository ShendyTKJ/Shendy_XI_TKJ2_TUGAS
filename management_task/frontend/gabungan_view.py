from flet import *
import flet
from frontend.sidebar_view import SideBar
from frontend.content_view import *
from reference.ref import *

def show_content_merge(page):
    return Container(
        height=page.height,
        # bgcolor=colors.RED,
        # expand=True,
        content=Row(
            # expand=True,
            controls=[
                # Container(
                #     bgcolor='green',
                #     width=50,
                #     height=50
                # ),
                SideBar(
                    page
                    # width=page.width * 20 / 100,
                ),
                Container(
                    margin=margin.only(top=10),
                    # width=page.width * 80 / 100,
                    # bgcolor=colors.GREY_300,
                    expand=True,
                    content=Stack(
                        controls=[
                            # page_tenggat(),
                            # page_penting(),
                            # page_daftar_tugas(),
                            # page_tambah_tugas(),
                            # page_home()
                            
                            ITEM_CONTROL_VIEW.CONTAINER_TENGGAT_TUGAS.current,
                            ITEM_CONTROL_VIEW.CONTAINER_PENTING_TUGAS.current,
                            ITEM_CONTROL_VIEW.CONTAINER_DAFTAR_TUGAS.current,
                            ITEM_CONTROL_VIEW.CONTAINER_TAMBAH_TUGAS.current,
                            ITEM_CONTROL_VIEW.CONTAINER_HOME.current
                        ]
                    )
                )
            ]
        ),
    )
