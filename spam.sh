#!/bin/bash

G='\033[0;32m'
C='\033[0;36m'
W='\033[0m'

clear
echo -e "${C}"
echo "╔═══════════════════════════════════════╗"
echo "║       🔥 SPAM-NGL-BARZ V2 🔥          ║"
echo "║    Created by : @Barxzzz              ║"
echo "║    Github    : github.com/BarzzID     ║"
echo "╚═══════════════════════════════════════╝"
echo -e "${W}"

echo -e "${G}[+] Install dependencies...${W}"
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install --upgrade pip
pip install -r requirements.txt

echo -e "${G}[+] Menjalankan spam...${W}"
python spam.py
