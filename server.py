#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import sys
import json
import os
import socketserver
from datetime import datetime, date, time, timedelta

FORMATO = '%Y-%m-%d %H:%M:%S'


class SIPRegisterHandler(socketserver.DatagramRequestHandler):

    dicc = {}
    lista = []

    def handle(self):
        self.json2registered()
        line = self.rfile.read()
        doc = line.decode('utf-8').split(" ")
        ip = self.client_address[0]
        port = self.client_address[1]
        if doc[0] == 'REGISTER':
            user = doc[1].split(':')[1]
            tiempo = datetime.now()
            expires = doc[2].split(':')[1].split('\r\n')[0]
            if int(expires) == 0:
                try:
                    del self.dicc[user]
                    self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
                except KeyError:
                    pass
            else:
                expired = tiempo + timedelta(seconds=int(expires))
                address = str(ip) + ":" + str(port)
                fecha = expired.strftime(FORMATO)
                self.dicc[user] = {'Address ': address, 'Expires': fecha}
                self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            lista = []
            now = datetime.now()
            for user in self.dicc:
                if self.dicc[user]['Expires'] <= now.strftime(FORMATO):
                    lista.append(user)
            for user in lista:
                del self.dicc[user]
            print(self.dicc)
            self.register2json()

    def register2json(self):
        with open('registered.json', 'w') as outfile_json:
            json.dump(self.dicc, outfile_json, indent=3)
        os.system('cat registered.json')

    def json2registered(self):
        try:
            with open('registered.json', 'r') as outfile_json:
                self.dicc = json.load(outfile_json)
        except:
            pass


if __name__ == "__main__":
    try:
        PORT = int(sys.argv[1])
    except IndezError:
        sys.exit('Usage: server.py puerto')
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...\n")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
