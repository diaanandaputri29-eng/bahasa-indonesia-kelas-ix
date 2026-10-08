# 📚 Bahasa Indonesia Kelas IX

Aplikasi pembelajaran Bahasa Indonesia untuk siswa Kelas IX berbasis **Python + Streamlit + Knowledge Base TXT**.

## ✨ Fitur

- 📖 Tentang aplikasi
- 📚 Daftar materi
- 🔎 Pencarian materi dari Knowledge Base TXT
- 📖 Belajar materi
- 📝 Latihan pilihan berganda dan esai
- 🏆 Riwayat nilai
- ✨ Tampilan animasi dan interaktif

## 📁 Struktur folder

```text
bahasa-indonesia-kelas-ix/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── database/
    ├── README.txt
    └── *.txt
```

## ▶️ Menjalankan di komputer

Pastikan Python sudah terpasang, lalu buka Terminal/CMD di folder aplikasi.

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📚 Menambahkan materi

Masukkan materi Bahasa Indonesia dalam format `.txt` ke folder `database/`.
Aplikasi akan membacanya secara otomatis.

## ☁️ Deploy ke Streamlit Community Cloud

1. Upload seluruh isi folder ini ke repository GitHub.
2. Buka Streamlit Community Cloud.
3. Hubungkan akun GitHub.
4. Pilih repository ini.
5. Pilih file utama `app.py`.
6. Klik **Deploy**.

Setelah berhasil, Streamlit akan memberikan alamat web yang dapat dibagikan kepada siswa dan guru.

## 👨‍🏫 Catatan

Aplikasi ini menggunakan pencarian berbasis kata kunci pada file TXT. Penilaian otomatis tersedia untuk soal pilihan berganda, sedangkan esai dapat diperiksa oleh guru.
