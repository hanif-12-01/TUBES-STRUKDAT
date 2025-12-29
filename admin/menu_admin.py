import os
import time
from database.data_store import (
    artists_list,
    add_artist, get_artist, delete_artist, search_artist,
    add_song_to_artist, delete_song_from_artist,
    count_total_songs, get_artist_with_most_songs, get_all_artists_sorted_by_songs
)
from admin.coming_soon import show_coming_soon, show_under_development, show_feature_roadmap

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    width = 70
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()

def pause():
    input("\n[Tekan Enter untuk kembali ke menu...]")


def katalog_add_artist():
  
    print("\n--- TAMBAH ARTIS BARU ---\n")
    
    nama = input("Nama Artis: ").strip()
    if not nama:
        print("Nama artis tidak boleh kosong!")
        return
    
    if get_artist(nama):
        print(f"Artis '{nama}' sudah ada di database!")
        return
    
    genre = input("Genre: ").strip()
    if not genre:
        print("Genre tidak boleh kosong!")
        return
    
    try:
        tahun_debut = int(input("Tahun Debut: "))
    except ValueError:
        print("Tahun debut harus berupa angka!")
        return
    
    if add_artist(nama, genre, tahun_debut):
        print(f"\n✓ Artis '{nama}' berhasil ditambahkan!")
        print(f"  Genre: {genre}")
        print(f"  Tahun Debut: {tahun_debut}")
    else:
        print("Gagal menambahkan artis!")




def katalog_add_song():

    print("\n--- TAMBAH LAGU KE ARTIS ---\n")
    
    if not artists_list:
        print("Belum ada artis di database! Tambahkan artis terlebih dahulu.")
        return
    
    print("Daftar Artis:")
    for i, artist in enumerate(artists_list, 1):
        print(f"  {i}. {artist.nama_artis} ({artist.genre}) - {artist.song_count()} lagu")
    
    nama_artis = input("\nNama Artis: ").strip()
    artist = get_artist(nama_artis)
    
    if not artist:
        print(f"Artis '{nama_artis}' tidak ditemukan!")
        return
    
    judul_lagu = input("Judul Lagu: ").strip()
    if not judul_lagu:
        print("Judul lagu tidak boleh kosong!")
        return
    
    if add_song_to_artist(nama_artis, judul_lagu):
        print(f"\n✓ Lagu '{judul_lagu}' berhasil ditambahkan ke artis '{artist.nama_artis}'!")
        print(f"  Total lagu {artist.nama_artis}: {artist.song_count()}")
    else:
        print(f"Gagal menambahkan lagu! (Mungkin lagu sudah ada)")


def katalog_view_all():
    from database.data_store import get_all_artists
    print("\n--- KATALOG ALBUM MUSIK LENGKAP ---\n")
    artists = get_all_artists()
    if not artists:
        print("(Katalog masih kosong)")
        return
    for i, artist in enumerate(artists, 1):
        print(f"{i}. {artist.nama_artis}")
        print(f"   Genre      : {artist.genre}")
        print(f"   Tahun Debut: {artist.tahun_debut}")
        print(f"   Jumlah Lagu: {artist.song_count()}")
        if artist.songs:
            print(f"   Daftar Lagu:")
            for j, judul_lagu in enumerate(artist.songs, 1):
                print(f"      {j}. {judul_lagu}")
        else:
            print(f"   (Belum ada lagu)")
        print()


