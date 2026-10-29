# API Auto-Tagging & Speech-to-Text (STT) Podcast dengan Groq Cloud

Sistem otomatisasi penandaan kategori (Auto-Tag) dan transkripsi suara ke teks (STT) menggunakan API Groq Cloud (Llama 3.3 & Whisper Large v3) yang **100% Gratis & Ultra Cepat**.

## 🚀 Fitur Unggulan
1. **Auto-Tagging Podcast**:
   - Ditenagai model **Llama 3.3 70B Versatile**.
   - Sangat akurat dalam memahami bahasa Indonesia dan istilah podcast.
   - Hasil tag dalam format JSON array yang siap diintegrasikan ke frontend atau database.
2. **Speech-to-Text (STT) Whisper**:
   - Ditenagai model **Whisper-large-v3** langsung dari Groq Cloud.
   - Mengubah file audio podcast (MP3, WAV, M4A) menjadi teks secara instan dan langsung mendeteksi tag-nya secara otomatis.

## 📦 Panduan Instalasi
1. Pasang pustaka dependensi:
   ```bash
   pip install -r requirements.txt
   ```

2. Buat file `.env` dan masukkan kunci API Groq:
   ```env
   GROQ_API_KEY=gsk_kunci_groq_anda
   ```
   *(Kunci gratis dapat diambil di [console.groq.com/keys](https://console.groq.com/keys))*

## 🛠️ Contoh Penggunaan
Jalankan file skrip:
```bash
python groq_tagger.py
```
