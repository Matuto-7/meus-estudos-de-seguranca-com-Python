import subprocess
import platform
from tqdm import tqdm
import time

def ping(ip):
    """
    Executa um ping simples para verificar se o IP está ativo.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    result = subprocess.run(command, stdout=subprocess.DEVNULL)
    return result.returncode == 0

def varrer_rede(base_ip):
    ativos = []
    print(f"\n🔎 Iniciando varredura em {base_ip}.0/24\n")
    time.sleep(1)

    for i in tqdm(range(1, 255), desc="Varrendo IPs", unit="host"):
        ip = f"{base_ip}.{i}"
        if ping(ip):
            ativos.append(ip)

    if ativos:
        print("\n📋 IPs ativos encontrados:")
        for ip in ativos:
            print(f"✅ {ip}")

        with open("ips_ativos.txt", "w") as arquivo:
            for ip in ativos:
                arquivo.write(ip + "\n")

        print("\n📝 IPs salvos em: ips_ativos.txt")
    else:
        print("\n❌ Nenhum IP ativo encontrado.")

if __name__ == "__main__":
    print("🧹 IP Sweeper — Descubra dispositivos ativos na rede local\n")
    base_ip = input("Digite a base da rede (ex: 192.168.0): ").strip()
    varrer_rede(base_ip)
