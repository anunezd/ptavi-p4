#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket


SERVER = sys.argv[1]
PORT = int(sys.argv[2])
METHOD = sys.argv[3]
USER = sys.argv[4]
REGISTERSIP = METHOD + ' sip:' + USER + ' SIP/2.0\r\n'

#Creamos el socket, configuramos y atamos servidor-puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    try:
        my_socket.connect((SERVER, PORT))
        print('Enviando: ' + REGISTERSIP)
        my_socket.send(bytes(REGISTERSIP, 'utf-8'))
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))
    except KeyboardInterrupt:
        print('Socket terminado.')
