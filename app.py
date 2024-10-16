import flet as ft
import requests

def main(page: ft.Page):
    # アプリのタイトルを設定
    page.title = "PicoW LED Controller"
    # 初期状態としてLEDはOFF
    led_state = False

    # テキスト入力とボタンを配置
    ip_input = ft.TextField(label="Enter Pico W IP Address", width=300)
    page.add(ip_input)

    # ボタンのテキストを設定する関数
    def update_button_text():
        return "Turn ON LED" if not led_state else "Turn OFF LED"

    # LEDのON/OFFを切り替える関数
    def toggle_led(e):
        nonlocal led_state
        ip_address = ip_input.value
        if not ip_address:
            page.snack_bar = ft.SnackBar(ft.Text("Please enter the IP address"))
            page.snack_bar.open = True
            page.update()
            return

        try:
            response = requests.get(f"http://{ip_address}/led", params={"state": int(not led_state)})
            response.raise_for_status()
            led_state = not led_state
            toggle_button.text = update_button_text()
            page.update()
        except requests.RequestException as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {ex}"))
            page.snack_bar.open = True
            page.update()

    # ボタンを作成してページに追加
    toggle_button = ft.ElevatedButton(text=update_button_text(), on_click=toggle_led)
    page.add(toggle_button)

# ft.app の呼び出し
ft.app(target=main)