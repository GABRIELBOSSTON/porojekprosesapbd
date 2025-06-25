# Proyek APBD Bekasi

Ini adalah proyek aplikasi web berbasis Django yang didesain untuk menyediakan informasi transparan mengenai Anggaran Pendapatan dan Belanja Daerah (APBD) Kota Bekasi. Aplikasi ini bertujuan untuk memudahkan masyarakat dalam mengakses data anggaran, berita terkini, dan dokumen terkait APBD.

---

## Tampilan Aplikasi

Berikut adalah beberapa tampilan antarmuka pengguna (UI) dari aplikasi APBD Bekasi:

### Halaman Beranda
Menampilkan ringkasan dan navigasi utama aplikasi.
![Halaman Beranda Proyek APBD](screenshots/Screenshot 2025-06-15 173304.png)

### Tampilan Detail Data
Contoh tampilan halaman yang menyajikan detail data APBD.
![Tampilan Data APBD](screenshots/Screenshot 2025-06-15 173323.png)

### Halaman Tanya Jawab Umum (FAQ)
Berisi daftar pertanyaan dan jawaban umum seputar APBD Bekasi.
![Halaman Pertanyaan Umum](screenshots/Screenshot 2025-06-08 063158.png)

### Halaman Unduh Dokumen
Tempat pengguna dapat mengunduh dokumen-dokumen penting terkait anggaran.
![Halaman Unduh Dokumen](screenshots/Screenshot 2025-05-30 033527.png)

---

## Fitur Utama

* **Dashboard Interaktif:** Menampilkan ringkasan APBD tahunan dan perbandingan data.
* **Informasi Berita:** Bagian khusus untuk berita atau pengumuman terkait anggaran.
* **Unduh Dokumen:** Memungkinkan pengguna untuk mengunduh laporan atau dokumen resmi APBD dalam format PDF.
* **FAQ:** Bagian tanya jawab untuk membantu pengguna memahami informasi lebih lanjut.
* **Responsif:** Tampilan yang adaptif di berbagai perangkat (desktop, tablet, mobile).

---

## Cara Menjalankan Proyek (Lokal)

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek APBD Bekasi di lingkungan lokal Anda:

1.  **Clone repositori:**
    Buka Terminal atau Command Prompt dan jalankan perintah berikut:
    ```bash
    git clone [https://github.com/GABRIELBOSSTON/porojekprosesapbd.git](https://github.com/GABRIELBOSSTON/porojekprosesapbd.git)
    ```

2.  **Masuk ke direktori proyek:**
    ```bash
    cd porojekprosesapbd
    ```

3.  **Buat dan aktifkan virtual environment:**
    Sangat disarankan untuk menggunakan virtual environment untuk mengelola dependensi proyek.
    * **Untuk Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **Untuk macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Instal dependensi:**
    Setelah virtual environment aktif, instal semua pustaka Python yang diperlukan:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Lakukan migrasi database:**
    Terapkan skema database Django:
    ```bash
    python manage.py migrate
    ```

6.  **Jalankan server pengembangan:**
    ```bash
    python manage.py runserver
    ```

7.  **Akses aplikasi:**
    Buka browser web Anda dan kunjungi alamat berikut:
    `http://127.0.0.1:8000/`

---

## Kontribusi

Kami menerima kontribusi dari siapa saja yang ingin membantu meningkatkan proyek ini. Silakan buka *issue* atau buat *pull request*.

---

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT.