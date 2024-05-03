import flet as ft
from flet import colors

def main(page: ft.page):
    page.bgcolor = '#fff'
    page.window_resizable = False
    page.window_width = 350
    page.window_height = 480
    page.title = 'Calculadora'
    page.window_always_on_top = True

    result = ft.Text(value = '0', color = colors.WHITE, size = 20)

    display =  ft.Row(
        width = 350,
        controls = [result],
        alignment = 'end'
    )

    page.add(display)

ft.app(target = main)