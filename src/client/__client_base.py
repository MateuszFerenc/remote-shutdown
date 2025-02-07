from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QColor, QPixmap
from main_ui import Ui_MainWindow
from author_ui import Ui_AuthorPopup
from documentation import Ui_Documentation
from os import path, abort
import socket
import sys
import threading
import re
import markdown

if __name__ == "__main__": 
    print("This file should not be run standalone, import in client main app!")
    abort()

file_path = path.dirname(path.abspath(sys.argv[0]))

class TCPCommunication:
    class CommunicationType(int):
        GET = "GET"
        CHECK = "CHECK"
        CLOSE = "CLOSE"

    def __init__(self, communicate_method):
        self.communicate = communicate_method

    # method to spawn workers for faster communication with many hosts
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

class DocumentationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(DocumentationWindow, self).__init__()

        self.ui = Ui_Documentation()
        self.ui.setupUi(self)
        self.markdown_path = path.join(file_path, "..", "..", "README.md")
        self.markdown_content = None        

    def read_markdown(self):
        with open(self.markdown_path, 'r', encoding="utf-8") as md_file:
            self.markdown_content = md_file.read()
        md = markdown.markdown(self.markdown_content, extensions=['extra', 'nl2br'])
        document = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset=\"UTF-8\">
            </head>
            <body style=\"background-color: darkgrey;\">
                {md}
            </body>
        </html>
        """
        
        self.ui.MarkdownView.setHtml(document)


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, communication_method: TCPCommunication):
        super(ApplicationWindow, self).__init__()

        self.tcp_communication = communication_method

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.AuthorPopup = AuthorPopup()
        self.DocumentationWindow = DocumentationWindow()
        self.DocumentationWindow.read_markdown()

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
        self.ui.action_Documentation.triggered.connect(lambda: self.DocumentationWindow.show())
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

    # return currently selected hosts
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
        
        self.ResultsSummary(summary=hosts_dict, type="Test", positive="Ok", negative="Dead")

    # send disable (server/service kill) request to selected hosts
    def disable_hosts(self):
        hosts_dict = self.get_hosts_selections()
        if hosts_dict is None:
            return
        
        hosts_dict = self.tcp_communication.communicate_threaded(self.port, "KILL", TCPCommunication.CommunicationType.CLOSE, hosts_dict, "OK")
        
        self.ResultsSummary(summary=hosts_dict, type="Disable", positive="Killed", negative="Fail")

    # send shutdown request to selected hosts
    def shutdown_hosts(self):
        hosts_dict = self.get_hosts_selections()
        if hosts_dict is None:
            return
        
        hosts_dict = self.tcp_communication.communicate_threaded(self.port, "SHUTDOWN", TCPCommunication.CommunicationType.CLOSE, hosts_dict, "NOK")
        
        self.ResultsSummary(summary=hosts_dict, type="Shutdown", positive="Ok", negative="Fail")

    def ResultsSummary(self, summary: dict, type: str, positive: str, negative: str):
        self.print_status(f"{type} results:")
        for ip, response in summary.items():
            if response == True:
                self.print_status(f"{ip}: {positive}")
            else:
                self.print_status(f"{ip}: {negative}")

    # selection mode indicator
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

    # read IP and PORT and try to discover reachable host over network
    def get_servers(self):
        self.ui.FoundHosts_list.clear()
        AddrEditPalette = self.ui.AddrEdit.palette()

        # read IP subnet (text)
        subnet = self.ui.AddrEdit.text()
        
        # check incoming address against regexp xxx.xxx.xxx
        if not re.match(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){3}$', subnet) :
            AddrEditPalette.setColor(QPalette.Base, QColor("red"))
            self.ui.AddrEdit.setPalette(AddrEditPalette)
            self.print_status(f"{subnet} is incorrect subnet!", status_color="red")
            return
        
        # read PORT (text)
        self.port = self.ui.PortEdit.text()

        # check if port value is valid
        if self.port == "" or int(self.port) > 65535 :
            AddrEditPalette.setColor(QPalette.Base, QColor("red"))
            self.ui.PortEdit.setPalette(AddrEditPalette)
            self.print_status(f"{self.port} is incorrect value!", status_color="red")
            return

        # reset text edit widget to default color
        AddrEditPalette.setColor(QPalette.Base, QColor("white"))
        self.ui.AddrEdit.setPalette(AddrEditPalette)
        self.ui.PortEdit.setPalette(AddrEditPalette)

        self.print_status(f"Discovering {subnet}:{self.port} subnet...")

        # run network discovery using threaded search, on success IPs and names of the hosts will be returned
        self.hosts = self.tcp_communication.communicate_threaded(self.port, "HOSTNAME", TCPCommunication.CommunicationType.GET, subnet=subnet)
        
        self.print_status(f"Found {len(self.hosts)} hosts.")

        self.ui.FoundHosts_label.setText(str(len(self.hosts)))

        if len(self.hosts):
            self.append_hosts()

    # receive LAN IP address
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

    # print system status to status prompt
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

    # append found hosts and their IPs to hosts list
    def append_hosts(self):
        for ip, hostname in self.hosts.items():
            self.ui.FoundHosts_list.addItem("{}: {}".format(ip, hostname.rstrip('\x00')))
