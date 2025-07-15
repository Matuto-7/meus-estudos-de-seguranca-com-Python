# -*- coding: utf-8 -*-
"""
Banner Grabbing com Python

Este script realiza o banner grabbing em serviços que estão escutando em portas abertas.
O banner é a resposta inicial de alguns serviços, revelando informações como versão e tipo do servidor.

Funcionalidades:
- Conecta a uma ou mais portas abertas e tenta capturar o banner do serviço.

Uso:
Execute no Termux ou terminal:

python3 banner_grabber.py

O script pedirá o IP do alvo e as portas separadas por vírgula.

Autor: matuto-7
Data: 14 de Julho de 2025
"""
Python

import socket

def banner_grab(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024)
        print(f"Banner da porta {port}: {banner.decode().strip()}")
        s.close()
    except Exception as e:
        print(f"Não foi possível obter banner da porta {port}: {e}")

def main():
    ip = input("Digite o IP do alvo: ")
    portas = input("Digite as portas separadas por vírgula (ex: 21,22,80): ")
    lista_portas = [int(p.strip()) for p in portas.split(",")]

    print(f"\nIniciando banner grabbing em {ip}...\n")

    for port in lista_portas:
        print(f"Tentando pegar banner da porta {port}...")
        banner_grab(ip, port)

    print("\nBanner grabbing finalizado!")

if __name__ == "__main__":
    main()
