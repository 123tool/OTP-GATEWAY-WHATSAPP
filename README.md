# 🔥 OTP GATEWAY WHATSAPP
> **Advanced Firebase-Synced OTP Delivery & Verification System**

![Firebase](https://img.shields.io/badge/Firebase-Cloud-orange.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Brand](https://img.shields.io/badge/Brand-SPY--E%20%26%20123Tool-blue.svg)

**OTP GATEWAY WHATSAPP** adalah sistem pengiriman kode verifikasi (OTP) otomatis yang terintegrasi langsung dengan **Google Firebase Firestore**. Dirancang untuk keamanan tingkat tinggi pada sistem login aplikasi atau verifikasi transaksi premium.

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
```
### 3. Menjalankan Tool
```bash
python spy_fire_otp.py
```

### 🚀 Cara Penggunaan

**​Pastikan file serviceAccountKey.json sudah ada di folder.
​Pastikan di Firestore Anda sudah ada Collection user dengan Document data yang berisi field phone.
​Jalankan script, dan sistem akan otomatis mengupdate field otp di database serta mengirimkan notifikasi.**

### Instruksi Penggunaan Pro :
1. **​File JSON** : 
File serviceAccountKey.json adalah kunci utama. Jangan sampai bocor ke orang lain atau di-upload ke GitHub publik tanpa .gitignore.

2. **​Firestore Structure** :
   • ​Create Collection : user
   • Create Document ID : data
   • ​Add Field : phone (Isi nomor tujuan,
   misal: 0812xxxx)

3. **​Cross-Platform** :
   Di Termux, Cukup ketik python
   ```bash
   spy_fire_otp.py
   ```
   Di CMD Windows, caranya sama. ​Secrets
   Library : Kode awal pakai random.random()
   yang bisa diprediksi oleh bot. Kode
   pakai secrets yang mustahil ditebak.

   ​Efficient Set : Update database dilakukan
   sekali secara kolektif (Merge Mode), tidak
   per-digit seperti kode awal yang bikin
   boros kuota API Firebase

## ​⚠️ Disclaimer

**​Gunakan untuk keperluan pengembangan sistem keamanan internal. Segala bentuk penyalahgunaan adalah tanggung jawab pengguna.**
