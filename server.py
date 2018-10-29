#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class SIPRegisterHandler(socketserver.DatagramRequestHandler):



    dicc = {}
    def handle(self):
        line = self.rfile.read()
        doc = line.decode('utf-8').split(" ")
        IP = self.client_address[0]
        PORT = self.client_address[1]
        if doc[0] == 'REGISTER':
            user = doc[2]
            address = str(ip) + ":" + str(port)
            self.dicc[user] = ('address: ' + address)
            print(self.dicc)
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

if __name__ == "__main__":
    PORT = int(sys.argv[1])
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...\n")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
