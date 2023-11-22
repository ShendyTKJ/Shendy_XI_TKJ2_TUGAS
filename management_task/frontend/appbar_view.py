import flet 
from flet import *


def appbar_widget(page):
    return AppBar(
            leading=Container(
                content= Text(
                value='Tasking',
                color=colors.WHITE,
                size=20
                ),
                # bgcolor=colors.RED,
                alignment=alignment.center,
                margin=margin.only(left=20)
            ),
            # margin=Margin(10,0,0,0),       
            leading_width=100,
            bgcolor=colors.BLUE_900,
            actions=[
                Container(
                    # width=self._page * 20 / 100,
                    # bgcolor=colors.WHITE,
                    # border_radius=100,
                    content=TextField(
                        prefix_icon=icons.SEARCH,
                        # hint_text='Search',
                        # hint_style=TextStyle(
                        #     color=colors.BLACK
                        # )
                        label='Cari Tugas Anda',
                        height=40,
                        border_radius=100,
                        bgcolor='white'
                    ),
                    margin=Margin(
                        left=10,
                        right=10,
                        bottom=10,
                        top=10
                    )
                      
                )
            ]
        )