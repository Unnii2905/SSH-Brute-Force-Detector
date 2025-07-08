 SSH Brute-Force Detector (

A simple but effective Python script to detect brute-force SSH attacks and automatically block the attacker’s IP using `iptables`.

If someone repeatedly fails to log in via SSH, this tool catches it and blocks the IP before they get further 

---

What It Does:
 Monitors SSH logs using `journalctl` (for systemd-based systems)
 Detects repeated failed login attempts
 Tracks how many times each IP fails
 Blocks IPs after a threshold (default: 3 attempts)
 Keeps logs of who was blocked and when

---

 Requirements

 Linux system with systemd
 SSH service enabled
 Python 3
 Root privileges
 IPTables

---

 How to Use

1. Clone the repo

2. Create required log files(if they don't exist)
 mkdir -p logs
 touch logs/blocklist.txt logs/attacker_log.txt


3. Run the script (as root)
sudo python3 detect_brute.py
   

---

 Why I Made This

 I wanted to create a small tool that's actually useful in the real world something simple, effective, and easy to expand for learning.

---

Feel free to open an issue or reach out. Always open to improving this or working on something new!

---

