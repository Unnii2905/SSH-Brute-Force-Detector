SSH Brute-Force Detector (Python + IPTables)

This is a simple but effective Python script I wrote to detect brute-force attacks on SSH and automatically block the attacker’s IP using iptables.
If someone keeps failing to log in through SSH, this script catches that and blocks them before they get any further. No more guessing passwords!!

What it does:
Looks through SSH logs using journalctl (works on systemd-based systems)
Finds repeated failed login attempts
Tracks how many times each IP fails
If an IP fails more than a set number of times (default: 3,can be changed on the code), it's blocked using iptables
Keeps logs of who was blocked and when


REQUIREMENTS

Python
linux system
SSH service running
root privilages 
Ip tables


HOW TO USE:

1. Clone the repo
2. create log files
  mkdir -p logs
  touch logs/blocklist.txt logs/attacker_log.txt
3. Run the script
sudo python3 detect_brute.py
(make sure you are on root)

why i made this:
i wanted to make a small project that was useful for real world works
also easy to expand

Open to feedback, ideas, or collabs!

