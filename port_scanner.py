import socket
import pyfiglet

nome = "Nome: Romildo (thuf)    Site: helptecinfo.com"

print("\n\n======================================")
banner = pyfiglet.figlet_format("SCANNER")
print(banner)
print(nome)
print("======================================\n")

ip_address = input('Insira o serviço que deseja scannear: ')
start_port = int(input('Insira a porta inicial: '))
end_port = int(input('Insira a porta final: '))

def scan_ports(ip_address, start_port, end_port):
    open_ports_count = 0

    # Faz um loop pelas portas desejadas
    for port in range(start_port, end_port+1):
        try:
            # Cria um novo socket para cada tentativa de conexão
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                # Configura o timeout do socket para 3 segundos
                sock.settimeout(3)
                # Tenta se conectar à porta atual
                result = sock.connect_ex((ip_address, port))
                if result == 0:
                    # Se a conexão foi bem-sucedida, a porta está aberta
                    print(f'Porta {port} está aberta.')
                    open_ports_count += 1
        except socket.error as e:
            print(f"Não foi possível conectar à porta {port}. Erro: {e}")
            continue

    # Verifica se foram encontradas portas abertas
    if open_ports_count == 0:
        print('Não foram encontradas portas abertas.')
    print("")

# Chama a função de verificação de portas
scan_ports(ip_address, start_port, end_port)
