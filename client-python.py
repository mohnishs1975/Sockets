###############################################################################
# client-python.py
# Name:
# BU ID:
# Email:
###############################################################################

import sys
import socket
import select
import fileinput

SEND_BUFFER_SIZE = 2048

def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    #buffer = sys.stdin.read(SEND_BUFFER_SIZE)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #instance of socket
    s.connect((server_ip, server_port))                     #connect to server
    message = sys.stdin.read()
    s.sendall(message.encode())
    s.close()   

def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

def utf8len(s):
    return len(s.encode('utf-8'))


if __name__ == "__main__":
    main()
