from PyQt5 import QtWidgets
from main_ui import Ui_MainWindow
import socket
import sys

host = "localhost"
port = 21037

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__": 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sfd:
        sfd.connect((host, port))
        sfd.sendall(b"author")
        data = sfd.recv(64)

    print(f"Received {data!r}")

    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())
