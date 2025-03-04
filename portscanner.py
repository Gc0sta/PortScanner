import nmap


def iniciar_varredura():
    # Cria o objeto do scanner
    scanner = nmap.PortScanner()

    # Entrada de IP
    ip = input("Digite o IP a ser escaneado: ")
    print(f"O IP digitado foi: {ip}")

    # Menu de opções
    print("""
    Escolha o tipo de varredura a ser realizada:
    1 - Varredura SYN
    2 - Varredura UDP
    3 - Varredura Intensa
    """)
    menu = input("Digite a opção desejada: ")
    print(f"A opção escolhida foi: {menu}")

    # Processamento com base na escolha
    if menu == "1":
        print("Versão do Nmap:", scanner.nmap_version())
        scanner.scan(ip, '1-1024', '-v -sS')
        print("Status do IP:", scanner[ip].state())
        print("Protocolos:", scanner[ip].all_protocols())
        print("Portas Abertas:", scanner[ip]['tcp'].keys())

    elif menu == "2":
        print("Versão do Nmap:", scanner.nmap_version())
        scanner.scan(ip, '1-1024', '-v -sU')
        print("Status do IP:", scanner[ip].state())
        print("Protocolos:", scanner[ip].all_protocols())
        print("Portas Abertas:", scanner[ip]['udp'].keys())

    elif menu == "3":
        print("Versão do Nmap:", scanner.nmap_version())
        scanner.scan(ip, '1-1024', '-v -sC')
        print("Status do IP:", scanner[ip].state())
        print("Protocolos:", scanner[ip].all_protocols())
        print("Portas Abertas:", scanner[ip]['tcp'].keys())

    else:
        print("Escolha uma opção válida!")
        

# Função principal
if __name__ == "__main__":
    print("Bem-vindo ao Port Scanner!")
    iniciar_varredura()