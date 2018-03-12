#!/usr/bin/env python

import socket
import sys

import os

server = input('Server: ')

while True:
	version = int(input('Version: '))
	if version == 4:
		sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		break
	if version == 6:
		sd = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
		break
	else:
		print('Puoi scegliere solo 4 o 6')
		continue

try:
	sd.connect((server, 3000))
except OSError as e:
	print(f'Errore sulla connect: {e}')
	sys.exit(0)

with sd:
	print('Connessione avvenuta\n')

	while True:
		data = input('Messaggio: ')
		sd.sendall(bytes(data, 'UTF-8'))
		data = sd.recv(1024)
		response = data.decode('UTF-8')
		print(f'Ricevuto: {data}')

		if response[0:4] == "ALGO":
			print(f'Connection closed.\n{response[5:]} files deleted.\n')
			os._exit(0)
