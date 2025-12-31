# TUBES-STRUKDAT

## Deskripsi
Program ini adalah aplikasi katalog musik berbasis CLI (C++), menggunakan struktur data Multi Linked List (MLL) untuk mengelola data artis dan lagu. Data dapat dimuat dan disimpan dari/ke file CSV.

## Fitur Utama
- Tambah artis baru beserta data genre dan tahun debut
- Tambah lagu ke artis tertentu
- Tampilkan seluruh data artis dan lagu
- Hapus lagu dari artis
- Hapus artis beserta seluruh lagunya (delete cascade)
- Cari artis berdasarkan nama
- Laporan: total lagu & artis paling produktif
- Load & save data ke file CSV (otomatis saat start/opsional saat keluar)

## Struktur Data
- **Artis (Parent):**
	- Nama
	- Genre
	- Tahun Debut
	- List Lagu (Child)
- **Lagu (Child):**
	- Judul Lagu

Struktur Data MLL (Multi Linked List) 1-N:

| Komponen         | Tipe                    | Atribut                                                                 |
|------------------|-------------------------|-------------------------------------------------------------------------|
| **PARENT (Artis)** | Record (Class/Object)   | `nama_artis` (String), `genre` (String), `tahun_debut` (Integer), Pointer ke Child |
| **CHILD (Lagu)**  | Tipe Dasar (String)     | Judul lagu saja (contoh: "Hati-Hati di Jalan", "Monokrom", "Dan")         |

Implementasi menggunakan pointer dan struct (lihat `katalog.h`).
# TUBES-STRUKDAT

## Deskripsi
Program ini adalah aplikasi katalog musik berbasis CLI (C++), menggunakan struktur data Multi Linked List (MLL) untuk mengelola data artis dan lagu. Data dapat dimuat dan disimpan dari/ke file CSV.

## Fitur Utama
- Tambah artis baru beserta data genre dan tahun debut
- Tambah lagu ke artis tertentu
- Tampilkan seluruh data artis dan lagu
- Hapus lagu dari artis
- Hapus artis beserta seluruh lagunya (delete cascade)
- Cari artis berdasarkan nama
- Laporan: total lagu & artis paling produktif
- Load & save data ke file CSV (otomatis saat start/opsional saat keluar)

## Struktur Data
- **Artis (Parent):**
	- Nama
	- Genre
	- Tahun Debut
	- List Lagu (Child)
- **Lagu (Child):**
	- Judul Lagu

Implementasi menggunakan pointer dan struct (lihat `katalog.h`).

## Format File CSV
Setiap baris: `NamaArtis;Genre;TahunDebut;JudulLagu`
Contoh:
```
Tulus;Pop;2011;Hati-Hati di Jalan
Sheila on 7;Pop Rock;1996;Dan
```

## Cara Build & Jalankan
1. Pastikan sudah terinstall g++ (MinGW/WSL/Linux/macOS)
2. Compile:
	 ```sh
	 g++ -o program_new main.cpp katalog.cpp -std=c++17
	 ```
3. Jalankan:
	 ```sh
	 ./program_new
	 ```
	 atau di Windows:
	 ```sh
	 program_new.exe
	 ```

## Contoh Penggunaan
```
=== APLIKASI KATALOG MUSIK ===
1. Tambah Artis Baru
2. Tambah Lagu ke Artis
3. Tampilkan Semua Data
4. Hapus Lagu
5. Hapus Artis (Beserta Lagunya)
6. Cari Artis
7. Laporan (Total & Artis Terproduktif)
0. Keluar
```

## Struktur File
- `main.cpp` : Program utama & menu
- `katalog.h` : Definisi struct & prototype fungsi
- `katalog.cpp` : Implementasi fungsi & pengolahan data
- `music_db..csv` : Data dummy artis & lagu

## Kontributor
- @hanif-12-01

---
Tugas Besar Struktur Data 2025