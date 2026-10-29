import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Menggunakan model klasifikasi teks open-source populer (Zero-Shot Classification)
# Rekomendasi model multi-bahasa / default Hugging Face Inference API
DEFAULT_MODEL_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
API_URL = os.getenv("HF_API_URL", DEFAULT_MODEL_URL)

# Token dapat diatur di file .env atau langsung di variabel environment
HF_TOKEN = os.getenv("HF_TOKEN", "HF_TOKEN_GRATIS_ANDA")
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def dapatkan_tag(teks_dari_podcast, candidate_labels=None, threshold=0.4):
    """
    Menganalisis teks podcast dan mengembalikan tag/kategori dengan probabilitas di atas threshold.
    """
    if candidate_labels is None:
        candidate_labels = ["agama", "podcast santai", "horor", "edukasi", "bisnis", "komedi"]

    payload = {
        "inputs": teks_dari_podcast,
        "parameters": {
            # Tentukan pilihan tag yang ingin Anda deteksi otomatis
            "candidate_labels": candidate_labels
        }
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()
    
    # Validasi respon jika terjadi error dari API
    if isinstance(data, dict) and "error" in data:
        print(f"Peringatan dari API: {data['error']}")
        return []

    # Mengambil tag dengan skor kecocokan tertinggi
    if isinstance(data, dict) and "labels" in data and "scores" in data:
        tags_terpilih = [label for label, score in zip(data["labels"], data["scores"]) if score > threshold]
        return tags_terpilih

    return []

if __name__ == "__main__":
    # Contoh Uji Coba
    teks = "Selamat datang di podcast bedah iman. Hari ini kita bahas dosa menurut ajaran Katolik..."
    print("Menganalisis teks...")
    hasil_tag = dapatkan_tag(teks)
    print("Output otomatis:", hasil_tag)
