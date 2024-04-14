import flet as ft
import requests as req
def main(page: ft.Page):
    page.title = "VimeCheck"
    page.theme_mode  = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 450
    page.window_resizable = False
    def validate(e):
        if all([user_data.value]):
            bt_get.disabled = False
        else:
            bt_get.disabled = True
        page.update()
    def get_info(e):
        URL = f'https://api.vimeworld.com/user/name/{user_data.value}'
        response = req.get(URL).json()
        id_data.value = str(response[0]['id'])
        username_data.value = str(response[0]['username'])
        level.value = str(response[0]['level'])
        level_rank.value = str(response[0]['rank'])
        def rank_color(response):
            rank_nickname = response[0]['rank']
            if rank_nickname == 'VIP':
                rank_color = '#00be00'
            elif rank_nickname == 'PREMIUM':
                rank_color = '#00dada'
            elif rank_nickname == 'HOLY':
                rank_color = '#ffba2d'
            elif rank_nickname == 'IMMORTAL':
                rank_color = '#e800d5'
            else:
                rank_color = ' '
            return rank_color
        level_rank.color = rank_color(response)
        # print(response) - debug mode
        page.update()
    id_text = ft.Text('Айди игрока:')
    id_data = ft.Text('')
    username = ft.Text('Никнейм игрока:')
    username_data = ft.Text('')
    level_name = ft.Text('Уровень игрока:')
    level = ft.Text('')
    rank = ft.Text('Ранг игрока:')
    level_rank = ft.Text('', color='')
    user_data = ft.TextField(label= 'Никнейм игрока',width=350, on_change=validate)
    bt_get = ft.ElevatedButton(text='Поиск', on_click=get_info, disabled=True)
    def change_theme(e):
        user = page.navigation_bar.selected_index
        if user == 0:
            page.theme_mode = 'light'
        elif user == 1:
            page.theme_mode = 'dark'
        page.update()
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.WB_SUNNY_SHARP, label='Светлая тема'),
            ft.NavigationDestination(icon=ft.icons.MODE_NIGHT_SHARP, label='Темная тема')
        ], on_change=change_theme
    )
    page.add(
        ft.Row(
            [
                ft.Text('Айди игрока по его нику')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([id_text, id_data],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([username, username_data],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([level_name, level],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([rank, level_rank],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([bt_get],alignment=ft.MainAxisAlignment.CENTER)
    )
ft.app(target=main)