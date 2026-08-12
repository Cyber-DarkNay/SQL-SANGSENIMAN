⚡ SANGSENIMAMWARTEFAK v2.0

<p align="center">Brutal Force SQL Injection Scanner

For authorized security testing & educational purposes.

</p><p align="center">"Python" (https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
"Security" (https://img.shields.io/badge/Security-SQLi-red?style=for-the-badge)
"Status" (https://img.shields.io/badge/Status-Experimental-orange?style=for-the-badge)
"License" (https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>╔══════════════════════════════════════════════════════╗
║       S A N G S E N I M A M W A R T E F A K        ║
║                                                      ║
║             Brutal Force SQLi Scanner               ║
║                 Untuk LO tersayang                  ║
╚══════════════════════════════════════════════════════╝

«🔥 Scan responsibly. Learn aggressively. Break nothing you don't own.»

---

🧠 About

SANGSENIMAMWARTEFAK adalah tool Python untuk membantu melakukan security assessment terhadap aplikasi web yang kamu miliki atau sistem yang secara eksplisit memberikan izin untuk diuji.

Tool ini melakukan automated testing terhadap parameter dan form untuk mencari indikasi SQL Injection.

🔎 Detection Methods

- GET parameter discovery
- POST form discovery
- Error-based SQL Injection detection
- Boolean-based testing
- Time-based testing
- Basic database fingerprinting
- Response-length analysis
- Authenticated testing menggunakan cookie
- HTTP/HTTPS proxy support
- Colorful CLI interface
- Result logging

---

✨ Features

Feature| Description
🔎 Parameter Scanner| Mencari parameter yang berpotensi injectable
📋 Form Scanner| Mendeteksi input dari HTML form
💥 Error Detection| Menganalisis indikasi SQL error
🔀 Boolean Testing| Membandingkan response true/false
⏱️ Time-Based Testing| Mendeteksi response delay yang mencurigakan
🍪 Cookie Support| Mendukung authenticated security testing
🌐 Proxy Support| Mendukung HTTP/HTTPS proxy
🎨 ANSI Interface| Output terminal berwarna
💾 Result Logging| Menyimpan hasil assessment

---

📦 Installation

1. Clone Repository

git clone https://github.com/USERNAME/SANGSENIMAMWARTEFAK.git
cd SANGSENIMAMWARTEFAK

2. Install Dependencies

pip install -r requirements.txt

Atau:

pip3 install -r requirements.txt

Dependencies

requests
beautifulsoup4

---

🚀 Usage

Basic

Jalankan scanner menggunakan:

python3 main.py --url "https://LAB-TARGET.example/item?id=1"

Dengan Cookie

Untuk authenticated testing pada sistem yang memang kamu punya izin untuk diuji:

python3 main.py \
  --url "https://LAB-TARGET.example/item?id=1" \
  --cookie "session=YOUR_AUTHORIZED_SESSION"

⚠️ Important

Gunakan tool ini hanya terhadap:

- ✅ Sistem milik sendiri
- ✅ Local laboratory
- ✅ CTF
- ✅ DVWA
- ✅ OWASP Juice Shop
- ✅ Staging environment
- ✅ Sistem dengan written authorization

Jangan melakukan scanning terhadap website pihak lain tanpa izin.

---

🔬 How It Works

Secara umum workflow scanner:

                    ┌─────────────────┐
                    │    TARGET URL   │
                    └────────┬────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │ Parameter Discovery   │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │    SQLi Detection     │
                 └───────────┬───────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │  ERROR   │   │ BOOLEAN  │   │   TIME   │
        │  BASED   │   │  BASED   │   │  BASED   │
        └────┬─────┘   └────┬─────┘   └────┬─────┘
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                 ┌───────────────────────┐
                 │   Assessment Result   │
                 └───────────┬───────────┘
                             │
                             ▼
                    ┌────────────────┐
                    │ Result Logging │
                    └────────────────┘

---

🖥️ Example Output

╔══════════════════════════════════════════════════════╗
║       S A N G S E N I M A M W A R T E F A K        ║
║             Brutal Force SQLi Scanner               ║
║                 Untuk LO tersayang                  ║
╚══════════════════════════════════════════════════════╝

[INFO] Target: https://LAB-TARGET.example/item?id=1
[INFO] Scanning dimulai...

[1] Scanning GET parameters...

[SANGSENIMAMWARTEFAK] Testing GET param: id
[SANGSENIMAMWARTEFAK] Testing GET param: page
[SANGSENIMAMWARTEFAK] Testing GET param: search

[!!!] VULNERABLE!
Parameter : id
Type      : TIME-BASED

[+] Assessment completed.

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

Kalau tujuanmu adalah belajar SQL Injection secara legal, gunakan environment yang memang dirancang untuk security testing.

🧰 Beginner

- DVWA
- OWASP Juice Shop
- WebGoat

🧠 Advanced

- PortSwigger Web Security Academy
- Local PHP/MySQL laboratory
- Dedicated CTF environments

---

🛡️ Defensive Security

Tool seperti ini juga bisa digunakan dari perspektif defensive security.

Developer dapat menggunakan hasil assessment untuk:

1. Mengidentifikasi parameter yang membutuhkan validasi.
2. Menguji penggunaan prepared statements.
3. Mengevaluasi konfigurasi database.
4. Mengidentifikasi endpoint yang perlu security review.
5. Memvalidasi perbaikan SQL Injection.

Recommended Remediation

┌─────────────────────────────────────┐
│       SQL INJECTION DEFENSE         │
├─────────────────────────────────────┤
│                                     │
│  ✓ Prepared Statements              │
│  ✓ Parameterized Queries            │
│  ✓ Input Validation                 │
│  ✓ Least-Privilege DB Accounts      │
│  ✓ Secure Error Handling            │
│  ✓ Proper Authentication            │
│  ✓ Security Monitoring              │
│                                     │
└─────────────────────────────────────┘

---

⚠️ Disclaimer

SANGSENIMAMWARTEFAK dibuat untuk educational purposes dan authorized security testing.

Developer tidak bertanggung jawab atas penggunaan tool terhadap sistem tanpa authorization.

Dengan menggunakan software ini, kamu bertanggung jawab atas aktivitas yang kamu lakukan.

«Only scan systems you own or have explicit permission to test.»

---

📜 License

Project ini menggunakan MIT License.

Pastikan file "LICENSE" pada repository sesuai dengan license yang dipilih.

---

🤝 Contributing

Pull request dan improvement dipersilakan untuk pengembangan yang berkaitan dengan:

- Bug fixes
- Code quality
- Detection reliability
- Performance improvements
- Documentation
- Safe security research

Untuk perubahan besar, sebaiknya buat issue terlebih dahulu sebelum membuat pull request.

---

⭐ Support

Kalau project ini membantu pembelajaran security kamu:

⭐ Star the repository
🍴 Fork the repository
🐛 Report bugs
💡 Suggest improvements
📚 Learn cybersecurity

---

⚡ SANGSENIMAMWARTEFAK

███████╗ █████╗ ███╗   ██╗ ██████╗ ███████╗███████╗███╗   ██╗
██╔════╝██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔════╝████╗  ██║
███████╗███████║██╔██╗ ██║██║  ███╗█████╗  █████╗  ██╔██╗ ██║
╚════██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══╝  ██║╚██╗██║
███████║██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝

Scan responsibly. Learn aggressively. Break nothing you don't own. ⚡
