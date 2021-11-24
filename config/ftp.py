import socket
import os
from colorama import Fore
from datetime import date, datetime
import linecache

class Run:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        date_today = date.today()
        now = datetime.now()
        bytes = 1024

        try:
            os.mkdir(f'/etc/ehoney/logs/ftp-hp-{date_today}')
            os.mkdir(f'/etc/ehoney/logs/ftp-hp-{date_today}/usernames_tried')
        except FileExistsError:
            pass

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))

            s.listen(1000)
            clientsock, clientAddress = s.accept()

            log_ftp = open(f'/etc/ehoney/logs/ftp-hp-{date_today}/IPs.txt', 'a')
            log_ftp.write(f'{clientAddress[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
            log_ftp.close()

            print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Intrusion Detected: {clientAddress[0]}:{clientAddress[1]}')
            print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Capturing Typing:')
            clientsock.send('220 (vsFTPd 2.3.4)\n\r'.encode('utf-8'))
        except:
            pass

        while True:
            try:
                resposta = clientsock.recv(bytes).decode()
                users_used_ftp = open(f'/etc/ehoney/logs/ftp-hp-{date_today}/usernames_tried/usernames_tried_{clientAddress[0].replace(".", "_")}.txt', 'a')
                resposta2 = resposta.replace('SYST', '')
                resposta3 = resposta2.replace('QUIT', '')

                users_used_ftp.write(resposta3[5::])
                users_used_ftp.close()
                print(resposta.replace('\n', ''))
            except:
                pass

            if resposta:
                try:
                    clientsock.send('530 user not found\n\r'.encode('utf-8'))
                except:
                    pass

            if 'USER' in resposta:
                print(f'└─> {Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}User he tried to connect')

            if 'OPTIONS / RTSP/1.0' in resposta:
                print(f'\n{Fore.LIGHTYELLOW_EX}[!] ALERT: The Invader is using Nmap!!!\n{Fore.LIGHTWHITE_EX}')

            if not resposta:
                try:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.LIGHTWHITE_EX}Invader left: {clientAddress[0]}:{clientAddress[1]}\n')
                    s.listen(1000)
                    clientsock, clientAddress = s.accept()
                    log_ftp = open(f'/etc/ehoney/logs/ftp-hp-{date_today}/IPs.txt', 'a')
                    log_ftp.write(f'{clientAddress[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
                    log_ftp.close()
                    print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Intrusion Detected: {clientAddress[0]}:{clientAddress[1]}')
                    print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Capturing Typing:')
                    clientsock.send('220 (vsFTPd 3.0.3)\n\r'.encode('utf-8'))

                    if resposta:
                        clientsock.send('530 user not found\n\r'.encode('utf-8'))
                except:
                    pass

Run(host='127.0.0.1', port=int(linecache.getline('/etc/ehoney/config/ports.conf', 3).split('=')[1]))
