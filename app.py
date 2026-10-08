git --versionimport streamlit as st
import os
import re
import base64
from collections import Counter



# =========================================================
# ANIMASI DAN ELEMEN BERGERAK
# =========================================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #EAF7FF, #FFF7E8, #EEFCEB, #F6EEFF);
    background-size: 400% 400%;
    animation: backgroundMove 14s ease infinite;
}
@keyframes backgroundMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.animated-card {
    animation: floatCard 4s ease-in-out infinite;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.animated-card:hover {
    transform: translateY(-7px) scale(1.02);
}
@keyframes floatCard {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
}
.floating-emoji {
    display: inline-block;
    font-size: 42px;
    animation: floatEmoji 3s ease-in-out infinite;
}
.floating-emoji.delay1 { animation-delay: 0.7s; }
.floating-emoji.delay2 { animation-delay: 1.4s; }
@keyframes floatEmoji {
    0%, 100% { transform: translateY(0) rotate(-3deg); }
    50% { transform: translateY(-13px) rotate(3deg); }
}
.hero-title {
    animation: titleIn 1s ease-out;
}
@keyframes titleIn {
    from { opacity: 0; transform: translateY(-18px); }
    to { opacity: 1; transform: translateY(0); }
}
.stButton > button {
    transition: all 0.25s ease;
}
.stButton > button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 8px 18px rgba(0,0,0,0.12);
}
section[data-testid="stSidebar"] .stRadio label {
    transition: transform 0.2s ease;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    transform: translateX(5px);
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================

st.set_page_config(
    page_title="Bahasa Indonesia Kelas IX",
    page_icon="📚",
    layout="wide"
)


# =========================================================
# TEMA VISUAL CERIA UNTUK SISWA SMP KELAS 9
# =========================================================

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 8% 12%, rgba(255, 229, 150, .55) 0 7%, transparent 18%),
        radial-gradient(circle at 92% 18%, rgba(164, 225, 255, .55) 0 8%, transparent 20%),
        radial-gradient(circle at 15% 92%, rgba(204, 180, 255, .35) 0 8%, transparent 22%),
        linear-gradient(135deg, #f8fbff 0%, #fff8e8 48%, #f1f8ff 100%);
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fff7d6 0%, #eef8ff 55%, #f5edff 100%);
    border-right: 2px solid rgba(99, 102, 241, .12);
}
h1 { color: #4338ca !important; font-weight: 800 !important; letter-spacing: -.5px; }
h2, h3 { color: #334155 !important; }
p, label, .stMarkdown { color: #334155; }
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 20px !important;
    border: 1px solid rgba(99, 102, 241, .12) !important;
    box-shadow: 0 8px 24px rgba(30, 41, 59, .07) !important;
    background: rgba(255,255,255,.82) !important;
}
.stButton > button {
    border-radius: 14px !important; border: 0 !important; min-height: 46px;
    font-weight: 750 !important; background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
    color: white !important; box-shadow: 0 7px 16px rgba(99,102,241,.24);
}
.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(99,102,241,.32); }
div[data-baseweb="select"] > div, textarea, input { border-radius: 13px !important; }
textarea { background: rgba(255,255,255,.9) !important; }
div[role="radiogroup"] { background: rgba(255,255,255,.55); border-radius: 14px; padding: 8px 12px; }
.study-banner {
    padding: 22px 26px; border-radius: 24px; margin: 4px 0 20px 0;
    background: linear-gradient(110deg, rgba(255,255,255,.94), rgba(239,246,255,.94));
    border: 2px solid rgba(99,102,241,.10); box-shadow: 0 10px 30px rgba(30,41,59,.08);
}
.study-banner .title { font-size: 1.75rem; font-weight: 850; color: #4338ca; }
.study-banner .subtitle { margin-top: 5px; color: #475569; }
.edu-icons { font-size: 1.55rem; letter-spacing: 9px; margin-bottom: 5px; }
div[data-testid="stAlert"] { border-radius: 14px !important; }

.student-hero { display:flex; align-items:center; justify-content:space-between; gap:18px; padding:20px 26px 10px; margin:0 0 20px; border-radius:26px; background:linear-gradient(105deg,#eef2ff 0%,#fff7ed 52%,#ecfeff 100%); border:2px solid rgba(99,102,241,.10); box-shadow:0 12px 30px rgba(30,41,59,.08); overflow:hidden; }
.student-copy { flex:1; min-width:300px; padding:8px 0 16px 4px; }
.mini-badge { display:inline-block; padding:6px 11px; border-radius:999px; background:#ffffff; color:#4f46e5; font-size:.78rem; font-weight:800; box-shadow:0 4px 12px rgba(79,70,229,.10); }
.student-title { margin-top:10px; font-size:1.65rem; font-weight:850; color:#312e81; }
.student-text { margin-top:6px; color:#475569; max-width:560px; line-height:1.55; }
.student-chips { display:flex; gap:8px; flex-wrap:wrap; margin-top:12px; }
.student-chips span { background:rgba(255,255,255,.88); border:1px solid rgba(99,102,241,.10); border-radius:999px; padding:6px 10px; font-weight:700; color:#475569; }
.student-art { width:48%; min-width:430px; }
.student-art svg { width:100%; height:auto; display:block; }
@media (max-width: 900px) { .student-hero { flex-direction:column; align-items:stretch; } .student-art { width:100%; min-width:0; } }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="study-banner">
    <div class="edu-icons">📚 ✏️ 🧠 💡 📝 🌟</div>
    <div class="title">Belajar Bahasa Indonesia Jadi Lebih Seru! 🎉</div>
    <div class="subtitle">Khusus untuk kamu yang sedang belajar di kelas IX SMP — baca, pahami, latihan, lalu lihat perkembanganmu.</div>
</div>
""", unsafe_allow_html=True)

# Ilustrasi siswa SMP bergaya kartun, dibuat langsung sebagai SVG agar tidak
# membutuhkan file gambar eksternal.
st.markdown(r"""
<div class="student-hero">
  <div class="student-copy">
    <div class="mini-badge">🎓 KELAS IX SMP</div>
    <div class="student-title">Yuk, belajar bareng! 👋</div>
    <div class="student-text">Temani dua sahabat belajar memahami teks deskripsi, mengerjakan latihan, dan meningkatkan nilai.</div>
    <div class="student-chips"><span>📖 Baca</span><span>💡 Pahami</span><span>🏆 Latihan</span></div>
  </div>
  <div class="student-art">
    <svg viewBox="0 0 560 230" role="img" aria-label="Ilustrasi dua siswa SMP sedang belajar">
      <ellipse cx="280" cy="208" rx="250" ry="18" fill="#dbeafe"/>
      <rect x="210" y="155" width="140" height="42" rx="10" fill="#ffffff" stroke="#c7d2fe" stroke-width="3"/>
      <rect x="228" y="165" width="104" height="5" rx="3" fill="#a5b4fc"/>
      <rect x="240" y="178" width="80" height="5" rx="3" fill="#c4b5fd"/>
      <g transform="translate(75,20)">
        <circle cx="75" cy="55" r="34" fill="#f6c7a8"/>
        <path d="M43 52 Q48 15 78 18 Q108 18 109 55 Q96 37 80 38 Q60 38 43 52" fill="#4b3b34"/>
        <circle cx="63" cy="58" r="4" fill="#334155"/><circle cx="87" cy="58" r="4" fill="#334155"/>
        <path d="M67 72 Q75 78 83 72" fill="none" stroke="#9a5b50" stroke-width="3" stroke-linecap="round"/>
        <path d="M42 96 Q75 78 108 96 L119 168 L31 168 Z" fill="#60a5fa"/>
        <path d="M48 168 L42 207 M102 168 L108 207" stroke="#334155" stroke-width="13" stroke-linecap="round"/>
        <path d="M36 207 L55 207 M95 207 L116 207" stroke="#1e3a8a" stroke-width="9" stroke-linecap="round"/>
        <path d="M105 118 Q137 105 151 125" stroke="#f6c7a8" stroke-width="12" fill="none" stroke-linecap="round"/>
      </g>
      <g transform="translate(335,15)">
        <circle cx="75" cy="60" r="34" fill="#e9b58f"/>
        <path d="M42 58 Q44 20 77 17 Q110 22 110 58 Q94 38 78 41 Q58 40 42 58" fill="#252525"/>
        <circle cx="63" cy="62" r="4" fill="#334155"/><circle cx="88" cy="62" r="4" fill="#334155"/>
        <path d="M67 76 Q75 82 83 76" fill="none" stroke="#9a5b50" stroke-width="3" stroke-linecap="round"/>
        <path d="M42 101 Q75 83 108 101 L119 168 L31 168 Z" fill="#f59e0b"/>
        <path d="M48 168 L42 207 M102 168 L108 207" stroke="#334155" stroke-width="13" stroke-linecap="round"/>
        <path d="M36 207 L55 207 M95 207 L116 207" stroke="#92400e" stroke-width="9" stroke-linecap="round"/>
        <path d="M45 119 Q20 107 7 128" stroke="#e9b58f" stroke-width="12" fill="none" stroke-linecap="round"/>
      </g>
      <text x="265" y="145" font-size="30">📚</text>
      <text x="185" y="62" font-size="28">💡</text>
      <text x="380" y="48" font-size="26">⭐</text>
    </svg>
  </div>
</div>
""", unsafe_allow_html=True)


# Musik belajar instrumental ringan (lokal agar aplikasi tetap dapat berjalan offline).
MUSIK_BELAJAR = os.path.join(os.path.dirname(__file__), "musik_belajar_ringan.wav")
if os.path.exists(MUSIK_BELAJAR):
    with open(MUSIK_BELAJAR, "rb") as f:
        audio_b64 = base64.b64encode(f.read()).decode("utf-8")
    st.markdown(
        '<div style="background:rgba(255,255,255,.75);padding:10px 16px;border-radius:16px;border:1px solid rgba(99,102,241,.10);margin-bottom:14px;">'
        '<span style="font-weight:700;color:#4338ca;">🎧 Musik belajar ringan</span>'
        '<audio controls loop style="width:100%;margin-top:6px;">'
        f'<source src="data:audio/wav;base64,{audio_b64}" type="audio/wav">'
        '</audio></div>',
        unsafe_allow_html=True
    )


# =========================================================
# KONFIGURASI DATABASE
# =========================================================

FOLDER_DATABASE = "database"


# =========================================================
# FUNGSI MEMBACA DATABASE TXT
# =========================================================

def baca_database():

    data = []

    if not os.path.exists(FOLDER_DATABASE):
        os.makedirs(FOLDER_DATABASE)

    daftar_file = os.listdir(FOLDER_DATABASE)

    for nama_file in daftar_file:

        if nama_file.lower().endswith(".txt"):

            lokasi_file = os.path.join(
                FOLDER_DATABASE,
                nama_file
            )

            try:

                with open(
                    lokasi_file,
                    "r",
                    encoding="utf-8"
                ) as file:

                    isi = file.read()

                data.append({
                    "nama_file": nama_file,
                    "isi": isi
                })

            except Exception as error:

                st.error(
                    f"Gagal membaca {nama_file}: {error}"
                )

    return data


# =========================================================
# MEMBERSIHKAN TEKS
# =========================================================

def bersihkan_teks(teks):

    teks = teks.lower()

    teks = re.sub(
        r"[^a-zA-ZÀ-ÿ0-9\s]",
        " ",
        teks
    )

    teks = re.sub(
        r"\s+",
        " ",
        teks
    )

    return teks.strip()


# =========================================================
# STOPWORDS SEDERHANA
# =========================================================

STOPWORDS = {
    "yang",
    "dan",
    "di",
    "ke",
    "dari",
    "pada",
    "dengan",
    "untuk",
    "dalam",
    "adalah",
    "itu",
    "ini",
    "atau",
    "apa",
    "bagaimana",
    "mengapa",
    "sebutkan",
    "jelaskan",
    "jelaskanlah",
    "tentang",
    "suatu",
    "sebuah",
    "secara",
    "merupakan",
    "dapat",
    "akan",
    "sebagai",
    "oleh",
    "lebih",
    "juga",
    "tidak",
    "tersebut"
}


# =========================================================
# MENGAMBIL KATA KUNCI
# =========================================================

def ambil_kata_kunci(pertanyaan):

    teks = bersihkan_teks(pertanyaan)

    kata = teks.split()

    kata_kunci = []

    for item in kata:

        if len(item) > 2 and item not in STOPWORDS:

            kata_kunci.append(item)

    return kata_kunci


# =========================================================
# SISTEM PENILAIAN RELEVANSI
# =========================================================

def hitung_relevansi(pertanyaan, isi):

    kata_kunci = ambil_kata_kunci(pertanyaan)

    if len(kata_kunci) == 0:
        return 0

    teks_database = bersihkan_teks(isi)

    kata_database = teks_database.split()

    frekuensi = Counter(kata_database)

    skor = 0

    for kata in kata_kunci:

        if kata in frekuensi:

            jumlah = frekuensi[kata]

            if jumlah > 10:
                jumlah = 10

            skor += jumlah

    # Bonus jika frasa pertanyaan muncul
    pertanyaan_bersih = bersihkan_teks(
        pertanyaan
    )

    if pertanyaan_bersih in teks_database:

        skor += 20

    # Bonus jika kata kunci utama terdapat di judul
    baris_awal = teks_database[:500]

    for kata in kata_kunci:

        if kata in baris_awal:

            skor += 5

    return skor


# =========================================================
# MENCARI MATERI
# =========================================================

def cari_materi(pertanyaan, database):

    hasil = []

    for data in database:

        skor = hitung_relevansi(
            pertanyaan,
            data["isi"]
        )

        if skor > 0:

            hasil.append({
                "nama_file": data["nama_file"],
                "isi": data["isi"],
                "skor": skor
            })

    hasil.sort(
        key=lambda x: x["skor"],
        reverse=True
    )

    return hasil


# =========================================================
# MEMBUAT POTONGAN MATERI
# =========================================================

def ambil_potongan_relevan(
    pertanyaan,
    isi,
    jumlah_maksimal=1200
):

    kata_kunci = ambil_kata_kunci(
        pertanyaan
    )

    paragraf = re.split(
        r"\n\s*\n|\r\n",
        isi
    )

    paragraf_relevan = []

    for p in paragraf:

        p_bersih = bersihkan_teks(p)

        skor = 0

        for kata in kata_kunci:

            if kata in p_bersih:

                skor += 1

        if skor > 0:

            paragraf_relevan.append(
                (skor, p.strip())
            )

    paragraf_relevan.sort(
        key=lambda x: x[0],
        reverse=True
    )

    hasil = ""

    for skor, p in paragraf_relevan:

        if len(hasil) + len(p) <= jumlah_maksimal:

            hasil += p + "\n\n"

    if hasil.strip() == "":

        hasil = isi[:jumlah_maksimal]

    return hasil.strip()


# =========================================================
# LOAD DATABASE
# =========================================================

database = baca_database()

# Menyimpan riwayat nilai selama aplikasi berjalan
st.session_state.setdefault("riwayat_nilai", [])


# =========================================================
# HEADER APLIKASI
# =========================================================

st.title("📚 Bahasa Indonesia Kelas IX")
st.write(
    "Teman belajar Bahasa Indonesia untuk kelas IX SMP — cari materi, pelajari konsep, dan uji pemahamanmu."
)

st.divider()


# =========================================================
# SIDEBAR / MENU
# =========================================================

with st.sidebar:

    st.header("🎒 Menu Belajar")

    menu = st.radio(
        "Pilih Menu",
        [
            "📖 Tentang",
            "📚 Daftar Materi",
            "🔎 Cari Materi",
            "📖 Belajar Materi",
            "📝 Latihan Soal",
            "🏆 Nilai"
        ]
    )

    st.divider()

    st.subheader("🗂️ Knowledge Base")
    st.write("Database dibaca otomatis dari folder:")
    st.code("database/")
    st.write(f"Jumlah file database: **{len(database)}**")


# =========================================================
# BANK SOAL - MATERI TEKS DESKRIPSI
# =========================================================
# Soal berikut dibuat berdasarkan materi "Teks Deskripsi"
# yang kamu masukkan.

SOAL = [
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Apa yang dimaksud dengan teks deskripsi?",
        "pilihan": [
            "Teks yang menceritakan rangkaian peristiwa",
            "Teks yang menggambarkan suatu objek secara terperinci",
            "Teks yang memberikan langkah-langkah melakukan sesuatu",
            "Teks yang mengajak pembaca melakukan sesuatu"
        ],
        "jawaban": "Teks yang menggambarkan suatu objek secara terperinci",
        "pembahasan": (
            "Teks deskripsi menggambarkan suatu objek secara terperinci "
            "sehingga pembaca memperoleh gambaran yang jelas tentang objek tersebut."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Apa tujuan utama teks deskripsi?",
        "pilihan": [
            "Memberikan gambaran yang jelas dan terperinci mengenai suatu objek",
            "Memberikan langkah-langkah melakukan sesuatu",
            "Menceritakan konflik antartokoh",
            "Membujuk pembaca agar mengikuti pendapat penulis"
        ],
        "jawaban": "Memberikan gambaran yang jelas dan terperinci mengenai suatu objek",
        "pembahasan": (
            "Tujuan utama teks deskripsi adalah memberikan gambaran yang jelas "
            "dan terperinci agar pembaca dapat membayangkan objek yang dijelaskan."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Berikut yang termasuk objek yang dapat dideskripsikan adalah ...",
        "pilihan": [
            "Manusia, hewan, tumbuhan, benda, tempat, dan peristiwa",
            "Hanya manusia dan hewan",
            "Hanya tempat dan peristiwa",
            "Hanya benda dan tumbuhan"
        ],
        "jawaban": "Manusia, hewan, tumbuhan, benda, tempat, dan peristiwa",
        "pembahasan": (
            "Materi menyebutkan manusia, hewan, tumbuhan, benda, tempat dan "
            "lingkungan, serta peristiwa sebagai objek yang dapat dideskripsikan."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Salah satu ciri teks deskripsi adalah ...",
        "pilihan": [
            "Melibatkan pancaindra",
            "Selalu menggunakan kalimat perintah",
            "Selalu menceritakan tokoh dan alur",
            "Berisi langkah-langkah secara berurutan"
        ],
        "jawaban": "Melibatkan pancaindra",
        "pembahasan": (
            "Teks deskripsi melibatkan pancaindra, yaitu penglihatan, "
            "pendengaran, penciuman, perabaan, dan pengecapan."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Struktur teks deskripsi yang berisi pengenalan objek secara umum disebut ...",
        "pilihan": [
            "Deskripsi bagian",
            "Penutup",
            "Deskripsi umum atau identifikasi",
            "Kesimpulan"
        ],
        "jawaban": "Deskripsi umum atau identifikasi",
        "pembahasan": (
            "Deskripsi umum atau identifikasi merupakan bagian yang "
            "memperkenalkan objek secara umum, seperti nama atau lokasi."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Bagian struktur teks deskripsi yang menggambarkan bagian-bagian objek secara terperinci disebut ...",
        "pilihan": [
            "Deskripsi umum",
            "Deskripsi bagian",
            "Orientasi",
            "Penutup"
        ],
        "jawaban": "Deskripsi bagian",
        "pembahasan": (
            "Deskripsi bagian berisi penggambaran terperinci mengenai "
            "bagian-bagian objek, seperti bentuk, warna, ukuran, sifat, dan suasana."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Kata seperti 'kemerahan', 'mungil', 'rimbun', dan 'sejuk' termasuk ...",
        "pilihan": [
            "Kata sifat",
            "Kata rujukan",
            "Kata hubung",
            "Kata kerja"
        ],
        "jawaban": "Kata sifat",
        "pembahasan": (
            "Kata-kata tersebut menjelaskan warna, ukuran, keadaan, atau "
            "suasana sehingga termasuk kata sifat atau adjektiva."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Manakah penulisan kata baku yang tepat?",
        "pilihan": [
            "Aktifitas",
            "Resiko",
            "Obyek",
            "Aktivitas"
        ],
        "jawaban": "Aktivitas",
        "pembahasan": (
            "Bentuk baku yang terdapat dalam materi adalah aktivitas, "
            "sedangkan aktifitas merupakan bentuk yang tidak baku."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Kata 'di pantai' ditulis terpisah karena 'di' berfungsi sebagai ...",
        "pilihan": [
            "Imbuhan",
            "Kata depan yang menunjukkan tempat",
            "Kata kerja",
            "Kata sifat"
        ],
        "jawaban": "Kata depan yang menunjukkan tempat",
        "pembahasan": (
            "Kata depan di ditulis terpisah jika menunjukkan tempat, "
            "misalnya di pantai, di hutan, dan di rumah."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Kalimat 'Air terjun itu bagaikan tirai putih raksasa' menggunakan majas ...",
        "pilihan": [
            "Metafora",
            "Personifikasi",
            "Hiperbola",
            "Perumpamaan atau simile"
        ],
        "jawaban": "Perumpamaan atau simile",
        "pembahasan": (
            "Kalimat tersebut menggunakan kata 'bagaikan' untuk membandingkan "
            "air terjun dengan tirai putih raksasa sehingga termasuk perumpamaan."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Teks deskripsi yang menggambarkan objek berdasarkan keadaan sebenarnya tanpa terlalu memasukkan kesan pribadi disebut ...",
        "pilihan": [
            "Deskripsi subjektif",
            "Deskripsi objektif",
            "Deskripsi spasial",
            "Deskripsi impresionistis"
        ],
        "jawaban": "Deskripsi objektif",
        "pembahasan": (
            "Deskripsi objektif menggambarkan objek berdasarkan fakta hasil "
            "pengamatan secara jelas dan apa adanya."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Deskripsi subjektif dipengaruhi oleh ...",
        "pilihan": [
            "Pengalaman dan sudut pandang penulis",
            "Urutan langkah kerja",
            "Data statistik saja",
            "Pendapat pembaca"
        ],
        "jawaban": "Pengalaman dan sudut pandang penulis",
        "pembahasan": (
            "Deskripsi subjektif berdasarkan penafsiran, kesan, pandangan, "
            "atau perasaan penulis."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Pola pengembangan yang disusun menurut letak, seperti depan ke belakang atau luar ke dalam, disebut pola ...",
        "pilihan": [
            "Waktu",
            "Kesan",
            "Spasial",
            "Khusus ke umum"
        ],
        "jawaban": "Spasial",
        "pembahasan": (
            "Pola spasial disusun berdasarkan ruang atau letak, misalnya "
            "depan ke belakang, atas ke bawah, atau luar ke dalam."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Langkah pertama dalam membuat teks deskripsi adalah ...",
        "pilihan": [
            "Menyunting teks",
            "Menentukan tema atau topik",
            "Mengembangkan kerangka",
            "Menetapkan pola pengembangan"
        ],
        "jawaban": "Menentukan tema atau topik",
        "pembahasan": (
            "Langkah pertama adalah menentukan tema atau topik yang menjadi "
            "dasar penggambaran."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Dalam menulis teks deskripsi, kata 'bagus' atau 'indah' sebaiknya ...",
        "pilihan": [
            "Digunakan sebanyak mungkin",
            "Diganti dengan kata yang lebih spesifik dan disertai penjelasan",
            "Dihilangkan semua",
            "Diganti dengan kata asing"
        ],
        "jawaban": "Diganti dengan kata yang lebih spesifik dan disertai penjelasan",
        "pembahasan": (
            "Materi menyarankan penggunaan kata yang spesifik, bukan kata umum "
            "seperti bagus atau indah tanpa penjelasan."
        )
    },
    {
        "materi": "Teks Deskripsi",
        "pertanyaan": "Teks yang menggambarkan ruang atau tempat dari berbagai sisi disebut ...",
        "pilihan": [
            "Deskripsi spasial",
            "Deskripsi objektif",
            "Deskripsi subjektif",
            "Narasi"
        ],
        "jawaban": "Deskripsi spasial",
        "pembahasan": (
            "Deskripsi spasial menggambarkan ruang atau tempat berdasarkan "
            "letak dan posisi bagian-bagiannya."
        )
    }
]

# =========================================================
# BANK SOAL ESAI - MATERI TEKS DESKRIPSI
# =========================================================
SOAL_ESAI = [
    {"nomor": 1, "pertanyaan": "Jelaskan pengertian teks deskripsi dengan menggunakan bahasa Anda sendiri!"},
    {"nomor": 2, "pertanyaan": "Sebutkan dan jelaskan minimal empat ciri-ciri teks deskripsi!"},
    {"nomor": 3, "pertanyaan": "Jelaskan perbedaan antara teks deskripsi spasial, objektif, dan subjektif!"},
    {"nomor": 4, "pertanyaan": "Jelaskan secara berurutan langkah-langkah yang harus dilakukan dalam membuat teks deskripsi!"},
    {"nomor": 5, "pertanyaan": "Buatlah sebuah teks deskripsi singkat mengenai salah satu objek yang ada di lingkungan sekolah, rumah, atau tempat tinggal Anda. Gunakan penggambaran yang jelas dan terperinci!"}
]


# =========================================================
# MENU TENTANG
# =========================================================

if menu == "📖 Tentang":

    st.header("📖 Tentang Bahasa Indonesia Kelas IX")

    st.write(
        """
        Bahasa Indonesia Kelas IX merupakan aplikasi pembelajaran
        yang membantu pengguna mencari dan mempelajari materi
        Bahasa Indonesia.

        Aplikasi ini menggunakan Python dan Streamlit serta
        mengambil materi dari Knowledge Base berupa file TXT.
        """
    )

    st.info(
        "Gunakan menu **Latihan Soal** untuk mengerjakan soal "
        "interaktif dan melihat nilai secara otomatis."
    )


# =========================================================
# MENU DAFTAR MATERI
# =========================================================

elif menu == "📚 Daftar Materi":

    st.header("📚 Daftar Materi")
    st.caption("Pilih materi yang ingin kamu jelajahi. Semangat belajar! 🌟")

    if len(database) == 0:

        st.warning("Belum ada file TXT di folder database.")

    else:

        st.write("Materi yang tersedia dalam Knowledge Base:")

        for nomor, data in enumerate(database, 1):

            nama = data["nama_file"]
            nama = nama.replace(".txt", "")
            nama = nama.replace("_", " ")

            st.write(f"**{nomor}. 📄 {nama.title()}**")


# =========================================================
# MENU CARI MATERI
# =========================================================

elif menu == "🔎 Cari Materi":

    st.header("🔎 Cari Materi")
    st.caption("Tanyakan materi dengan kata kunci yang kamu pahami. 💡")

    pertanyaan = st.text_area(
        "Masukkan pertanyaan Anda:",
        placeholder=(
            "Contoh: Apa yang dimaksud dengan kalimat efektif?"
        ),
        height=120
    )

    tombol = st.button(
        "🔍 TANYAKAN",
        use_container_width=True
    )

    if tombol:

        if pertanyaan.strip() == "":

            st.warning(
                "Silakan masukkan pertanyaan terlebih dahulu."
            )

        elif len(database) == 0:

            st.error(
                "Database TXT belum ditemukan."
            )

        else:

            with st.spinner(
                "Sedang mencari materi..."
            ):

                hasil = cari_materi(
                    pertanyaan,
                    database
                )

            if len(hasil) > 0:

                hasil_utama = hasil[0]

                st.success(
                    "Materi yang paling relevan ditemukan."
                )

                st.subheader("💡 Jawaban")

                jawaban = ambil_potongan_relevan(
                    pertanyaan,
                    hasil_utama["isi"]
                )

                st.info(jawaban)

                st.subheader("📚 Sumber Materi")

                st.write(
                    f"**{hasil_utama['nama_file']}**"
                )

                if len(hasil) > 1:

                    st.subheader("📑 Materi Terkait")

                    for item in hasil[1:4]:

                        with st.expander(
                            item["nama_file"]
                        ):

                            potongan = ambil_potongan_relevan(
                                pertanyaan,
                                item["isi"],
                                800
                            )

                            st.write(potongan)

            else:

                st.warning(
                    "Maaf, materi yang Anda tanyakan "
                    "belum ditemukan dalam database."
                )

                st.write(
                    "Coba gunakan kata kunci yang lebih spesifik."
                )


# =========================================================
# MENU BELAJAR MATERI
# =========================================================

elif menu == "📖 Belajar Materi":

    st.header("📖 Belajar Materi")
    st.caption("Baca perlahan, tandai ide penting, dan pahami contohnya. ✏️")

    if len(database) == 0:

        st.warning(
            "Belum ada materi. Masukkan file TXT ke folder database."
        )

    else:

        pilihan_file = st.selectbox(
            "Pilih materi yang ingin dipelajari:",
            [
                data["nama_file"]
                for data in database
            ]
        )

        data_terpilih = next(
            (
                data
                for data in database
                if data["nama_file"] == pilihan_file
            ),
            None
        )

        if data_terpilih:

            st.subheader(
                pilihan_file.replace(".txt", "").replace("_", " ").title()
            )

            st.write(data_terpilih["isi"])


# =========================================================
# MENU LATIHAN SOAL INTERAKTIF
# =========================================================

elif menu == "📝 Latihan Soal":

    st.header("📝 Latihan Soal Interaktif")
    st.caption("Uji pemahamanmu dan jadikan hasilnya sebagai bahan belajar berikutnya. 🚀")

    jenis_latihan = st.radio(
        "Pilih jenis soal:",
        ["A. Pilihan Berganda", "B. Esai"],
        horizontal=True
    )

    # =====================================================
    # PILIHAN BERGANDA
    # =====================================================

    if jenis_latihan == "A. Pilihan Berganda":

        st.write("Pilihlah jawaban yang paling tepat!")

        daftar_materi_soal = sorted(
            set(soal["materi"] for soal in SOAL)
        )

        materi_dipilih = st.selectbox(
            "📚 Pilih materi:",
            ["Semua Materi"] + daftar_materi_soal
        )

        if materi_dipilih == "Semua Materi":

            soal_aktif = SOAL

        else:

            soal_aktif = [
                soal
                for soal in SOAL
                if soal["materi"] == materi_dipilih
            ]

        jumlah_maksimal = len(soal_aktif)

        jumlah_soal = st.slider(
            "🔢 Jumlah soal:",
            min_value=1,
            max_value=jumlah_maksimal,
            value=min(5, jumlah_maksimal)
        )

        soal_aktif = soal_aktif[:jumlah_soal]

        st.divider()

        jawaban_pengguna = {}

        for nomor, soal in enumerate(soal_aktif, 1):

            st.markdown(f"### Soal {nomor}")

            st.write(soal["pertanyaan"])

            jawaban_pengguna[nomor] = st.radio(
                "Pilih jawaban:",
                soal["pilihan"],
                key=f"jawaban_{materi_dipilih}_{nomor}"
            )

        st.divider()

        if st.button(
            "✅ PERIKSA JAWABAN",
            use_container_width=True
        ):

            skor = 0

            st.subheader("📊 Hasil Latihan")

            for nomor, soal in enumerate(soal_aktif, 1):

                jawaban = jawaban_pengguna[nomor]

                if jawaban == soal["jawaban"]:

                    skor += 1

                    st.success(
                        f"Soal {nomor}: ✅ Benar"
                    )

                else:

                    st.error(
                        f"Soal {nomor}: ❌ Salah"
                    )

                    st.write(
                        f"Jawaban yang benar: **{soal['jawaban']}**"
                    )

                with st.expander(
                    f"💡 Pembahasan soal {nomor}"
                ):

                    st.write(
                        soal["pembahasan"]
                    )

            nilai = round(
                (skor / len(soal_aktif)) * 100
            )

            st.session_state["riwayat_nilai"].append({
                "jenis": "Pilihan Berganda",
                "nilai": nilai,
                "benar": skor,
                "jumlah": len(soal_aktif)
            })

            st.divider()

            st.metric(
                "🎯 Nilai Anda",
                f"{nilai}"
            )

            st.write(
                f"Jawaban benar: **{skor} dari {len(soal_aktif)} soal**"
            )

            if nilai >= 80:

                st.success(
                    "🎉 Sangat baik! Kamu sudah memahami materi."
                )

                st.balloons()

            elif nilai >= 60:

                st.warning(
                    "👍 Cukup baik. Pelajari kembali materi yang masih kurang."
                )

            else:

                st.error(
                    "📚 Jangan menyerah. Pelajari materi kembali dan coba lagi."
                )

    # =====================================================
    # ESAI
    # =====================================================

    else:

        st.subheader("B. ESAI")
        st.write("Jawablah pertanyaan berikut dengan jelas dan lengkap!")

        jawaban_esai = {}

        for soal in SOAL_ESAI:
            st.markdown(f"### {soal['nomor']}. {soal['pertanyaan']}")
            jawaban_esai[soal["nomor"]] = st.text_area(
                f"Jawaban soal {soal['nomor']}:",
                height=140,
                key=f"esai_{soal['nomor']}",
                placeholder="Tuliskan jawaban Anda di sini..."
            )

        st.divider()

        if st.button("💾 SIMPAN JAWABAN ESAI", use_container_width=True):
            jumlah_terisi = sum(
                1 for jawaban in jawaban_esai.values()
                if jawaban.strip()
            )
            if jumlah_terisi == 0:
                st.warning("Silakan isi jawaban terlebih dahulu.")
            else:
                st.success(
                    f"Jawaban berhasil dicatat. "
                    f"{jumlah_terisi} dari {len(SOAL_ESAI)} soal telah diisi."
                )
                st.info(
                    "Jawaban esai belum diberi nilai otomatis. "
                    "Penilaian dapat dilakukan oleh guru."
                )


# =========================================================
# MENU NILAI
# =========================================================

elif menu == "🏆 Nilai":

    st.header("🏆 Nilai Saya")
    st.write("Lihat hasil latihan pilihan berganda yang sudah kamu kerjakan.")

    riwayat = st.session_state.get("riwayat_nilai", [])

    if len(riwayat) == 0:
        st.info("Belum ada nilai. Yuk kerjakan Latihan Soal terlebih dahulu! 📝")
    else:
        nilai_terakhir = riwayat[-1]
        st.metric("🎯 Nilai Terakhir", nilai_terakhir["nilai"])

        st.write(
            f"Jawaban benar: **{nilai_terakhir['benar']} dari "
            f"{nilai_terakhir['jumlah']} soal**"
        )

        if nilai_terakhir["nilai"] >= 80:
            st.success("🎉 Hebat! Hasil belajarmu sangat baik.")
        elif nilai_terakhir["nilai"] >= 60:
            st.warning("👍 Cukup baik. Yuk belajar lagi agar nilainya lebih tinggi.")
        else:
            st.error("💪 Jangan menyerah. Pelajari kembali materinya dan coba lagi!")

        st.subheader("📊 Riwayat Nilai")

        for nomor, hasil in enumerate(reversed(riwayat), 1):
            st.write(
                f"**Latihan {len(riwayat) - nomor + 1}** — "
                f"{hasil['jenis']} — **{hasil['nilai']}** "
                f"({hasil['benar']}/{hasil['jumlah']} benar)"
            )

        if st.button("🗑️ Hapus Riwayat Nilai"):
            st.session_state["riwayat_nilai"] = []
            st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Bahasa Indonesia Kelas IX | "
    "Python + Streamlit + TXT Knowledge Base"
)
