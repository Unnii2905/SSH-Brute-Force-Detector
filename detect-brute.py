import re
import subprocess
from collections import defaultdict
from datetime import datetime

BLOCK_THRESHOLD = 3
BLOCK_COMMAND = "iptables -A INPUT -s {ip} -j DROP"
BLOCKLIST_FILE = "logs/blocklist.txt"
ATTACKER_LOG_FILE = "logs/attacker_log.txt"

FAIL_PATTERN = re.compile(r"Failed password for(?: invalid user)? .* from (\d+\.\d+\.\d+\.\d+)")

blocked_ips = set()
try:
    with open(BLOCKLIST_FILE, 'r') as f:
        blocked_ips = set(line.strip() for line in f if line.strip())
except FileNotFoundError:
    pass

try:
    print("[*] Reading logs from journalctl...")
    log_data = subprocess.check_output(["journalctl", "-u", "ssh", "--no-pager", "--since", "today"]).decode()
    log_lines = log_data.splitlines()
    print(f"[+] Total log lines read: {len(log_lines)}")
except subprocess.CalledProcessError:
    print("[X] Failed to read SSH logs from journalctl")
    exit(1)

def block_ip(ip):
    print(f"[!] Blocking IP: {ip}")
    subprocess.run(BLOCK_COMMAND.format(ip=ip), shell=True)
    blocked_ips.add(ip)

    with open(BLOCKLIST_FILE, 'a') as f:
        f.write(ip + '\n')

    with open(ATTACKER_LOG_FILE, 'a') as f:
        f.write(f"[{datetime.now()}] Blocked {ip} after too many failed attempts\n")

failed_attempts = defaultdict(int)

for line in log_lines:
    if "Failed password" in line:
        print("[DEBUG] Log line:", line.strip())

    match = FAIL_PATTERN.search(line)
    if match:
        ip = match.group(1)
        failed_attempts[ip] += 1
        print(f"[DEBUG] Match: IP {ip}, Failed attempts: {failed_attempts[ip]}")
        if failed_attempts[ip] >= BLOCK_THRESHOLD and ip not in blocked_ips:
            block_ip(ip)
