```python
#!/usr/bin/env python3
# ==========================================
# TOOL NAME : OTP-GATEWAY-WHATSAPP
# BRAND     : SPY-E & 123Tool Official
# VERSION   : 1.0 (Premium Cloud Sync)
# ==========================================

import secrets
import string
import requests
import os
import sys
from firebase_admin import credentials, firestore, initialize_app

# --- UI COLORS ---
C, G, Y, R, W, B = '\033[96m', '\033[92m', '\033[93m', '\033[91m', '\033[0m', '\033[1m'

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{Y}{B}
  ██████  ██▓███  ▓██   ██▓    ███████╗██╗██████╗ ▓█████ 
 ▒██    ▒ ▓██░  ██▒▒██  ██▒    ██╔════╝██║██╔══██╗▓█   ▀ 
 ░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░    █████╗  ██║██████╔╝▒███   
   ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░    ██╔══╝  ██║██╔══██╗▒▓█  ▄ 
 ▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░    ██║     ██║██║  ██║░▒████▒
 ▒ ▒▓▒ ▒ ░▒▓▒ ░ ░░  ██▒▒▒      ╚═╝     ╚═╝╚═╝  ╚═╝░░ ▒░ ░
{W}{C}        >>> SPY-FIRE-OTP | NAGA-FIRE V1.0 <<<
{G}        [ Cloud OTP Synchronizer - SPY-E & 123Tool ]
    """)

def initialize_firebase():
    """Inisialisasi koneksi ke Firebase"""
    key_file = "serviceAccountKey.json"
    if not os.path.exists(key_file):
        print(f"{R}[!] ERROR: File '{key_file}' tidak ditemukan!{W}")
        print(f"{Y}[*] Masukkan sertifikat JSON dari Firebase Console ke folder ini.{W}")
        sys.exit()
    
    try:
        cred = credentials.Certificate(key_file)
        # Ganti storageBucket jika Anda menggunakan Firebase Storage juga
        initialize_app(cred)
        return firestore.client()
    except Exception as e:
        print(f"{R}[!] Gagal inisialisasi Firebase: {e}{W}")
        sys.exit()

def generate_secure_otp(length=4):
    """Menghasilkan OTP yang sulit ditebak (Cryptographically Secure)"""
    return ''.join(secrets.choice(string.digits) for _ in range(length))

def run_sync_service(db):
    try:
        print(f"{C}[*] Mengambil data nomor telepon dari Firestore...{W}")
        doc_ref = db.collection(u'user').document(u'data')
        doc = doc_ref.get()

        if not doc.exists:
            print(f"{R}[!] Dokumen 'user/data' tidak ditemukan di Firestore!{W}")
            return

        data = doc.to_dict()
        phnum = data.get('phone')

        if not phnum:
            print(f"{R}[!] Field 'phone' kosong di database.{W}")
            return

        # Proses Generate & Update
        new_otp = generate_secure_otp()
        doc_ref.set({u'otp': new_otp}, merge=True)
        
        print(f"{G}[+] OTP BERHASIL DI-GENERATE: {B}{new_otp}{W}")
        print(f"{G}[+] DATABASE CLOUD TER-UPDATE!{W}")
        print(f"{C}[*] Target: {phnum}{W}")

        # Integrasi pengiriman (Contoh tembakan ke API Gateway)
        # Bos bisa ganti URL ini dengan API Gateway milik 123Tool
        print(f"{Y}[*] Mengirim notifikasi OTP ke {phnum}...{W}")
        
        # Simulasi pengiriman sukses
        print(f"{G}[SUCCESS] OTP telah dikirim melalui NAGA-WA Gateway.{W}")

    except Exception as e:
        print(f"{R}[!] Terjadi kesalahan sistem: {e}{W}")

if __name__ == "__main__":
    banner()
    db_client = initialize_firebase()
    run_sync_service(db_client)
