#!/usr/bin/env python3
import socket
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
import sys

sys.path.append('/etc/ehoney')
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

    banner()
    print(f'''{Fore.LIGHTWHITE_EX}
    [01] Start FTP Honeypot
    [02] Start Telnet Honeypot
    [03] Start Web Honeypot
    [04] Create Report
    ''')
    select = input(f'{Fore.LIGHTWHITE_EX}Select: ')

    if select == '01' or select == '1':
        print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Honeypot is starting, good hunting ;)')
        time.sleep(3)
        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Honeypot started!\n')
        import config.ftp as ftp

    if select == '02' or select == '2':
        print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Honeypot is starting, good hunting ;)')
        time.sleep(3)
        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Honeypot started!\n')
        import config.telnet as telnet

    if select == '03' or select == '3':
        print(f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}Honeypot is starting, good hunting ;)')
        time.sleep(3)
        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}Honeypot started!\n')
        import config.web as web

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

                report_ftp_file = open(f'/etc/ehoney/reports/ftp_report_{date_today}.txt', 'a')
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
                    try:
                        iplookup = requests.get('https://ipinfo.io/' + ip_ftp.split('|')[0]).text
                        j = json.loads(iplookup)
                        report_ftp_file.write(f"{ip_ftp} | City: {j['city']} | Region: {j['region']} | Country: {j['country']} | Location: {j['loc'].replace(',', ', ')} | ISP: {j['org']} | Zipcode: {j['postal']} | Timezone: {j['timezone']}\n")
                    except:
                        pass

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

                report_ftp_file = open(f'/etc/ehoney/reports/ftp_report_{date_today}.html', 'a')
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
                    try:
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
                    except:
                        pass

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

                report_telnet_file = open(f'/etc/ehoney/reports/telnet_report_{date_today}.txt', 'a')
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
                    try:
                        iplookup = requests.get('https://ipinfo.io/' + ip_telnet.split('|')[0]).text
                        j = json.loads(iplookup)
                        report_telnet_file.write(f"{ip_telnet} | City: {j['city']} | Region: {j['region']} | Country: {j['country']} | Location: {j['loc'].replace(',', ', ')} | ISP: {j['org']} | Zipcode: {j['postal']} | Timezone: {j['timezone']}\n")
                    except:
                        pass

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

                report_telnet_file = open(f'/etc/ehoney/reports/telnet_report_{date_today}.html', 'a')
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
                    try:
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
                    except:
                        pass

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
