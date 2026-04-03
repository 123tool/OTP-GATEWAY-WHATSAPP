# 🔥 SPY-FIRE-OTP (NAGA-FIRE)
> **Advanced Firebase-Synced OTP Delivery & Verification System**

![Firebase](https://img.shields.io/badge/Firebase-Cloud-orange.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Brand](https://img.shields.io/badge/Brand-SPY--E%20%26%20123Tool-blue.svg)

**SPY-FIRE-OTP** adalah sistem pengiriman kode verifikasi (OTP) otomatis yang terintegrasi langsung dengan **Google Firebase Firestore**. Dirancang untuk keamanan tingkat tinggi pada sistem login aplikasi atau verifikasi transaksi premium.

## ⚡ Fitur Utama
- **Cloud Sync:** OTP yang dihasilkan otomatis terupdate di database Firebase.
- **Secure Secret:** Menggunakan library `secrets` (Cryptographically Strong) untuk generate kode.
- **Dynamic Fetching:** Menarik nomor telepon target secara otomatis dari Firestore.
- **Cross-Platform:** Berjalan mulus di Windows, Linux, maupun Termux.

## 📦 Instalasi & Setup

### 1. Persiapan Firebase
1. Buat proyek di [Firebase Console](https://console.firebase.google.com/).
2. Masuk ke **Project Settings** > **Service Accounts**.
3. Klik **Generate New Private Key**, lalu simpan filenya dengan nama `serviceAccountKey.json` di folder tool ini.

### 2. Install Dependensi
```bash
pip install firebase-admin requests
