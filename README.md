⚡ SANGSENIMAMWARTEFAK

Brutal Force SQL Injection Scanner

A lightweight Python tool for authorized web security testing and educational research.

<p align="center">"Python" (https://img.shields.io/badge/Python-3.x-00ff9c?style=flat-square&logo=python&logoColor=white)
"Security" (https://img.shields.io/badge/Security-SQLi-ff0055?style=flat-square)
"Status" (https://img.shields.io/badge/Status-Experimental-ffaa00?style=flat-square)
"License" (https://img.shields.io/badge/License-MIT-00aaff?style=flat-square)

</p>«Scan responsibly. Learn aggressively. Break nothing you don't own.»

---

🧠 Overview

SANGSENIMAMWARTEFAK adalah scanner berbasis Python yang dirancang untuk membantu proses security assessment terhadap aplikasi web yang dimiliki sendiri atau telah memberikan izin pengujian.

Tool ini melakukan pengujian terhadap parameter dan form web untuk mencari indikasi SQL Injection menggunakan beberapa teknik detection.

Detection

- 🔎 GET parameter discovery
- 📝 POST form discovery
- ⚠️ Error-based detection
- 🔀 Boolean-based detection
- ⏱️ Time-based detection
- 🗄️ Basic database fingerprinting
- 🍪 Cookie-based authenticated testing
- 🌐 HTTP/HTTPS proxy support
- 🎨 Colored terminal interface
- 💾 Assessment result logging

---

✨ Features

Feature| Description
🔎 Parameter Discovery| Mendeteksi parameter GET yang dapat diuji
📝 Form Discovery| Mengidentifikasi input dari HTML form
⚠️ Error Detection| Menganalisis indikasi SQL error pada response
🔀 Boolean Testing| Membandingkan response berdasarkan kondisi true/false
⏱️ Time-Based Testing| Mendeteksi response delay yang mencurigakan
🍪 Cookie Support| Mendukung testing pada sesi yang telah diautentikasi
🌐 Proxy Support| Mendukung HTTP/HTTPS proxy
🎨 CLI Interface| Output terminal dengan ANSI colors
💾 Result Logging| Menyimpan hasil assessment

---

🛠️ Requirements

- Python 3.x
- "requests"
- "beautifulsoup4"

Check Python version:

python3 --version

---

📦 Installation

Clone repository:

git clone https://github.com/USERNAME/SANGSENIMAMWARTEFAK.git
cd SANGSENIMAMWARTEFAK

Install dependencies:

pip3 install -r requirements.txt

Atau:

pip install -r requirements.txt

---

🚀 Usage

Basic Scan

python3 main.py --url "https://LAB-TARGET.example/item?id=1"

Authenticated Testing

Jika environment membutuhkan session cookie:

python3 main.py \
  --url "https://LAB-TARGET.example/item?id=1" \
  --cookie "session=YOUR_AUTHORIZED_SESSION"

«Note: Ganti URL dengan target laboratory/staging yang memang kamu miliki atau memiliki izin untuk diuji.»

---

🔬 Detection Flow

TARGET
  │
  ▼
Parameter Discovery
  │
  ▼
Baseline Response
  │
  ▼
SQL Injection Tests
  │
  ├── Error Based
  │
  ├── Boolean Based
  │
  └── Time Based
  │
  ▼
Response Analysis
  │
  ▼
Assessment Result

---

🖥️ Example

Contoh output terminal:

[SANGSENIMAMWARTEFAK] Testing GET param: id
[SANGSENIMAMWARTEFAK] Testing GET param: page
[SANGSENIMAMWARTEFAK] Testing GET param: search

[!!!] VULNERABLE!
Parameter : id
Type      : TIME-BASED

[+] Assessment completed.

«Output di atas hanya contoh ilustrasi. Hasil aktual bergantung pada aplikasi dan environment pengujian.»

---

📁 Project Structure

SANGSENIMAMWARTEFAK/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

---

🧪 Recommended Labs

Untuk belajar SQL Injection secara legal, gunakan environment yang memang dibuat untuk security testing.

Beginner

- DVWA
- OWASP Juice Shop
- WebGoat

Advanced

- PortSwigger Web Security Academy
- Local PHP/MySQL laboratory
- Authorized CTF environments
- Dedicated security testing environments

---

🛡️ Defensive Security

Hasil dari security assessment dapat digunakan untuk membantu developer menemukan area aplikasi yang membutuhkan perbaikan.

Recommended Protection

┌──────────────────────────────┐
│     SQL INJECTION DEFENSE    │
├──────────────────────────────┤
│                              │
│  ✓ Prepared Statements       │
│  ✓ Parameterized Queries     │
│  ✓ Input Validation          │
│  ✓ Least-Privilege DB User   │
│  ✓ Secure Error Handling     │
│  ✓ Authentication Controls   │
│  ✓ Security Monitoring       │
│                              │
└──────────────────────────────┘

Prepared statements dan parameterized queries harus menjadi pertahanan utama terhadap SQL Injection.

---

⚠️ Disclaimer

SANGSENIMAMWARTEFAK dibuat untuk:

- educational purposes;
- authorized security testing;
- local security laboratories;
- CTF environments;
- aplikasi atau infrastructure yang memang memberikan izin pengujian.

Jangan menjalankan scanner terhadap sistem pihak lain tanpa authorization.

Developer tidak bertanggung jawab atas:

- unauthorized usage;
- downtime atau excessive requests;
- data loss;
- damage terhadap target;
- konsekuensi hukum akibat penyalahgunaan tool.

«Only scan systems you own or have explicit permission to test.»

---

🤝 Contributing

Contribution dipersilakan untuk peningkatan yang berkaitan dengan:

- 🐛 Bug fixes
- ⚡ Performance
- 🧹 Code quality
- 📚 Documentation
- 🧪 Test coverage
- 🔐 Defensive security research

Untuk perubahan besar, buat issue terlebih dahulu sebelum mengirim pull request.

---

📜 License

Distributed under the MIT License.

See "LICENSE" for more information.

---

⭐ Support

Jika project ini berguna untuk pembelajaran security:

⭐ Star — 🍴 Fork — 🐛 Report Issues — 💡 Suggest Improvements

---

<div align="center">⚡ SANGSENIMAMWARTEFAK

Security Research • Authorized Testing • Education

"scan responsibly"

</div>
