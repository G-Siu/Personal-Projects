import pyautogui
import time

while True:
    time.sleep(3)
    x, y = pyautogui.position()
    px = pyautogui.pixel(x, y)
    print(px)
