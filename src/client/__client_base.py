if __name__ == "__main__": 
    print("This file should not be run standalone, import in client main app!")
    abort()

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QColor, QPixmap
from main_ui import Ui_MainWindow
from author_ui import Ui_AuthorPopup
from os import path, abort
import socket
import sys
import threading
import re

file_path = path.dirname(path.abspath(sys.argv[0]))

class TCPCommunication:
    class CommunicationType(int):
        GET = "GET"
        CHECK = "CHECK"
        CLOSE = "CLOSE"

    def __init__(self, communicate_method):
        self.communicate = communicate_method

    def communicate_threaded(self, port: str, command: str, communication_type: CommunicationType, hosts_ips: dict = {}, expected_response: str = "OK", subnet: str = "") -> dict:
        hosts_dict = hosts_ips

        threads = []

        IPSet_Range = None
        if hosts_ips:
            IPSet_Range = hosts_ips
        else:
            if subnet != "":
                IPSet_Range = [ f"{subnet}.{i}" for i in range(1, 255) ]
            else:
                print("You need to specify the subnet!")
                return {}

        for ip in IPSet_Range:
            thread = threading.Thread(target=self.communicate, args=(hosts_dict, ip, port, command, expected_response, communication_type))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        return hosts_dict

class AuthorPopup(QtWidgets.QMainWindow):
    def __init__(self):
        super(AuthorPopup, self).__init__()

        self.ui = Ui_AuthorPopup()
        self.ui.setupUi(self)
        self.setWindowTitle("Author Info")
        self.ui.AuthorImage.setPixmap(QPixmap(path.join(file_path, "author_image.png")))


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, communication_method: TCPCommunication):
        super(ApplicationWindow, self).__init__()

        self.tcp_communication = communication_method

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # remove before commit !!!!!!!!!!!!
        self.ui.AddrEdit.setText("127.0.0")
        self.ui.PortEdit.setText("21037")

        self.AuthorPopup = AuthorPopup()

        # setup clicked Event methods
        self.ui.SearchButton.clicked.connect(self.get_servers)
        self.ui.getLocalAddr.clicked.connect(self.get_local_addr)
        self.ui.TestHosts_button.clicked.connect(self.test_hosts)
        self.ui.DisableHosts_button.clicked.connect(self.disable_hosts)
        self.ui.ShutdownHosts_button.clicked.connect(self.shutdown_hosts)
        self.ui.SelectAll_button.clicked.connect(self.selectAllHosts)
        self.ui.UnselectAll_button.clicked.connect(self.unselectAllHosts)
        self.ui.SelectRange_button.clicked.connect(self.selectRange)
        self.ui.SelectOne_button.clicked.connect(self.selectOne)
        self.ui.ClearStatus.clicked.connect(self.clear_status)
        self.ui.action_Author.triggered.connect(lambda: self.AuthorPopup.show())
        self.ui.action_Exit_2.triggered.connect(lambda: self.close())

        # setup selection changed Event methods
        self.ui.FoundHosts_list.itemSelectionChanged.connect(lambda: self.ui.SelectedHosts_label.setText(str(len(self.ui.FoundHosts_list.selectedIndexes()))))

        self.ui.FoundHosts_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)        

        self.hosts = []
        self.port = ""
        self.selected_hosts = []

        self.ui.StatusIndicator.setStyleSheet("""
                QCheckBox::indicator {
                    background-color: lightgrey;
                    border: 1px solid darkgrey;
                }
            """)
        
        self.selectCheckBoxes = (self.ui.SelectOne_checkBox, self.ui.SelectRange_checkBox, self.ui.SelectAllActive_checkBox)

        # setup selection status checkboxes
        for cb in self.selectCheckBoxes:
            cb.setStyleSheet("""
                QCheckBox::indicator {
                    background-color: lightgrey;
                    border: 1px solid darkgrey;
                }
                QCheckBox::indicator:checked {
                    background-color: yellow;
                }
            """)

    def clear_status(self):
        self.ui.ClearStatus.setChecked(False)
        self.ui.StatusInfoBox.clear()

    def get_hosts_selections(self) -> (None | dict):
        if len(self.hosts) == 0:
            self.print_status("Search for hosts first!", status_color="orange")
            return None
        
        selected_hosts = self.ui.FoundHosts_list.selectedItems()
        hosts_dict = {}
        if selected_hosts:
            for sel in selected_hosts:
                sel = sel.text().split()
                hosts_dict[sel[0][0:-1]] = False
        else:
            self.print_status("Nothing selected!", status_color="orange")
            return None
        
        return hosts_dict

    def test_hosts(self):
        hosts_dict = self.get_hosts_selections()
        if hosts_dict is None:
            return
        
        hosts_dict = self.tcp_communication.communicate_threaded(self.port, "TEST", TCPCommunication.CommunicationType.CHECK, hosts_dict, "OK")
        #hosts_dict = self.tcp_communication(hosts_ips=hosts_dict, port=self.port, command="TEST")
        
        self.ResultsSummary(summary=hosts_dict, type="Test", positive="Ok", negative="Dead")

    def disable_hosts(self):
        hosts_dict = self.get_hosts_selections()
        if hosts_dict is None:
            return
        
        hosts_dict = self.tcp_communication.communicate_threaded(self.port, "KILL", TCPCommunication.CommunicationType.CLOSE, hosts_dict, "OK")
        #hosts_dict = self.tcp_communication(hosts_ips=hosts_dict, port=self.port, command="KILL")
        
        self.ResultsSummary(summary=hosts_dict, type="Disable", positive="Killed", negative="Fail")

    def shutdown_hosts(self):
        hosts_dict = self.get_hosts_selections()
        if hosts_dict is None:
            return
        
        hosts_dict = self.tcp_communication.communicate_threaded(self.port, "SHUTDOWN", TCPCommunication.CommunicationType.CLOSE, hosts_dict, "NOK")
        # hosts_dict = self.tcp_communication(hosts_ips=hosts_dict, port=self.port, command="SHUTDOWN")
        
        self.ResultsSummary(summary=hosts_dict, type="Shutdown", positive="Ok", negative="Fail")

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

        subnet = self.ui.AddrEdit.text()
        
        if not re.match("^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){3}$", subnet) :
            AddrEditPalette.setColor(QPalette.Base, QColor("red"))
            self.ui.AddrEdit.setPalette(AddrEditPalette)
            self.print_status(f"{subnet} is incorrect subnet!", status_color="red")
            return
        
        self.port = self.ui.PortEdit.text()

        if self.port == "" or int(self.port) > 65535 :
            AddrEditPalette.setColor(QPalette.Base, QColor("red"))
            self.ui.PortEdit.setPalette(AddrEditPalette)
            self.print_status(f"{self.port} is incorrect value!", status_color="red")
            return

        AddrEditPalette.setColor(QPalette.Base, QColor("white"))
        self.ui.AddrEdit.setPalette(AddrEditPalette)
        self.ui.PortEdit.setPalette(AddrEditPalette)

        self.print_status(f"Discovering {subnet}:{self.port} subnet...")
        self.hosts = self.tcp_communication.communicate_threaded(self.port, "HOSTNAME", TCPCommunication.CommunicationType.GET, subnet=subnet)
        self.print_status(f"Found {len(self.hosts)} hosts.")

        self.ui.FoundHosts_label.setText(str(len(self.hosts)))

        if len(self.hosts):
            self.append_hosts()

    def get_local_addr(self):
        self.ui.getLocalAddr.setChecked(False)
        ip_address = ""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect(("8.8.8.8", 80))
            ip_address = sock.getsockname()[0]
            sock.close()
        except Exception as e:
            return f"Nie udało się uzyskać adresu IP: {e}"

        ip_address = '.'.join(ip_address.split('.')[0:-1])
        self.ui.AddrEdit.setText(ip_address)

    def print_status(self, status_text: str, status_color: str = "green"):
        if len(status_text):
            self.ui.StatusIndicator.setStyleSheet(f"""
                QCheckBox::indicator {{
                    background-color: {status_color};
                    border: 1px solid darkgrey;
                }}
            """)
            self.ui.StatusInfoBox.append(status_text)
            self.ui.StatusInfoBox.moveCursor(self.ui.StatusInfoBox.textCursor().End)
            self.ui.StatusInfoBox.ensureCursorVisible()

    def append_hosts(self):
        for ip, hostname in self.hosts.items():
            self.ui.FoundHosts_list.addItem(f"{ip}: {hostname}")
