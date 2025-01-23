from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QColor
from main_ui import Ui_MainWindow
import socket
import sys
import threading
import re

host = "localhost"
PORT = 21037

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        #self.setStyle(QtWidgets)
        self.ui.setupUi(self)
        self.ui.SearchButton.clicked.connect(self.get_servers)
        self.ui.getLocalAddr.clicked.connect(self.get_local_addr)
        self.ui.AddrEdit.setMaxLength(12)


    def get_servers(self):
        AddrEditPalette = self.ui.AddrEdit.palette()

        subnet = self.ui.AddrEdit.text()
        
        if ( not re.match("^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){3}$", subnet)):
            AddrEditPalette.setColor(QPalette.Base, QColor("red"))
            self.ui.AddrEdit.setPalette(AddrEditPalette)
            self.print_status(f"{subnet} is incorrect subnet!")
            return
        
        self.print_status(f"Discovering {subnet} subnet...")
        AddrEditPalette.setColor(QPalette.Base, QColor("white"))
        self.ui.AddrEdit.setPalette(AddrEditPalette)
        serv = discover_servers(subnet)
        self.print_status(f"Found {len(serv)} servers.")
        self.ui.FoundHosts_label.setText(str(len(serv)))
        if len(serv):
            self.append_hosts(serv)

    def get_local_addr(self):
        net = socket.gethostbyname(socket.gethostname())
        net = '.'.join(net.split('.')[0:-1])
        self.ui.AddrEdit.setText(net)

    def print_status(self, status_text: str):
        if len(status_text):
            self.ui.StatusInfoBox.append(status_text)

    def append_hosts(self, hosts: list):
        for server in hosts:
            self.ui.FoundHosts_list.addItem(server)


def discover_servers(subnet: str = "127.0.0"):
    found_servers = []

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
        ip = f"{subnet}.{i}"
        thread = threading.Thread(target=discover, args=(ip,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return found_servers


if __name__ == "__main__": 
    found_servers = []
    if ( True ):
        app = QtWidgets.QApplication(sys.argv)
        application = ApplicationWindow()
        application.show()
        sys.exit(app.exec_())

