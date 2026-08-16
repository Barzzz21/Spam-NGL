#!/bin/bash

G='\033[0;32m'
C='\033[0;36m'
W='\033[0m'

clear
echo -e "${C}"
echo "╔═══════════════════════════════════════════╗"
echo "║       🔥 TITAN SPAM NGL 🔥               ║"
echo "║    Created by : @Barxzzz                  ║"
echo "║    Mode       : 100% Work + Proxy         ║"
echo "╚═══════════════════════════════════════════╝"
echo -e "${W}"

echo -e "${G}[+] Install dependencies...${W}"
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install --upgrade pip
pip install -r requirements.txt

echo -e "${G}[+] Menjalankan TITAN mode...${W}"
python titan.py
