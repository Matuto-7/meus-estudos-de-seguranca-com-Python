# 🔍 Varredura de IPs Ativos com Bash

Este script simples em **Bash** permite fazer uma **varredura rápida** na sua rede local, identificando quais **endereços IP estão ativos** (respondendo a ping).

Ideal pra quem tá começando no mundo da **segurança ofensiva**, **redes** ou **pentest**, e quer entender o funcionamento do `ping sweep` direto na prática. 😎

---

## 🧠 O que o script faz?

Ele executa os seguintes passos:

1. **Recebe a base do IP como entrada** (ex: `192.168.0`)
2. Faz um **loop de 1 a 254**, testando IPs de `192.168.0.1` até `192.168.0.254`
3. **Usa o `ping`** para verificar se o IP está respondendo
4. Filtra apenas os IPs que estão **ativos**
5. Exibe os IPs ativos no terminal

---

## 📜 Código-fonte: `sweeper.sh`

```bash
#!/bin/bash

# Verifica se o usuário passou a base do IP
if [ -z "$1" ]; then
    echo "Uso: ./sweeper.sh 192.168.1"
    exit 1
fi

echo "Varredura iniciada em $1.1 até $1.254"
echo "IPs ativos:"

for ip in $(seq 1 254); do
    ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d "." &
done

wait