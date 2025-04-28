# backend/scanner.py

import subprocess
import json

def scan_network(subnet):
    result = subprocess.run(["nmap", "-sn", subnet], capture_output=True, text=True)
    hosts = []
    for line in result.stdout.splitlines():
        if "Nmap scan report for" in line:
            hosts.append(line.split("for")[-1].strip())
    return hosts