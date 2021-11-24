<h1 align="center">「🍯」About EHoney</h1>

![banner](assets/banner.png)

<img src="https://media.discordapp.net/attachments/724351008440057950/882755118162935898/20210901_193204.png?width=62&height=62">

EHoney is a simple non-interactive Honeypot developed in the python language. Made entirely with the socket module, it was created in order to obtain information about the intruder who is trying to enter some service.

In addition, EHoney offers some advantages to have a good result in the search for the intruder.

### Services:

* FTP
* Telnet
* Web

### Benefits:

* Automatic capture of IPs and users used during service authentication
* Text and HTML report
* Get information about an IP address
* Get users used during authentication
* Detection of port scanners like Nmap

### Available Reports:

- [x] FTP Report
- [X] Telnet Report
- [ ] Web Report

### Tested Operating Systems:

- [x] Linux
- [ ] MacOS
- [ ] Windows

### Install:

```
$ git clone https://github.com/MrEmpy/EHoney.git
$ cd EHoney
$ chmod +x EHoney.py
$ pip install -r requirements.txt
$ ./EHoney.py
```

### Screenshots:

#### Start
![start](assets/start.png)

#### Attacker
![attacker](assets/attacker.png)

#### Port Scanner Detected
![nmap](assets/nmap_detected.png)

#### HTML Report
![html report](assets/report.png)

#### Text Report
![text report](assets/report2.png)
