from pynput import mouse
import pyautogui
from pynput.keyboard import Key, Listener


def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        px = pyautogui.pixel(x, y)
        print(px)


def on_press(key):
    if key == Key.esc:
        return False


listener = mouse.Listener(on_click=on_click)
listener.start()

with Listener(on_press=on_press) as keyboard_listener:
    keyboard_listener.join()