import flet as ft
import requests

def main(page: ft.Page):
    # アプリのタイトルを設定
    page.title = "PicoW LED Controller"
    
    # 初期状態としてLEDはOFF
    led_state = False

    # テキスト入力とボタンを配置
    ip_input = ft.TextField(label="Enter PicoW IP Address", width=300)
    page.add(ip_input)

    # ボタンのテキストを設定する関数
    def update_button_text():
        return "LED ON" if not led_state else "LED OFF"

    # LEDのON/OFFを切り替える関数
    def toggle_led(e):
        nonlocal led_state
        ip_address = ip_input.value
        if ip_address:
            # LEDの状態に応じてONかOFFのリクエストを送信
            action = "on" if not led_state else "off"
            url = f"http://{ip_address}/{action}"
            try:
                response = requests.get(url)
                # LEDの状態を反転
                led_state = not led_state
                # ボタンのテキストを更新
                toggle_button.text = update_button_text()
                page.add(ft.Text(f"Sent {action.upper()} signal to {ip_address}: {response.text}"))
            except Exception as e:
                page.add(ft.Text(f"Error: {e}"))
        page.update()

    # 切り替えボタンを作成し、初期のテキストを設定
    toggle_button = ft.ElevatedButton(text=update_button_text(), on_click=toggle_led)
    
    # ボタンをページに追加
    page.add(toggle_button)
    page.update()

ft.app(target=main)

