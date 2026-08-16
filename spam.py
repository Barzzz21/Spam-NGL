#!/usr/bin/env python3
import requests
import time
import threading
import os
import sys
from datetime import datetime, timedelta

# Banner
banner = """
╔═══════════════════════════════════════╗
║       🔥 SPAM-NGL-BARZ 🔥             ║
║    Created by : @Barxzzz              ║
║    Github    : github.com/BarzzID     ║
╚═══════════════════════════════════════╝
"""

print(banner)

# Input user
target = input("Target (username NGL): ")
pesan = input("Pesan: ")
jumlah = int(input("Jumlah: "))
menit = int(input("Menit: "))

# Konfigurasi
url = "https://ngl.link/api/submit"
headers = {
    "User-Agent": "Mozilla/5.0 (Android 12; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0",
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

stop_spam = False
counter = 0

def spam():
    global counter
    while not stop_spam and counter < jumlah:
        try:
            data = {
                "username": target,
                "question": pesan,
                "deviceId": "android_" + str(time.time())[:10]
            }
            r = requests.post(url, data=data, headers=headers, timeout=5)
            if r.status_code == 200:
                counter += 1
                print(f"[✓] Spam ke-{counter} terkirim")
            else:
                print(f"[✗] Gagal ({r.status_code})")
        except Exception as e:
            print(f"[!] Error: {e}")
        time.sleep(0.1)

# Jalankan spam dalam thread
print(f"\n[+] Mulai spam ke @{target}")
print(f"[+] Pesan: {pesan}")
print(f"[+] Target: {jumlah} spam dalam {menit} menit\n")

threads = []
for _ in range(10):  # 10 thread paralel
    t = threading.Thread(target=spam)
    t.daemon = True
    t.start()
    threads.append(t)

# Timer otomatis stop
timeout = menit * 60
time.sleep(timeout)
stop_spam = True

print(f"\n[✓] Selesai! Total {counter} spam terkirim.")
