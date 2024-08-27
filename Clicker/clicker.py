import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener as KeyboardListener, Key
from threading import Thread


class Clicker:
    def __init__(self):
        self.mouse = MouseController()
        self.clicking = False
        self.listener = KeyboardListener(on_press=self.toggle_clicking)
        self.listener.start()

    def toggle_clicking(self, key):
        if key == Key.space:
            if not self.clicking:
                self.clicking = True
                print("Started clicking")
                self.click_thread = Thread(target=self.click)
                self.click_thread.start()
            else:
                self.clicking = False
                print("Stopped clicking")
                self.click_thread.join()

    def click(self):
        while self.clicking:
            self.mouse.click(Button.left, 1)
            time.sleep(
                0.00000001)  # Adjust the sleep time to control the speed of
            # clicking

    def run(self):
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.listener.stop()


if __name__ == "__main__":
    clicker = Clicker()
    clicker.run()