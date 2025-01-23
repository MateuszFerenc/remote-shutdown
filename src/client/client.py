from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPalette, QColor
from main_ui import Ui_MainWindow
import socket
import sys
import threading
import re
# import requests

host = "localhost"

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.SearchButton.clicked.connect(self.get_servers)
        self.ui.getLocalAddr.clicked.connect(self.get_local_addr)
        self.ui.TestHosts_button.clicked.connect(self.test_hosts)
        self.ui.DisableHosts_button.clicked.connect(self.disable_hosts)
        self.ui.ShutdownHosts_button.clicked.connect(self.shutdown_hosts)
        self.ui.SelectAll_button.clicked.connect(self.selectAllHosts)
        self.ui.UnselectAll_button.clicked.connect(self.unselectAllHosts)
        self.ui.SelectRange_button.clicked.connect(self.selectRange)
        self.ui.SelectOne_button.clicked.connect(self.selectOne)
        # self.ui.AddrEdit.installEventFilter(self)
        self.ui.progressBar.setValue(0)

        self.hosts = []
        self.port = ""
        self.selected_hosts = []
        self.selectCheckBoxes = (self.ui.SelectOne_checkBox, self.ui.SelectRange_checkBox, self.ui.SelectAllActive_checkBox)

        for cb in self.selectCheckBoxes:
            cb.setStyleSheet("""
                QCheckBox::indicator {
                    background-color: lightgrey;
                    border: 2px solid darkgrey;
                }
                QCheckBox::indicator:checked {
                    background-color: green;
                }
            """)

    # def eventFilter(self, widget, event):
    #     if (event.type() == QtCore.QEvent.Type.KeyPress and widget is self.ui.AddrEdit ):
    #         key = event.key()
    #         if key == QtCore.Qt.Key.Key_Return:
    #             print('return')
    #         elif key == QtCore.Qt.Key.Key_Enter:
    #             print('enter')
    #         return True
    #     return super().eventFilter(widget, event)

    def get_hosts_selections(self) -> (None | dict):
        if len(self.hosts) == 0:
            self.print_status("Search for hosts first!")
            return None
        
        selected_hosts = self.ui.FoundHosts_list.selectedItems()
        hosts_dict = {}
        if selected_hosts:
            for sel in selected_hosts:
                sel = sel.text().split()
                hosts_dict[sel[0][0:-1]] = False
        else:
            self.print_status("Nothing selected!")
            return None
        
        return hosts_dict

    def test_hosts(self):
        hosts_dict = self.get_hosts_selections()
        if hosts_dict is None:
            return
        
        hosts_dict = simple_communication(hosts_ips=hosts_dict, port=self.port, command="TEST")
        
        self.ResultsSummary(summary=hosts_dict, type="Test", positive="Ok", negative="Dead")

    def disable_hosts(self):
        hosts_dict = self.get_hosts_selections()
        if hosts_dict is None:
            return
        
        hosts_dict = simple_communication(hosts_ips=hosts_dict, port=self.port, command="KILL")
        
        self.ResultsSummary(summary=hosts_dict, type="Disable", positive="Killed", negative="Unknown")

    def shutdown_hosts(self):
        hosts_dict = self.get_hosts_selections()
        if hosts_dict is None:
            return
        
        hosts_dict = simple_communication(hosts_ips=hosts_dict, port=self.port, command="SHUTDOWN")
        
        self.ResultsSummary(summary=hosts_dict, type="Shutdown", positive="Ok", negative="Unknown")

    def ResultsSummary(self, summary: dict, type: str, positive: str, negative: str):
        self.print_status(f"{type} results:")
        for ip, response in summary.items():
            if response == True:
                self.print_status(f"{ip}: {positive}")
            else:
                self.print_status(f"{ip}: {negative}")

    def checkBoxHandle(self, checkbox_instance: QtWidgets.QCheckBox):
        for checkbox in self.selectCheckBoxes:
            checkbox.setCheckable(True)
            if checkbox is checkbox_instance:
                checkbox.setChecked(True)
                continue
            checkbox.setChecked(False)

    def selectOne(self):
        self.checkBoxHandle(self.ui.SelectOne_checkBox)
        self.ui.FoundHosts_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

    def selectRange(self):
        self.checkBoxHandle(self.ui.SelectRange_checkBox)
        self.ui.FoundHosts_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

    def unselectAllHosts(self):
        self.checkBoxHandle(self.ui.SelectAllActive_checkBox)     
        self.ui.FoundHosts_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.ui.FoundHosts_list.clearSelection()

    def selectAllHosts(self):
        self.checkBoxHandle(self.ui.SelectAllActive_checkBox)
        self.ui.FoundHosts_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.ui.FoundHosts_list.selectAll()

    def get_servers(self):
        self.ui.FoundHosts_list.clear()
        AddrEditPalette = self.ui.AddrEdit.palette()
        self.ui.progressBar.setValue(0)

        subnet = self.ui.AddrEdit.text()
        
        if not re.match("^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){3}$", subnet) :
            AddrEditPalette.setColor(QPalette.Base, QColor("red"))
            self.ui.AddrEdit.setPalette(AddrEditPalette)
            self.print_status(f"{subnet} is incorrect subnet!")
            return
        
        self.port = self.ui.PortEdit.text()

        if self.port == "" or int(self.port) > 65535 :
            AddrEditPalette.setColor(QPalette.Base, QColor("red"))
            self.ui.PortEdit.setPalette(AddrEditPalette)
            self.print_status(f"{self.port} is incorrect value!")
            return

        AddrEditPalette.setColor(QPalette.Base, QColor("white"))
        self.ui.AddrEdit.setPalette(AddrEditPalette)
        self.ui.PortEdit.setPalette(AddrEditPalette)

        self.print_status(f"Discovering {subnet}:{self.port} subnet...")
        self.hosts = discover_servers(subnet, self.port)
        self.print_status(f"Found {len(self.hosts)} hosts.")

        self.ui.FoundHosts_label.setText(str(len(self.hosts)))

        if len(self.hosts):
            self.append_hosts()

        self.ui.progressBar.setValue(100)

    def get_local_addr(self):
        ip_address = ""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect(("8.8.8.8", 80))
            ip_address = sock.getsockname()[0]
            sock.close()
        except Exception as e:
            return f"Nie udało się uzyskać adresu IP: {e}"
        # net = socket.gethostbyname(socket.gethostname())    # requests.get('https://api.ipify.org').content.decode('utf8')
        ip_address = '.'.join(ip_address.split('.')[0:-1])
        self.ui.AddrEdit.setText(ip_address)

    def print_status(self, status_text: str):
        if len(status_text):
            self.ui.StatusInfoBox.append(status_text)
            self.ui.StatusInfoBox.moveCursor(self.ui.StatusInfoBox.textCursor().End)
            self.ui.StatusInfoBox.ensureCursorVisible()

    def append_hosts(self):
        for server in self.hosts:
            self.ui.FoundHosts_list.addItem(f"{server[0]}: {server[1]}")

