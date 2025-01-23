from PyQt5 import QtWidgets
from main_ui import Ui_MainWindow
import socket
import sys
import threading

host = "localhost"
PORT = 21037

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.get_servers)

    def get_servers(self):
        serv = discover_servers()
        self.ui.label_4.setText(str(len(serv)))


def discover_servers():
    print("Discovery start...")
    found_servers = []
    # subnet = "192.168.1."
    subnet = "127.0.0."

    def discover(ip):
        try:
            with socket.create_connection((ip, PORT), timeout=1) as sock:
                sock.sendall(b"HI SERVER")
                response = sock.recv(64).decode()
                if response == "HI CLIENT":
                    found_servers.append(ip)
        except Exception:
            pass

    threads = []
    for i in range(1, 2): # change to 255 after release
        ip = f"{subnet}{i}"
        thread = threading.Thread(target=discover, args=(ip,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if ( len( found_servers ) ):
        print(f"Found {len( found_servers )} servers:")
        for server in found_servers:
            print(f"- {server}")

    return found_servers


if __name__ == "__main__": 
    found_servers = []
    if ( True ):
        app = QtWidgets.QApplication(sys.argv)
        application = ApplicationWindow()
        application.show()
        sys.exit(app.exec_())