def katalog_delete_song():

    show_under_development(
        feature_name="HAPUS LAGU",
        current_status="Implementasi dasar sudah berjalan, sedang perbaikan validasi",
        todo_items=[
            "Perbaikan validasi input",
            "Konfirmasi penghapusan yang lebih baik",
            "Handle edge cases",
            "Testing dengan berbagai skenario"
        ],
        progress=70
    )
    
    print("  🔄 Fitur ini tetap dapat digunakan, namun mungkin ada kekurangan.\n")
    
    lanjut = input("  Lanjutkan menggunakan fitur ini? (y/n): ").lower()
    if lanjut != 'y':
        return
    
    print("\n--- HAPUS LAGU ---\n")
    
    if not artists_list:
        print("Belum ada artis di database!")
        return
    
    print("Daftar Artis:")
    for i, artist in enumerate(artists_list, 1):
        print(f"  {i}. {artist.nama_artis} - {artist.song_count()} lagu")
    
    nama_artis = input("\nNama Artis: ").strip()
    artist = get_artist(nama_artis)
    
    if not artist:
        print(f"Artis '{nama_artis}' tidak ditemukan!")
        return
    
    if not artist.songs:
        print(f"Artis '{artist.nama_artis}' belum memiliki lagu!")
        return
    
    print(f"\nLagu dari {artist.nama_artis}:")
    for j, judul_lagu in enumerate(artist.songs, 1):
        print(f"  {j}. {judul_lagu}")
    
    judul_lagu = input("\nJudul Lagu yang akan dihapus: ").strip()
    
    # TODO: Tambahkan konfirmasi yang lebih baik
    konfirmasi = input(f"Yakin hapus lagu '{judul_lagu}'? (y/n): ").lower()
    if konfirmasi != 'y':
        print("Batal menghapus.")
        return
    
    if delete_song_from_artist(nama_artis, judul_lagu):
        print(f"\n✓ Lagu '{judul_lagu}' berhasil dihapus dari '{artist.nama_artis}'!")
        print(f"  Sisa lagu: {artist.song_count()}")
    else:
        print(f"✗ Lagu '{judul_lagu}' tidak ditemukan!")




def katalog_delete_artist():
  
    show_coming_soon(
        feature_name="HAPUS ARTIS",
        feature_description="Fitur ini akan memungkinkan Anda menghapus artis beserta semua lagu yang dimilikinya secara otomatis (DELETE CASCADE).",
        planned_features=[
            "Menghapus artis dari database",
            "Otomatis menghapus semua lagu artis (DELETE CASCADE)",
            "Konfirmasi keamanan sebelum menghapus",
            "Validasi data sebelum penghapusan",
            "Backup otomatis sebelum delete"
        ],
        progress=0,
        target_version="1.0"
    )




def katalog_search_artist():
  
    show_under_development(
        feature_name="CARI ARTIS",
        current_status="Pencarian dasar sudah berjalan, perlu tambahan fitur filter",
        todo_items=[
            "Tambah filter berdasarkan genre",
            "Tambah filter berdasarkan tahun debut",
            "Implementasi fuzzy search",
            "Search berdasarkan judul lagu"
        ],
        progress=60
    )
    
    print("  🔄 Fitur pencarian dasar sudah dapat digunakan.\n")
    
    lanjut = input("  Lanjutkan menggunakan fitur ini? (y/n): ").lower()
    if lanjut != 'y':
        return
    
    print("\n--- CARI ARTIS ---\n")
    
    keyword = input("Masukkan nama artis: ").strip()
    if not keyword:
        print("Kata kunci tidak boleh kosong!")
        return
    
    results = search_artist(keyword)
    
    if not results:
        print(f"\n✗ Tidak ditemukan artis dengan kata kunci '{keyword}'")
        return
    
    print(f"\n✓ Ditemukan {len(results)} artis:")
    for i, artist in enumerate(results, 1):
        print(f"\n{i}. {artist.nama_artis}")
        print(f"   Genre      : {artist.genre}")
        print(f"   Tahun Debut: {artist.tahun_debut}")
        print(f"   Jumlah Lagu: {artist.song_count()}")
        
        if artist.songs:
            print(f"   Daftar Lagu:")
            for j, judul_lagu in enumerate(artist.songs, 1):
                print(f"      {j}. {judul_lagu}")



