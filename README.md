# Auto-Tagging Podcast & Audio (Versi 2)

Sistem pendeteksi dan klasifikasi otomatis kategori/tag untuk transkrip audio dan podcast menggunakan Hugging Face Zero-Shot Text Classification.

## 🚀 Fitur
- Deteksi tag otomatis tanpa perlu melatih model dari awal (*Zero-Shot Classification*).
- Pilihan label fleksibel (`agama`, `podcast santai`, `horor`, `edukasi`, `bisnis`, `komedi`, dll).
- Konfigurasi token aman menggunakan file `.env` agar tidak bocor ke repositori publik.

## 📦 Instalasi
1. Clone repositori ini:
   ```bash
   git clone https://github.com/yonnukak7-byte/tagging.git
   cd tagging
   ```

2. Pasang dependensi:
   ```bash
   pip install -r requirements.txt
   ```

3. Buat file `.env` dari `.env.example`:
   ```bash
   copy .env.example .env
   ```
   Lalu masukkan token Hugging Face gratis Anda ke dalam file `.env`.

## 🛠️ Penggunaan
Jalankan skrip:
```bash
python auto_tagger.py
```
