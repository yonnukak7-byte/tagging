import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_CHAT_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_AUDIO_URL = "https://api.groq.com/openai/v1/audio/transcriptions"

def dapatkan_tag(teks_podcast, candidate_labels=None):
    """
    Menganalisis teks podcast dan mengembalikan daftar tag otomatis
    menggunakan model Llama-3 di Groq Cloud (Gratis & Sangat Cepat).
    """
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY belum diisi di file .env")

    if candidate_labels is None:
        candidate_labels = ["agama", "podcast santai", "horor", "edukasi", "bisnis", "komedi", "teknologi", "kesehatan"]

    labels_str = ", ".join(candidate_labels)
    prompt = f"""Kamu adalah asisten AI klasifikasi konten podcast.
Tugasmu: Pilih 1 sampai 3 tag yang PALING SESUAI dari daftar pilihan yang diberikan berdasarkan teks podcast.

Pilihan Tag yang Tersedia: [{labels_str}]

Teks Podcast:
\"\"\"{teks_podcast}\"\"\"

Aturan:
- HANYA pilih tag yang ada dalam daftar di atas.
- Berikan respon HANYA dalam format JSON array berisi tag terpilih, contoh: ["agama", "edukasi"]
- Jangan tambahkan teks pembuka atau penutup lain."""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are an expert podcast categorization assistant. Output only valid JSON arrays."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1,
        "response_format": {"type": "json_object"} if False else None
    }

    response = requests.post(GROQ_CHAT_URL, headers=headers, json=payload, timeout=20)
    data = response.json()

    if "error" in data:
        print(f"Error dari Groq: {data['error'].get('message', data['error'])}")
        return []

    content = data["choices"][0]["message"]["content"].strip()
    try:
        # Coba parse JSON jika format array
        tags = json.loads(content)
        if isinstance(tags, list):
            return tags
        elif isinstance(tags, dict) and "tags" in tags:
            return tags["tags"]
    except Exception:
        pass

    # Fallback pencocokan kata
    matched = [lbl for lbl in candidate_labels if lbl.lower() in content.lower()]
    return matched if matched else [candidate_labels[0]]


def audio_ke_teks_dan_tag(audio_path, candidate_labels=None):
    """
    Fitur STT (Speech-to-Text) menggunakan Whisper-large-v3 di Groq,
    lalu otomatis memberi tag pada hasil transkripsinya.
    """
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY belum diisi di file .env")

    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"File audio tidak ditemukan: {audio_path}")

    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}

    with open(audio_path, "rb") as f:
        files = {
            "file": (os.path.basename(audio_path), f),
            "model": (None, "whisper-large-v3"),
            "language": (None, "id"),
            "response_format": (None, "json")
        }
        res = requests.post(GROQ_AUDIO_URL, headers=headers, files=files, timeout=60)
        data = res.json()

    if "error" in data:
        print(f"Error STT Whisper: {data['error']}")
        return None, []

    teks_transkripsi = data.get("text", "")
    tag_terpilih = dapatkan_tag(teks_transkripsi, candidate_labels)

    return teks_transkripsi, tag_terpilih


if __name__ == "__main__":
    # Uji Coba Auto-Tag Teks
    contoh_teks = "Selamat datang di podcast bedah iman. Hari ini kita bahas dosa menurut ajaran Katolik..."
    print("=== MENGUJI AUTO-TAG DENGAN GROQ (LLAMA 3.3) ===")
    print("Teks:", contoh_teks)
    tags = dapatkan_tag(contoh_teks)
    print("Hasil Tag Otomatis:", tags)
