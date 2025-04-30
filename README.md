# 🔍 Simple Python Port Scanner

A lightweight, beginner-friendly Python script to scan open ports on a target IP or domain. Built using only the standard library.

---

## ⚙️ Features

- Scans TCP ports (default: 1–1024)
- Reports open ports
- Lightweight and easy to understand
- Fast scanning with timeout handling
- Saves results (optional)

---


```bash
$ python3 port_scanner.py
Enter target IP or domain: scanme.nmap.org
[+] Port 22 is OPEN
[+] Port 80 is OPEN
Scan completed in 2.4 seconds.
