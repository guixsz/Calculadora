import flet as ft
from flet import colors

botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '+-', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
]

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

    btn = [ft.Container(
        content = ft.Text(value=btn['operador'], color=btn['fonte']),
        width = 70,
        height = 70,
        bgcolor = btn['fundo'],
        border_radius = 100,
        alignment = ft.alignment.center,
    )   for btn in botoes]

    keyboard = ft.Row(
        width = 420,
        wrap = True,
        controls = btn,
        alignment =  'end'
    )

    page.add(display,keyboard)

ft.app(target = main)