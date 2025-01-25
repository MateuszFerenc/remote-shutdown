from PyQt5 import QtWidgets
from os import path
import socket
import sys
from __client_base import ApplicationWindow, TCPCommunication
import ssl

file_path = path.dirname(path.abspath(sys.argv[0]))

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(path.join(file_path, "..", "..", "cert.pem"))

# with SSL    
def communicate(hosts_dict: dict, ip: str, port: str, command: str, expected_response: str, communicationtype: TCPCommunication.CommunicationType):
    try:
        # initialise communication (socket) with server, after 1s give up
        with socket.create_connection((ip, port), timeout=1) as sock:
            # create SSL socket over already open TCP socket (wrapping)
            with context.wrap_socket(sock, server_hostname=ip) as ssl_sock:
                # send client->server greeting
                ssl_sock.sendall(b"HI SERVER")
                # get response
                response = ssl_sock.recv(64).decode()
                # if response is "HI CLIENT" continue communication
                if response == "HI CLIENT":
                    # send command to server
                    ssl_sock.sendall(str.encode(command))
                    # receive response
                    response = ssl_sock.recv(64).decode()
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
                        response = ssl_sock.recv(64).decode()
                        if response == expected_response:
                            hosts_dict[ip] = False
                    # close the communication after all
                    ssl_sock.sendall(b"CLOSE")
                    return
    except Exception as e:
        if str(e).find("SSL") == 1:
            print(f"SSL Error with {ip}: {e}")

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
