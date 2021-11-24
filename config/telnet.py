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
            os.mkdir(f'/etc/ehoney/logs/telnet-hp-{date_today}')
            os.mkdir(f'/etc/ehoney/logs/telnet-hp-{date_today}/usernames_tried')
        except FileExistsError:
            pass

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))

        s.listen(1000)
        clientsock, clientAddress = s.accept()
        log_telnet = open(f'/etc/ehoney/logs/telnet-hp-{date_today}/IPs.txt', 'a')
        log_telnet.write(f'{clientAddress[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
        log_telnet.close()
        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Intrusion Detected: {clientAddress[0]}:{clientAddress[1]}')
        print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Capturing Typing:')
        while True:
            try:
                clientsock.send('Ubuntu login: '.encode('utf-8'))
                resposta = clientsock.recv(bytes).decode()
                users_used_telnet = open(f'/etc/ehoney/logs/telnet-hp-{date_today}/usernames_tried/usernames_tried_{clientAddress[0].replace(".", "_")}.txt', 'a')
                users_used_telnet.write(resposta)
                users_used_telnet.close()
                print(resposta.replace('\n', ''))
                print(f'└─> {Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}User he tried to connect')

                if 'OPTIONS / RTSP/1.0'  in resposta:
                    print(f'{Fore.LIGHTYELLOW_EX}[!] ALERT: The Invader is using Nmap!!!')

                

                if not resposta:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.LIGHTWHITE_EX}Invader left: {clientAddress[0]}:{clientAddress[1]}\n')
                    s.listen(1000)
                    clientsock, clientAddress = s.accept()
                    log_telnet = open(f'/etc/ehoney/logs/telnet-hp-{date_today}/IPs.txt', 'a')
                    log_telnet.write(f'{clientAddress[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
                    log_telnet.close()
                    print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Intrusion Detected: {clientAddress[0]}:{clientAddress[1]}')
                    print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Capturing Typing:')
                    clientsock.send('Ubuntu login: '.encode('utf-8'))
            except:
                pass

Run(host='127.0.0.1', port=int(linecache.getline('/etc/ehoney/config/ports.conf', 4).split('=')[1]))
