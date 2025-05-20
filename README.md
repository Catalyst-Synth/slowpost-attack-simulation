# Simulasi Serangan DDoS (Slow POST) via File Tersembunyi

## 📌 Deskripsi
Repositori ini adalah simulasi riset untuk memahami cara kerja teknik stealth malware dan serangan Slow POST DDoS. Sistem dirancang **khusus untuk lingkungan uji coba (virtual lab)** menggunakan Metasploitable2 sebagai target dan Kali Linux sebagai perangkat attacker.

## ⚠️ Disclaimer
Proyek ini **hanya untuk kepentingan edukasi dan pengujian di lingkungan pribadi atau lab tertutup**. Segala bentuk penyalahgunaan terhadap sistem yang bukan milik pribadi atau tanpa izin adalah **tindakan ilegal dan sepenuhnya bukan tanggung jawab pengembang proyek ini**.

## 🗂️ Struktur Berkas
Slow-Post
├── dummy.pdf # PDF asli (tidak berbahaya) dapat diperbanyak sesuai kebutuhan.
├── Laporan_TA_Final.pdf # PDF yang jika dibuka akan menjalankan .sh tersembunyi
└── .common/
    └── temp/
        ├── desktop_notify.sh # Menjalankan skrip Python di background
        ├── update_check.py # Script utama untuk serangan Slow POST
    ├── checksum # file dummy pengecoh (opsional)
    ├── lisence # file dummy pengecoh (opsional)
    ├── log # file dummy pengecoh (opsional)
    ├── README.txt # file dummy pengecoh (opsional)

## 💣 Cara Kerja Simulasi
1. Pengguna membuka `Laporan_TA_Final.pdf` → trigger file `.desktop` atau exploit embedded.
2. Script `desktop_notify.sh` dijalankan secara stealth (background).
3. `desktop_notify.sh` mengeksekusi `update_check.py` untuk mulai serangan Slow POST ke target IP lokal.
4. Script berjalan terus di background hingga dihentikan manual (via task manager atau reboot).

## 🧪 Target Simulasi
- **Target:** `Metasploitable2` (localhost, IP bisa diatur)
- **Metode Serangan:** Slow POST DDoS
- **Bahasa:** Python & Shell

## ✅ Catatan Etis
- Semua testing dilakukan pada **lab pribadi dan mesin virtual**.
- Proyek ini **tidak memuat binary payload, exploit, atau eksekusi otomatis terhadap pihak ketiga**.

## 📄 Lisensi
MIT License — Bebas digunakan untuk edukasi dan riset.
