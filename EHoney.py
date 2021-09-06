#!/usr/bin/env python3
import socket
import http.server as SimpleHTTPServer
import socketserver as SocketServer
from colorama import Fore
import logging
import os
import platform
import time
from datetime import date, datetime
import glob
import requests
import json

host = '0.0.0.0'
ftp_port = 21        # change if you prefer
telnet_port = 23     # change if you prefer
web_port = 80        # change if you prefer
bytes = 1024
date_today = date.today()
now = datetime.now()
version = '1.0'

def main():
    def banner():
        print(f'''{Fore.LIGHTYELLOW_EX}
       .;oOOOOd;. .;oOOOOd:.       
       OOOOOOOOOO OOOOOOOOOO       
       OOOOOOOOOO OOOOOOOOOO       
       cOOOOOOOOl ;OOOOOOOOd       
    .:occ. OO .ccoc:. OO..cco:.    
 .okOOOOOkl.'lkOOOOOkl'.lkOOOOOko. 
 cOOOOOOOOO':OOOOOOOOO:'OOOOOOOOOc 
 cOOOOOOOOO':OOOOOOOOO:'OOOOOOOOOc 
   OOOOOOk .. kOOOOOO ., xOOOOOO   
        ::okkocc  .ccoOOdll.       
       xOOOOOOOOx kOOOOOOOOk       
       OOOOOOOOOO OOOOOOOOOO       
       OOOOOOOOOO OOOOOOOOOO       
         .OOOO.      kOOO
 _____ _   _                        
| ____| | | | ___  _ __   ___ _   _ 
|  _| | |_| |/ _ \| '_ \ / _ \ | | |
| |___|  _  | (_) | | | |  __/ |_| |
|_____|_| |_|\___/|_| |_|\___|\__, |
                              |___/
{Fore.LIGHTWHITE_EX}     [Tool created by MrEmpy]
           [Version {version}]''')


    def ftp():
        try:
            os.mkdir(f'logs/ftp-hp-{date_today}')
            os.mkdir(f'logs/ftp-hp-{date_today}/usernames_tried')
        except FileExistsError:
            pass

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, ftp_port))

        s.listen(1000)
        clientsock, clientAddress = s.accept()

        log_ftp = open(f'logs/ftp-hp-{date_today}/IPs.txt', 'a')
        log_ftp.write(f'{clientAddress[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
        log_ftp.close()

        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Intrusion Detected: {clientAddress[0]}:{clientAddress[1]}')
        print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Capturing Typing:')
        clientsock.send('220 (vsFTPd 3.0.3)\n\r'.encode('utf-8'))

        while True:
            try:
                resposta = clientsock.recv(bytes).decode()
                users_used_ftp = open(f'logs/ftp-hp-{date_today}/usernames_tried/usernames_tried_{clientAddress[0].replace(".", "_")}.txt', 'a')
                resposta2 = resposta.replace('SYST', '')
                resposta3 = resposta2.replace('QUIT', '')

                users_used_ftp.write(resposta3[5::])
                users_used_ftp.close()
                print(resposta.replace('\n', ''))
            except:
                pass

            if resposta:
                clientsock.send('530 user not found\n\r'.encode('utf-8'))

            if 'USER' in resposta:
                print(f'└─> {Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}User he tried to connect')

            if 'QUIT' in resposta:
                print(f'└─> {Fore.LIGHTRED_EX}[-] {Fore.LIGHTWHITE_EX}Invader left: {clientAddress[0]}:{clientAddress[1]}\n')

            if 'OPTIONS / RTSP/1.0'  in resposta:
                print(f'\n{Fore.LIGHTYELLOW_EX}[!] ALERT: The Invader is using Nmap!!!\n{Fore.LIGHTWHITE_EX}')

            if not resposta:
                s.listen(1000)
                clientsock, clientAddress = s.accept()
                log_ftp = open(f'logs/ftp-hp-{date_today}/IPs.txt', 'a')
                log_ftp.write(f'{clientAddress[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
                log_ftp.close()
                print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Intrusion Detected: {clientAddress[0]}:{clientAddress[1]}')
                print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Capturing Typing:')
                clientsock.send('220 (vsFTPd 3.0.3)\n\r'.encode('utf-8'))

                if resposta:
                    clientsock.send('530 user not found\n\r'.encode('utf-8'))

    def telnet():
        try:
            os.mkdir(f'logs/telnet-hp-{date_today}')
            os.mkdir(f'logs/telnet-hp-{date_today}/usernames_tried')
        except FileExistsError:
            pass

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, telnet_port))

        s.listen(1000)
        clientsock, clientAddress = s.accept()
        log_telnet = open(f'logs/telnet-hp-{date_today}/IPs.txt', 'a')
        log_telnet.write(f'{clientAddress[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
        log_telnet.close()
        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Intrusion Detected: {clientAddress[0]}:{clientAddress[1]}')
        print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Capturing Typing:')
        while True:
            try:
                clientsock.send('Ubuntu login: '.encode('utf-8'))
                resposta = clientsock.recv(bytes).decode()
                users_used_telnet = open(f'logs/telnet-hp-{date_today}/usernames_tried/usernames_tried_{clientAddress[0].replace(".", "_")}.txt', 'a')
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
                    log_telnet = open(f'logs/telnet-hp-{date_today}/IPs.txt', 'a')
                    log_telnet.write(f'{clientAddress[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
                    log_telnet.close()
                    print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Intrusion Detected: {clientAddress[0]}:{clientAddress[1]}')
                    print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Capturing Typing:')
                    clientsock.send('Ubuntu login: '.encode('utf-8'))
            except:
                pass

    def web():
        try:
            os.mkdir(f'logs/web-hp-{date_today}')
        except FileExistsError:
            pass

        class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
            def do_GET(self):
                logging.error(self.headers)
                SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
            log_file = open(f'logs/web-hp-{date_today}/log.txt', 'w', 1)
            def log_message(self, format, *args):
                self.log_file.write('IP: %s\nDate: [%s]\n%s%s\n\n\n\n' % (self.client_address[0], self.log_date_time_string(), self.headers, format%args))

        web_dir = os.path.join(os.path.dirname(__file__), 'web')
        os.chdir(web_dir)
        Handler = GetHandler
        httpd = SocketServer.TCPServer(("", web_port), Handler)
        httpd.serve_forever()
            

    banner()
    print(f'''{Fore.LIGHTWHITE_EX}
    [01] Start FTP Honeypot
    [02] Start Telnet Honeypot
    [03] Start Web Honeypot
    [04] Create Report
    ''')
    select = input(f'{Fore.LIGHTWHITE_EX}Select: ')

    if select == '01' or select == '1':
        print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Honeypot is starting, if you want to change port look for "ftp_port" in the source code. Good hunting ;)')
        time.sleep(3)
        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Honeypot started!\n')
        ftp()

    if select == '02' or select == '2':
        print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Honeypot is starting, if you want to change port look for "telnet_port" in the source code. Good hunting ;)')
        time.sleep(3)
        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Honeypot started!\n')
        telnet()

    if select == '03' or select == '3':
        print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Honeypot is starting, if you want to change port look for "web_port" in the source code. Good hunting ;)')
        time.sleep(3)
        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Honeypot started!\n')
        web()

    if select == '04' or select == '4':
        if platform == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        banner()
        print(f'''{Fore.LIGHTWHITE_EX}
    [01] FTP Report
    [02] Telnet Report
    [03] Web Report
    ''')

        select_report = input(f'{Fore.LIGHTWHITE_EX}Select: ')
        if platform == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
            banner()
        if select_report == '01' or select_report == '1':
            print(f'''{Fore.LIGHTWHITE_EX}
    [01] Text Report
    [02] HTML Report
            ''')
            select_report_format = input(f'{Fore.LIGHTWHITE_EX}Select: ')
            if select_report_format == '01' or select_report_format == '1':
                ftp_report_folder = input(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Put the path where the ftp log folder is: ')
                print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Creating report')

                report_ftp_file = open(f'reports/ftp_report_{date_today}.txt', 'a')
                ips_ftp_file = open(f'{ftp_report_folder}/IPs.txt', 'r').read().splitlines()
                
                ip_count = 0
                for ip in ips_ftp_file:
                    ip_count += 1

                username_count = 0
                for all_usernames_count in glob.glob(f'{ftp_report_folder}/usernames_tried/*.txt'):
                    file_usernames_count = open(all_usernames_count, 'r').read().splitlines()
                    for x in file_usernames_count:
                        username_count += 1


                report_ftp_file.write(f'''╔═══════════════════════════════╗
║     EHoney Analysis Report    ║
╚═══════════════════════════════╝

* Tool Version: {version}
* Service used: FTP
* Total IPs: {ip_count}
* Total usernames tried: {username_count}

═════════════════════════════════

╔═══════════════════════════════╗
║               IPs             ║
╚═══════════════════════════════╝
    
''')

                for ip_ftp in ips_ftp_file:
                    iplookup = requests.get('https://ipinfo.io/' + ip_ftp.split('|')[0]).text
                    j = json.loads(iplookup)
                    report_ftp_file.write(f"{ip_ftp} | City: {j['city']} | Region: {j['region']} | Country: {j['country']} | Location: {j['loc'].replace(',', ', ')} | ISP: {j['org']} | Zipcode: {j['postal']} | Timezone: {j['timezone']}\n")

                report_ftp_file.write('''
\n═════════════════════════════════

╔═══════════════════════════════╗
║        Usernames Tried        ║
╚═══════════════════════════════╝

''')

                for all_file_usernames in glob.glob(f'{ftp_report_folder}/usernames_tried/*.txt'):
                    file_usernames = open(all_file_usernames, 'r').read().splitlines()
                    for username in file_usernames:
                        report_ftp_file.write(username + '\n')

                report_ftp_file.write('\n═════════════════════════════════')
                report_ftp_file.close()
                print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Report created!')

            if select_report_format == '02' or select_report_format == '2':
                ftp_report_folder = input(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Put the path where the ftp log folder is: ')
                print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Creating report')

                report_ftp_file = open(f'reports/ftp_report_{date_today}.html', 'a')
                ips_ftp_file = open(f'{ftp_report_folder}/IPs.txt', 'r').read().splitlines()
                
                ip_count = 0
                for ip in ips_ftp_file:
                    ip_count += 1

                username_count = 0
                for all_usernames_count in glob.glob(f'{ftp_report_folder}/usernames_tried/*.txt'):
                    file_usernames_count = open(all_usernames_count, 'r').read().splitlines()
                    for x in file_usernames_count:
                        username_count += 1

                for ip_ftp in ips_ftp_file:
                    iplookup = requests.get('https://ipinfo.io/' + ip_ftp.split('|')[0]).text
                    j = json.loads(iplookup)
                    for all_file_usernames in glob.glob(f'{ftp_report_folder}/usernames_tried/*.txt'):
                        file_usernames = open(all_file_usernames, 'r').read().splitlines()
                        breakline = '\n'
                        report_md = {
                            'name': 'EHoney FTP Analysis Report',
                            'unmd': f'''# EHoney Analysis Report

[![N|Solid](https://media.discordapp.net/attachments/724351008440057950/882755118162935898/20210901_193204.png?width=412&height=412)](https://github.com/MrEmpy/EHoney)

##### Tool Version: {version}
##### Service used: FTP
##### Total IPs: {ip_count}
##### Total usernames tried: {username_count}

# IPs

```
{str(ips_ftp_file).replace("'", '').replace(',', ' | City: ' + j["city"] + ' | Region: ' + j['region'] + ' | Country: ' + j['country'] + ' | Location: ' + j['loc'].replace(',', ', ') + ' | ISP: ' + j['org'] + '| Zipcode: ' + j['postal'] + '| Timezone: ' + j['timezone'] + breakline)}
```

# Usernames Tried

```
{str(file_usernames).replace("'", '')}
```''',
                            'formatting': 'true',
                            'preview': 'false'
                        }
                r = requests.post('https://dillinger.io/factory/fetch_html', data=report_md)
                report_ftp_file.write(r.text.replace(',', '\n').replace('[', ' ').replace(']', '').replace('412', '262'))

                report_ftp_file.close()
                print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Report created!')

        if select_report == '02' or select_report == '2':
            print(f'''{Fore.LIGHTWHITE_EX}
    [01] Text Report
    [02] HTML Report
            ''')
            select_report_format = input(f'{Fore.LIGHTWHITE_EX}Select: ')
            if select_report_format == '01' or select_report_format == '1':
                telnet_report_folder = input(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Put the path where the telnet log folder is: ')
                print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Creating report')

                report_telnet_file = open(f'reports/telnet_report_{date_today}.txt', 'a')
                ips_telnet_file = open(f'{telnet_report_folder}/IPs.txt', 'r').read().splitlines()
                
                ip_count = 0
                for ip in ips_telnet_file:
                    ip_count += 1

                username_count = 0
                for all_usernames_count in glob.glob(f'{telnet_report_folder}/usernames_tried/*.txt'):
                    file_usernames_count = open(all_usernames_count, 'r').read().splitlines()
                    for x in file_usernames_count:
                        username_count += 1


                report_telnet_file.write(f'''╔═══════════════════════════════╗
    ║     EHoney Analysis Report    ║
    ╚═══════════════════════════════╝

    * Tool Version: {version}
    * Service used: Telnet
    * Total IPs: {ip_count}
    * Total usernames tried: {username_count}

    ═════════════════════════════════

    ╔═══════════════════════════════╗
    ║               IPs             ║
    ╚═══════════════════════════════╝
    
    ''')

                for ip_telnet in ips_telnet_file:
                    iplookup = requests.get('https://ipinfo.io/' + ip_telnet.split('|')[0]).text
                    j = json.loads(iplookup)
                    report_telnet_file.write(f"{ip_telnet} | City: {j['city']} | Region: {j['region']} | Country: {j['country']} | Location: {j['loc'].replace(',', ', ')} | ISP: {j['org']} | Zipcode: {j['postal']} | Timezone: {j['timezone']}\n")

                report_telnet_file.write('''
    \n═════════════════════════════════

    ╔═══════════════════════════════╗
    ║        Usernames Tried        ║
    ╚═══════════════════════════════╝

    ''')

                for all_file_usernames in glob.glob(f'{telnet_report_folder}/usernames_tried/*.txt'):
                    file_usernames = open(all_file_usernames, 'r').read().splitlines()
                    for username in file_usernames:
                        report_telnet_file.write(username + '\n')

                report_telnet_file.write('\n═════════════════════════════════')
                report_telnet_file.close()
                print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Report created!')



            if select_report_format == '02' or select_report_format == '2':
                telnet_report_folder = input(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Put the path where the telnet log folder is: ')
                print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Creating report')

                report_telnet_file = open(f'reports/telnet_report_{date_today}.html', 'a')
                ips_telnet_file = open(f'{telnet_report_folder}/IPs.txt', 'r').read().splitlines()
                
                ip_count = 0
                for ip in ips_telnet_file:
                    ip_count += 1

                username_count = 0
                for all_usernames_count in glob.glob(f'{telnet_report_folder}/usernames_tried/*.txt'):
                    file_usernames_count = open(all_usernames_count, 'r').read().splitlines()
                    for x in file_usernames_count:
                        username_count += 1

                for ip_telnet in ips_telnet_file:
                    iplookup = requests.get('https://ipinfo.io/' + ip_telnet.split('|')[0]).text
                    j = json.loads(iplookup)
                    for all_file_usernames in glob.glob(f'{telnet_report_folder}/usernames_tried/*.txt'):
                        file_usernames = open(all_file_usernames, 'r').read().splitlines()
                        breakline = '\n'
                        report_md = {
                            'name': 'EHoney Telnet Analysis Report',
                            'unmd': f'''# EHoney Analysis Report

[![N|Solid](https://media.discordapp.net/attachments/724351008440057950/882755118162935898/20210901_193204.png?width=412&height=412)](https://github.com/MrEmpy/EHoney)

##### Tool Version: {version}
##### Service used: Telnet
##### Total IPs: {ip_count}
##### Total usernames tried: {username_count}

# IPs

```
{str(ips_telnet_file).replace("'", '').replace(',', ' | City: ' + j["city"] + ' | Region: ' + j['region'] + ' | Country: ' + j['country'] + ' | Location: ' + j['loc'].replace(',', ', ') + ' | ISP: ' + j['org'] + '| Zipcode: ' + j['postal'] + '| Timezone: ' + j['timezone'] + breakline)}
```

# Usernames Tried

```
{str(file_usernames).replace("'", '')}
```''',
                            'formatting': 'true',
                            'preview': 'false'
                        }
                r = requests.post('https://dillinger.io/factory/fetch_html', data=report_md)
                report_telnet_file.write(r.text.replace(',', '\n').replace('[', ' ').replace(']', '').replace('412', '262'))

                report_telnet_file.close()
                print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Report created!')

        if select_report == '03' or select_report == '3':
            print(f'{Fore.LIGHTYELLOW_EX}[!] {Fore.LIGHTWHITE_EX}Building')


if __name__ == "__main__":
    if platform == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Fore.LIGHTRED_EX}[-] {Fore.LIGHTWHITE_EX}The script has been closed')
