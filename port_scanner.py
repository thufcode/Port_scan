import socket
import whois
import pyfiglet

nome = ("Nome: Romildo (thuf)    Site: helptecinfo.com")

print("")
print("")
print("======================================")
banner = pyfiglet.figlet_format("SCANNER")
print(banner)
print(nome)
print("======================================")
print("")

# Solicita o endereço IP ou URL do usuário
ip_address = input('Insira o serviço que deseja scannear: ')

# Solicita o intervalo de portas a serem verificadas
start_port = int(input('Insira a porta inicial: '))
end_port = int(input('Insira a porta final: '))

def scan_ports(ip_address, start_port, end_port):
  # Crie um socket do tipo SOCK_STREAM (TCP)
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Configure o timeout do socket para 3 segundos
  sock.settimeout(3)

  # Inicialize uma variável para contar as portas abertas encontradas
  open_ports_count = 0

  # Faça um loop pelas portas desejadas
  for port in range(start_port, end_port+1):
    # Tente se conectar à porta atual
    result = sock.connect_ex((ip_address, port))
    if result == 0:
      # Se a conexão foi bem-sucedida, a porta está aberta
      # Realize uma consulta whois para obter informações sobre o serviço na porta
      service = whois.whois(f'{ip_address}:{port}')
      print(f'Porta {port} está aberta e rodando o serviço "{service}"')
      open_ports_count += 1
    else:
      # Se a conexão falhou, a porta está fechada
      pass

  # Verifique se foram encontradas portas abertas
  if open_ports_count == 0:
    print('Não foram encontradas portas abertas')
  print("")

# Chama a função de verificação de portas
scan_ports(ip_address, start_port, end_port)

