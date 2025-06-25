
# Proyek APBD Bekasi

Ini adalah proyek aplikasi web untuk menampilkan data Anggaran Pendapatan dan Belanja Daerah (APBD) Kota Bekasi.

## Tampilan Aplikasi

Berikut adalah beberapa tampilan antarmuka pengguna (UI) dari aplikasi ini:

### Halaman Beranda
![Halaman Beranda](screenshots/Screenshot 2025-06-15 173304.png)

### Tampilan Data
![Tampilan Data APBD](screenshots/Screenshot 2025-06-15 173323.png)

### Halaman FAQ
![Halaman Pertanyaan Umum](screenshots/Screenshot 2025-06-08 063158.png)

### Halaman Unduh Dokumen
![Halaman Unduh Dokumen](screenshots/Screenshot 2025-05-30 033527.png)

---

## Fitur Utama

* Menampilkan ringkasan APBD tahunan.
* Menyediakan informasi detail mengenai pos-pos anggaran.
* Halaman FAQ untuk pertanyaan umum.
* Fitur unduh dokumen terkait APBD.

## Cara Menjalankan Proyek (Lokal)

1.  Clone repositori ini:
    `git clone https://github.com/GABRIELBOSSTON/porojekprosesapbd.git`
2.  Masuk ke direktori proyek:
    `cd porojekprosesapbd`
3.  Buat dan aktifkan virtual environment:
    * Windows: `python -m venv venv` lalu `.\venv\Scripts\activate`
    * macOS/Linux: `python3 -m venv venv` lalu `source venv/bin/activate`
4.  Instal dependensi:
    `pip install -r requirements.txt`
5.  Lakukan migrasi database:
    `python manage.py migrate`
6.  Jalankan server:
    `python manage.py runserver`
7.  Buka browser Anda dan kunjungi `http://127.0.0.1:8000/`
