import requests
import time

username = input("Username target: ")
msg = input("Pesan spam: ")
total = int(input("Jumlah: "))

url = "https://ngl.link/api/submit"

for i in range(total):
    try:
        data = {
            "username": username,
            "question": msg,
            "deviceId": "web_" + str(time.time())
        }
        r = requests.post(url, data=data)
        if r.status_code == 200:
            print(f"[{i+1}] OK")
        else:
            print(f"[{i+1}] Gagal")
    except:
        print(f"[{i+1}] Error")
    time.sleep(0.2)
