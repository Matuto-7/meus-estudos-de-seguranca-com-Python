#!/bin/bash

# ghost_sweep.sh - Varredura simples de rede local

for ip in $(seq 1 254); do
    ping -c 1 192.168.1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done