#!/bin/bash

# Warna
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

clear
echo -e "${CYAN}"
echo "╔═══════════════════════════════════════╗"
echo "║       🔥 SPAM-NGL-BARZ 🔥             ║"
echo "║    Created by : @Barxzzz              ║"
echo "║    Github    : github.com/BarzzID     ║"
echo "╚═══════════════════════════════════════╝"
echo -e "${NC}"

echo -e "${GREEN}[+] Install dependencies...${NC}"
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install --upgrade pip
pip install -r requirements.txt

echo -e "${GREEN}[+] Menjalankan spam...${NC}"
python spam.py
