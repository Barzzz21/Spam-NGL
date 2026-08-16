#!/usr/bin/env python3
import requests
import time
import threading
import os
import sys
from datetime import datetime, timedelta

# Warna
G = '\033[92m'
R = '\033[91m'
Y = '\033[93m'
C = '\033[96m'
B = '\033[94m'
W = '\033[0m'

os.system('clear' if os.name == 'posix' else 'cls')

banner = f"""
{C}╔═══════════════════════════════════════╗
║       {W}🔥 SPAM-NGL-BARZ V2 🔥{C}             ║
║    {W}Created by : @Barxzzz{C}              ║
║    {W}Github    : github.com/BarzzID{C}     ║
╚═══════════════════════════════════════╝{W}
"""

print(banner)

target = input(f"{G}[?] Target (username NGL): {W}")
pesan = input(f"{G}[?] Pesan: {W}")
jumlah = int(input(f"{G}[?] Jumlah: {W}"))
menit = int(input(f"{G}[?] Menit: {W}"))

url = "https://ngl.link/api/submit"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://ngl.link",
    "Referer": "https://ngl.link/"
}

stop_event = threading.Event()
counter = 0
success = 0
failed = 0
lock = threading.Lock()

def send_spam():
    global counter, success, failed
    while not stop_event.is_set():
        with lock:
            if counter >= jumlah:
                stop_event.set()
                break
            counter += 1
        try:
            data = {
                "username": target,
                "question": pesan,
                "deviceId": f"android_{int(time.time()*1000)}"
            }
            r = requests.post(url, data=data, headers=headers, timeout=10)
            if r.status_code == 200:
                with lock:
                    success += 1
                print(f"{G}[✓] Spam ke-{counter} berhasil{W}")
            else:
                with lock:
                    failed += 1
                print(f"{R}[✗] Spam ke-{counter} gagal (HTTP {r.status_code}){W}")
        except Exception as e:
            with lock:
                failed += 1
            print(f"{R}[!] Error: {str(e)[:30]}{W}")
        time.sleep(0.05)

print(f"\n{G}[+] Memulai spam ke @{target}{W}")
print(f"{G}[+] Pesan: {Y}{pesan}{W}")
print(f"{G}[+] Target: {Y}{jumlah} spam{W} dalam {Y}{menit} menit{W}\n")

threads = []
for _ in range(20):
    t = threading.Thread(target=send_spam)
    t.daemon = True
    t.start()
    threads.append(t)

timeout = menit * 60
time.sleep(timeout)
stop_event.set()

for t in threads:
    t.join(timeout=1)

print(f"\n{G}═══════════════════════════════════════{W}")
print(f"{G}[✓] SELESAI!{W}")
print(f"{G}[✓] Berhasil : {Y}{success}{W}")
print(f"{R}[✗] Gagal   : {Y}{failed}{W}")
print(f"{G}[✓] Total   : {Y}{success + failed}{W}")
print(f"{G}═══════════════════════════════════════{W}")
