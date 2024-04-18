import tkinter as tk
from datetime import datetime

class MessagingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Messaging App")
        self.root.minsize(200, 100)

        self.message_display = tk.Text(self.root, width=40, height=20)
        self.message_display.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.root, command=self.message_display.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.message_display.config(yscrollcommand=self.scrollbar.set)

        self.message_box_frame = tk.Frame(self.root)
        self.message_box_frame.pack(fill=tk.X)

        self.message_box = tk.Entry(self.message_box_frame, width=40)
        self.message_box.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.send_button = tk.Button(self.message_box_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self):
        message = self.message_box.get()
        if message:
            current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.message_display.insert(tk.END, f"{current_time}: {message}\n")
            self.message_box.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MessagingApp(root)
    root.mainloop()