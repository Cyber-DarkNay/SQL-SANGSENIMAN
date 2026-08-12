# ⚡ SANGSENIMAMWARTEFAK

### Brutal Force SQL Injection Scanner

<p align="center">
  <b>Lightweight Python tool for authorized web security testing & educational research.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Security-Authorized%20Testing-E63946?style=for-the-badge&logo=hackthebox&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-2EA44F?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Research-orange?style=for-the-badge">
</p>

<p align="center">
  <i>Scan responsibly. Learn aggressively. Break nothing you don't own.</i>
</p>

---

## 🧠 Overview

**SANGSENIMAMWARTEFAK** adalah scanner berbasis Python yang dirancang untuk membantu proses **security assessment** terhadap aplikasi web yang dimiliki sendiri atau telah memberikan izin pengujian.

Tool ini melakukan pengujian terhadap parameter dan form web untuk mencari **indikasi SQL Injection** menggunakan beberapa teknik detection.

> ⚠️ **Disclaimer:** Gunakan tool ini hanya terhadap sistem yang kamu miliki, laboratory environment, CTF, staging environment, atau target yang secara eksplisit memberikan izin pengujian.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔎 **GET Parameter Discovery** | Mendeteksi parameter GET yang dapat diuji |
| 📝 **POST Form Discovery** | Mengidentifikasi input dari HTML form |
| ⚠️ **Error-Based Detection** | Menganalisis indikasi SQL error pada response |
| 🔀 **Boolean-Based Detection** | Membandingkan response berdasarkan kondisi berbeda |
| ⏱️ **Time-Based Detection** | Mendeteksi response delay yang mencurigakan |
| 🗄️ **Database Fingerprinting** | Basic database fingerprinting |
| 🍪 **Cookie Support** | Mendukung authenticated session |
| 🌐 **Proxy Support** | Mendukung HTTP/HTTPS proxy |
| 🎨 **Colored CLI** | Interface terminal dengan ANSI colors |
| 💾 **Result Logging** | Menyimpan hasil assessment |

---

## 🛠️ Requirements

- Python **3.x**
- `requests`
- `beautifulsoup4`

### Check Python Version

```bash
python3 --version
