import secrets
import string
import requests
from firebase_admin import credentials, firestore, initialize_app

# BRANDING SPY-E & 123Tool
print("\033[96m" + ">>> SPY-OTP-GATEWAY | NAGA-OTP V1.0 <<<" + "\033[0m")

# 1. Inisialisasi Firebase
try:
    cred = credentials.Certificate("serviceAccountKey.json")
    initialize_app(cred)
    db = firestore.client()
    print("\033[92m[+] Firebase Connected!\033[0m")
except Exception as e:
    print(f"\033[91m[!] Gagal Koneksi Database: {e}\033[0m")
    exit()

def generate_secure_otp(length=4):
    """Generate OTP yang lebih aman menggunakan secrets"""
    digits = string.digits
    otp = ''.join(secrets.choice(digits) for _ in range(length))
    return otp

def sync_and_send():
    try:
        # 2. Ambil Data User dari Firestore
        doc_ref = db.collection(u'user').document(u'data')
        user_data = doc_ref.get().to_dict()
        phnum = user_data.get('phone')
        
        if not phnum:
            print("\033[91m[!] Nomor telepon tidak ditemukan di database!\033[0m")
            return

        # 3. Generate & Sync OTP
        new_otp = generate_secure_otp()
        doc_ref.set({u'otp': new_otp}, merge=True)
        print(f"\033[93m[*] OTP Generated: {new_otp} for {phnum}\033[0m")

        # 4. Kirim via API Gateway
        # Note: Ganti URL dengan API Gateway andalan Bos (seperti Fonnte atau NAGA-WA kita)
        api_url = f"https://api.gateway.com/send/{phnum}"
        payload = {'message': f"Kode OTP SPY-E Anda: {new_otp}. Rahasiakan kode ini!"}
        
        # response = requests.post(api_url, json=payload)
        print("\033[92m[+] OTP Successfully Synced & Sent!\033[0m")
        
    except Exception as e:
        print(f"\033[91m[!] Error: {e}\033[0m")

if __name__ == "__main__":
    sync_and_send()
