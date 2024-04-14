import flet as ft
import requests as req
import time

def main(page: ft.Page):
    page.title = "VimeCheck"
    page.theme_mode  = 'dark'
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

        try:
            response = req.get(URL).json()
            # print(response)
            if not response:
                # Если ответ пустой, выводим сообщение об ошибке
                bt_get.text = 'Неверный Ник!'
                bt_get.color = 'red'
                page.update()  # Обновляем страницу, чтобы изменения отобразились

                # Ждем 2 секунды
                time.sleep(2)

                # Возвращаем исходный текст кнопки
                bt_get.text = 'Получить информацию'
                bt_get.color = ''
                page.update()  # Обновляем страницу снова
                return
            else:
                bt_get.color = 'green'
                bt_get.text = 'Успешно!'
                page.update()
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
            
            page.update()
            time.sleep(2)
            bt_get.color = ''
            bt_get.text = 'Получить информацию'
            page.update()

        except req.RequestException as e:
            # Обработка ошибки при выполнении запроса (например, проблема с соединением)
            print("Ошибка при выполнении запроса:", e)
        except Exception as e:
            # Обработка других исключений
            print("Произошла неожиданная ошибка:", e)    

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
        if page.theme_mode == 'dark':
            page.theme_mode = 'light'
            bt_change_theme.icon = ft.icons.MODE_NIGHT_ROUNDED
        else:
            page.theme_mode = 'dark'
            bt_change_theme.icon = ft.icons.SUNNY
        page.update()
        
    bt_change_theme = ft.IconButton(ft.icons.WB_SUNNY_SHARP, on_click=change_theme)


    page.add(
        ft.Row(
            [
                bt_change_theme
            ],vertical_alignment=ft.MainAxisAlignment.SPACE_EVENLY, alignment=ft.MainAxisAlignment.END
        ),
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