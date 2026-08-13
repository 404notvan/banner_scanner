# 🐍 Learning Python — Day 5

> Progress belajar Python untuk persiapan **Ethical Hacking** (Red Team & Blue Team)

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)
![Day](https://img.shields.io/badge/Day-5-blue?style=flat)
![Focus](https://img.shields.io/badge/Focus-OOP%2C%20Multithreading%20%26%20Banner%20Grabbing-orange?style=flat)

---

## 📖 Daftar Isi

- [🎯 Fokus Hari Ini](#-fokus-hari-ini)
- [📚 Konsep & Kode Kunci](#-konsep--kode-kunci)
- [✨ Fitur Utama](#-fitur-utama)
- [⚙️ Cara Menjalankan](#️-cara-menjalankan)
- [🧠 Alur Kerja Program](#-alur-kerja-program)
- [📌 Progress Roadmap](#-progress-roadmap)
- [⚠️ Ethical Use](#️-ethical-use)

---

## 🎯 Fokus Hari Ini

Melanjutkan materi socket dari Day 4, hari ini memfokuskan pengembangan scanner menjadi lebih cepat, terstruktur, dan kaya informasi:

> ⚡ **Multithreaded Port Scanner & Banner Grabber (OOP Based)**

Hari ini mempelajari 3 konsep penting:
1. **Object-Oriented Programming (OOP)**: Membungkus logika scanning ke dalam class `PortScanner`.
2. **Multithreading**: Menggunakan module `threading` agar proses scanning port berjalan secara simultan (jauh lebih cepat).
3. **Banner Grabbing**: Mengambil respons service/banner dari port yang terbuka menggunakan `s.recv()`.

---

## 📚 Konsep & Kode Kunci

### 1️⃣ Class & Object-Oriented Programming (OOP)
Mengorganisasi variabel target, timeout, dan port terbuka dalam struktur class:
```python
class PortScanner:
    def __init__(self, target, timeout=1.0):
        self.target = target
        self.timeout = timeout
        self.open_ports = []
```

### 2️⃣ Multithreading untuk Speed Up
Menjalankan pengecekan port secara bersamaan (parallel) menggunakan `threading.Thread`:
```python
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=self._scan_worker, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### 3️⃣ Banner Grabbing
Menerima respons data pertama dari port terbuka untuk mengidentifikasi layanan (misal: SSH, HTTP version):
```python
def grab_banner(self, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(self.timeout)
        try:
            s.connect((self.target, port))
            banner = s.recv(1024)
            print(banner.decode(errors="ignore"))
        except (socket.timeout, ConnectionRefusedError):
            return None
```

---

## ✨ Fitur Utama

- ✅ **Fast Multithreaded Scanning**: Scan ratusan port dalam hitungan detik.
- ✅ **OOP Architecture**: Codebase rapi, modular, dan gampang dikembangkan.
- ✅ **Banner Grabbing**: Menampilkan banner service pada port yang aktif.
- ✅ **CLI Arguments**: Custom target, port range (`-s`, `-e`), dan timeout (`-t`).
- ✅ **Error & Host Validation**: Validasi IP/hostname dan penanganan exception yang aman.

---

## ⚙️ Cara Menjalankan

### 🚀 Usage Contoh

```bash
# Scan default port range (1 - 1024)
python banner_scanner.py 127.0.0.1

# Custom port range & timeout
python banner_scanner.py 192.168.1.1 -s 20 -e 100 -t 0.5

# Melihat opsi help CLI
python banner_scanner.py --help
```

---

## 🧠 Alur Kerja Program

```text
Input Target ──► Resolve Hostname ──► Launch Multi-Threads ──► Check TCP Port
                                                                    │
                                                            ┌───────┴───────┐
                                                            ▼               ▼
                                                         [OPEN]          [CLOSED]
                                                            │
                                                            ▼
                                                     Grab Service Banner
```

---

## 📌 Progress Roadmap

- [x] File Handling & Exception Handling
- [x] Regex & Standard Modules (`os`, `sys`, `argparse`)
- [x] Basic Socket Programming (Day 4)
- [x] **OOP, Multithreading & Banner Grabbing (Day 5)**
- [ ] HTTP Requests & Web Scraping
- [ ] Automation & Security Tooling

---

## ⚠️ Ethical Use

Project ini dibuat murni untuk **tujuan edukasi dan pembelajaran cybersecurity**.

> 🔐 **Learn security. Practice responsibly.**  
Gunakan tool ini hanya pada perangkat sendiri, localhost, atau target yang secara sah memberikan izin pengujian.

---

<p align="center">
  <i>🐍 Learning Python step by step.</i><br>
  <i>🔐 Building the foundation for Ethical Hacking & Security Tools.</i>
</p>