def katalog_report():

    show_under_development(
        feature_name="LAPORAN KATALOG",
        current_status="COUNTING sudah selesai, MAX perlu optimasi",
        todo_items=[
            "Optimasi algoritma MAX",
            "Tambah visualisasi chart yang lebih baik",
            "Export laporan ke file",
            "Statistik lanjutan (rata-rata, median, dll)"
        ],
        progress=65
    )
    
    print("  🔄 Fitur COUNTING sudah dapat digunakan dengan baik.\n")
    
    lanjut = input("  Lanjutkan melihat laporan? (y/n): ").lower()
    if lanjut != 'y':
        return
    
    print("\n--- LAPORAN KATALOG MUSIK ---\n")
    
    if not artists_list:
        print("(Katalog masih kosong)")
        return
    
    # === COUNTING: Total lagu seluruh database ===
    total_songs = count_total_songs()
    print(f"📊 STATISTIK KATALOG")
    print(f"   Total Artis: {len(artists_list)}")
    print(f"   Total Lagu : {total_songs}")
    print()
    
    # === COUNTING: Jumlah lagu per artis ===
    print(f"📋 JUMLAH LAGU PER ARTIS:")
    sorted_artists = get_all_artists_sorted_by_songs()
    for i, (artist, count) in enumerate(sorted_artists, 1):
        bar = "█" * count
        print(f"   {i}. {artist.nama_artis}: {count} lagu {bar}")
    print()
    
    # === MAX: Artis dengan lagu terbanyak ===
    print("🏆 ARTIS DENGAN LAGU TERBANYAK:")
    print("   ⚠️  [Fitur sedang dalam optimasi]")
    print()
    
    # Implementasi sementara
    max_artist, max_count = get_artist_with_most_songs()
    if max_artist:
        print(f"   Hasil Sementara: {max_artist.nama_artis} ({max_count} lagu)")
        print(f"   Genre: {max_artist.genre}")
        print(f"   Tahun Debut: {max_artist.tahun_debut}")
        print()
        print("   💡 Algoritma akan dioptimalkan untuk performa lebih baik")



def menu_katalog():
    """Menu utama untuk mengelola katalog musik"""
    while True:
        clear_screen()
        print_header("KATALOG ALBUM MUSIK [Perkembangan]")
        
        print("Menu Katalog:")
        print()
        print("  ✓ 1. Tambah Artis (Selesai)")
        print("  ✓ 2. Tambah Lagu ke Artis (Selesai)")
        print("  ✓ 3. Lihat Semua Data (Selesai)")
        print("  ⚠ 4. Hapus Lagu (Dalam Pengembangan)")
        print("  ✗ 5. Hapus Artis (Belum Tersedia)")
        print("  ⚠ 6. Cari Artis (Dalam Pengembangan)")
        print("  ⚠ 7. Laporan (Dalam Pengembangan)")
        print()
        print("  📍 8. Lihat Roadmap Pengembangan")
        print("  0. Kembali ke Menu Utama")
        print()
        print("-" * 70)
        print("Keterangan: ✓ = Selesai | ⚠ = Dalam Pengembangan | ✗ = Belum Mulai")
        print("-" * 70)
        
        pilihan = input(">> Pilih menu (0-8): ").strip()
        
        if pilihan == '1':
            katalog_add_artist()
            pause()
        
        elif pilihan == '2':
            katalog_add_song()
            pause()
        
        elif pilihan == '3':
            katalog_view_all()
            pause()
        
        elif pilihan == '4':
            katalog_delete_song()
            pause()
        
        elif pilihan == '5':
            katalog_delete_artist()
            pause()
        
        elif pilihan == '6':
            katalog_search_artist()
            pause()
        
        elif pilihan == '7':
            katalog_report()
            pause()
        
        elif pilihan == '8':
            show_feature_roadmap()
            pause()
        
        elif pilihan == '0':
            break
        
        else:
            print("\n✗ Pilihan tidak valid!")
            time.sleep(1)
