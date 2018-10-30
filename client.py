#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket


try:
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    LINEA = sys.argv[3]
    REGISTERSIP = ''
    USER = sys.argv[4]
    EXPIRES = sys.argv[5]
except IndexError:
        sys.exit('Usage: client.py ip puerto register sip_address expires_val')
REGISTERSIP = 'REGISTER sip:' + USER + ' SIP/2.0\r\n\r\n' + 'Expires:' + EXPIRES + '\r\n\r\n'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    try:
        my_socket.connect((SERVER, PORT))
        print('Enviando: ' + REGISTERSIP)
        my_socket.send(bytes(REGISTERSIP, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))

    except KeyboardInterrupt:
        print('Socket terminado.')
