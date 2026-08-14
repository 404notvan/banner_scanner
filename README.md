# ⚡ Multithreaded Banner Scanner

> Lightweight, fast TCP port scanner and service banner grabber written in Python.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Tool Type](https://img.shields.io/badge/Tool-Network%20Recon-blue?style=flat)
![Architecture](https://img.shields.io/badge/Architecture-Multithreaded%20%2F%20OOP-orange?style=flat)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Stdlib)-brightgreen?style=flat)

---

## 📌 Overview

**Banner Scanner** adalah tool *reconnaissance* jaringan berbasis CLI yang dirancang untuk melakukan scanning port TCP secara simultan (*multithreaded*) sekaligus mengambil data banner (*banner grabbing*) dari layanan yang aktif. Tool ini membantu mengidentifikasi port terbuka dan mendeteksi jenis/versi layanan yang berjalan pada target IP atau hostname.

Dibuat menggunakan modul standar Python (`socket`, `threading`, `argparse`), tool ini ringan, cepat, dan tidak memerlukan instalasi dependensi pihak ketiga.

---

## ✨ Fitur Utama

- ⚡ **Multithreaded Scanning**: Menjalankan pengecekan port secara paralel untuk proses scanning yang cepat dan efisien.
- 🏷️ **Service Banner Grabbing**: Mengambil respons awal (*banner*) dari port terbuka untuk mengidentifikasi layanan (seperti SSH, HTTP, dsb).
- 🛠️ **CLI Argument Parser**: Fleksibel dalam menentukan target, rentang port (`-s`, `-e`), serta durasi timeout (`-t`).
- 🔍 **Dynamic Host Resolution**: Mendukung input berupa IP Address maupun Hostname/Domain.
- 🧱 **Clean OOP Architecture**: Kode terstruktur rapi berbasis kelas (`PortScanner`) sehingga mudah dipahami dan dikembangkan.
- 📦 **Zero External Dependencies**: Berjalan sepenuhnya menggunakan Python 3 Standard Library.

---

## 🧠 Alur Kerja Tool

```text
       ┌────────────────────────┐
       │   Input IP / Hostname   │
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │  Resolve Host Domain   │
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │ Multi-thread Port Scan │
       └───────────┬────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
    [Port Open]        [Port Closed]
         │
         ▼
 ┌───────────────┐
 │ Grab Banner   │
 └───────┬───────┘
         │
         ▼
 ┌───────────────┐
 │ Display Result│
 └───────────────┘
```

---

## ⚙️ Cara Penggunaan

### 1. Prasyarat
Pastikan Anda sudah menginstall **Python 3.x** di sistem Anda.

### 2. Jalankan Tool

```bash
# Scan default port (1 - 1024) pada localhost
python banner_scanner.py 127.0.0.1

# Scan target domain dengan rentang port dan timeout khusus
python banner_scanner.py scanme.nmap.org -s 20 -e 100 -t 0.5

# Menampilkan bantuan parameter CLI
python banner_scanner.py --help
```

### 3. Opsi Parameter CLI

| Parameter | Shorthand | Default | Deskripsi |
| :--- | :--- | :--- | :--- |
| `target` | - | *Wajib* | IP Address atau Hostname target |
| `--start-port` | `-s` | `1` | Port awal pencarian |
| `--end-port` | `-e` | `1024` | Port akhir pencarian |
| `--timeout` | `-t` | `1.0` | Batas waktu respon per port (dalam detik) |

---

## 📊 Contoh Output

```text
[+] Port 22 OPEN
[+] Port 80 OPEN
[+] Banner Port 22 : SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5
[+] Banner Port 80 : HTTP/1.1 200 OK
```

---

## ⚠️ Penafian (Disclaimer)

Tool ini dibuat untuk **tujuan edukasi, riset, dan pengujian keamanan legal (authorized security testing)**. Jangan gunakan tool ini pada jaringan atau sistem tanpa izin resmi dari pemilik target. Penggunaan tool ini sepenuhnya menjadi tanggung jawab pengguna.

