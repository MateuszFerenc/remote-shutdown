from PyQt5 import QtWidgets
import socket
import sys
from __client_base import ApplicationWindow, TCPCommunication

# without SSL    
def communicate(hosts_dict: dict, ip: str, port: str, command: str, expected_response: str, communicationtype: TCPCommunication.CommunicationType):
    try:
        # initialise communication (socket) with server, after 1s give up
        with socket.create_connection((ip, port), timeout=1) as sock:
            # send client->server greeting
            sock.sendall(b"HI SERVER")
            # get response
            response = sock.recv(64).decode()
            # if response is "HI CLIENT" continue communication
            if response == "HI CLIENT":
                # send command to server
                sock.sendall(str.encode(command))
                # receive response
                response = sock.recv(64).decode()
                # if type of communication is GET, save response
                if communicationtype == TCPCommunication.CommunicationType.GET:
                    hosts_dict[ip] = response
                # if type of communication is CHECk, check server response against expected_response
                elif communicationtype == TCPCommunication.CommunicationType.CHECK:
                    if response == expected_response:
                        # server response is expected_response
                        hosts_dict[ip] = True
                # if type of communication is CLOSE, if server responds after shutdown select as invalid
                elif communicationtype == TCPCommunication.CommunicationType.CLOSE:
                    hosts_dict[ip] = True
                    response = sock.recv(64).decode()
                    if response == expected_response:
                        hosts_dict[ip] = False
                # close the communication after all
                sock.sendall(b"CLOSE")
                return
    except Exception:
        pass

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)

    if "breeze" not in QtWidgets.QStyleFactory.keys():
        app.setStyle("windowsvista")
    else:
        app.setStyle("breeze")
        
    noSLL = TCPCommunication(communicate_method=communicate)
    
    application = ApplicationWindow(communication_method=noSLL)
    application.show()
    sys.exit(app.exec_())

