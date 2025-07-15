# -*- coding: utf-8 -*-
"""
Scanner de Portas TCP com Descrição de Serviços

Este script foi desenvolvido como parte dos meus estudos de segurança ofensiva com Python no Termux.

Funcionalidades:
- Escaneamento de portas TCP em um alvo (IP ou hostname).
- Identificação dos serviços mais comuns nas portas abertas.
- Uso de threads para acelerar o processo.

Uso:
Execute no Termux ou no terminal:

python3 port_scanner_servico.py

O script pedirá o IP ou hostname e o intervalo de portas.

Autor: Matias Lopes
Data: 14 de Julho de 2025
"""

Python


import socket
import threading

# Mapeamento de portas para serviços conhecidos
servicos = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP (Web)",
    110: "POP3 (Email)",
    143: "IMAP (Email)",
    443: "HTTPS (Web Segura)",
    3306: "MySQL",
    3389: "RDP (Acesso Remoto)",
    8080: "HTTP Alternativo"
}

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            servico = servicos.get(port, "Serviço desconhecido")
            print(f"Porta {port} aberta → {servico}")
        sock.close()
    except:
        pass

def main():
    host = input("Digite o IP ou hostname para scanear: ")
    porta_inicial = int(input("Porta inicial: "))
    porta_final = int(input("Porta final: "))

    print(f"\nScan de portas em {host} de {porta_inicial} a {porta_final} com descrição de serviços...\n")

    threads = []
    for port in range(porta_inicial, porta_final + 1):
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nScan finalizado!")

if __name__ == "__main__":
    main()
