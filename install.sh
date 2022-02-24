#!/bin/bash
clear
printf "\033[0;33m       .;oOOOOd;. .;oOOOOd:.       
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
\n"
sleep 1

if [[ $EUID -ne 0 ]]; then
    printf "\033[0;33m[-] \033[0;37mThis script must be run as root" 
    exit 1
fi

main () {
    printf "\n\033[0;34m[*] \033[0;37mInstalling...\n"
    apt-get install python3-pip python3 -y
    pip install -r requirements.txt
    cp EHoney.py /usr/bin/ehoney
    chmod +x /usr/bin/ehoney
    chmod +x EHoney.py
    mkdir /etc/ehoney
    cp -r logs /etc/ehoney
    cp -r web /etc/ehoney
    cp -r reports /etc/ehoney
    cp -r config /etc/ehoney
    chmod 777 /etc/ehoney
    chmod 777 /etc/ehoney/logs
    chmod 777 /etc/ehoney/web
    chmod 777 /etc/ehoney/reports
    chmod 777 /etc/ehoney/config
    printf '\n\033[0;32m[+] \033[0;37mInstalled! Execute "ehoney".\nConfigure ports in "/etc/ehoney/config/ports.conf".\nLogs were in "/etc/ehoney/logs" and reports in "/etc/ehoney/reports".\n'
}

main