def simple_communication(hosts_ips: dict, port: str, command: str, expected_response: str = "OK") -> dict:
    hosts_dict = hosts_ips

    def test_hosts(ip, port, command, expected_response):
        try:
            with socket.create_connection((ip, port), timeout=1) as sock:
                sock.sendall(b"HI SERVER")
                response = sock.recv(64).decode()
                if response == "HI CLIENT":
                    sock.sendall(str.encode(command))
                    response = sock.recv(64).decode()
                    if response == expected_response:
                        hosts_dict[ip] = True
                        sock.sendall(b"CLOSE")
                        return

        except Exception:
            pass

    threads = []
    for ip in hosts_ips:
        thread = threading.Thread(target=test_hosts, args=(ip, port, command, expected_response))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return hosts_dict

def discover_servers(subnet: str = "127.0.0", port: str = "8080"):
    found_servers = []

    def discover(ip):
        try:
            with socket.create_connection((ip, port), timeout=1) as sock:
                sock.sendall(b"HI SERVER")
                response = sock.recv(64).decode()
                if response == "HI CLIENT":
                    sock.sendall(b"HOSTNAME")
                    hostname = sock.recv(64).decode()
                    found_servers.append([ip, hostname])
                    sock.sendall(b"CLOSE")

        except Exception:
            pass

    threads = []
    for i in range(1, 2):
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

        if "breeze" not in QtWidgets.QStyleFactory.keys():
            app.setStyle("windowsvista")
        else:
            app.setStyle("breeze")
            
        application = ApplicationWindow()
        application.show()
        sys.exit(app.exec_())

