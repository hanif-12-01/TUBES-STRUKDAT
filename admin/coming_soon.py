
def show_coming_soon(feature_name, feature_description, planned_features, progress=0, target_version="1.0"):

    width = 70
    
    print("\n")
    print("=" * width)
    print("🚧 COMING SOON 🚧".center(width))
    print("=" * width)
    print()
    print(f"FITUR: {feature_name}".center(width))
    print()
    print("-" * width)
    print()
    print(f"  {feature_description}")
    print()
    
    if planned_features:
        print("  📋 Yang akan bisa dilakukan:")
        for feature in planned_features:
            print(f"     • {feature}")
        print()
    
    # Progress bar
    filled = int(progress / 10)
    empty = 10 - filled
    progress_bar = "▰" * filled + "▱" * empty
    
    print("  📅 Status Pengembangan:")
    print(f"     Progress: {progress_bar} {progress}%")
    print(f"     Target  : Versi {target_version}")
    print()
    
    print("  🔧 Fitur ini sedang dalam tahap perencanaan dan pengembangan.")
    print()
    print("-" * width)
    print("  💡 Saran: Gunakan fitur lain yang sudah tersedia sementara waktu")
    print("-" * width)
    print()


def show_under_development(feature_name, current_status, todo_items, progress=50):
    width = 70
    
    print("\n")
    print("=" * width)
    print("⚠️  DALAM PENGEMBANGAN ⚠️".center(width))
    print("=" * width)
    print()
    print(f"FITUR: {feature_name}".center(width))
    print()
    print("-" * width)
    print()
    print(f"  Status: {current_status}")
    print()
    
    # Progress bar
    filled = int(progress / 10)
    empty = 10 - filled
    progress_bar = "▰" * filled + "▱" * empty
    
    print(f"  Progress: {progress_bar} {progress}%")
    print()
    
    if todo_items:
        print("  🔧 Yang masih perlu diselesaikan:")
        for item in todo_items:
            print(f"     [ ] {item}")
        print()
    
    print("-" * width)
    print("  ⚠️  Fitur ini mungkin belum berfungsi dengan sempurna")
    print("-" * width)
    print()


def show_feature_roadmap():
    width = 70
    
    print("\n")
    print("=" * width)
    print("📍 ROADMAP PENGEMBANGAN 📍".center(width))
    print("=" * width)
    print()
    
    print("  PHASE 1: FOUNDATION (50% Selesai) ✓")
    print("     ✓ Struktur MLL dasar")
    print("     ✓ CRUD Parent (Tambah Artis)")
    print("     ✓ CRUD Child (Tambah Lagu)")
    print("     ✓ View semua data")
    print()
    
    print("  PHASE 2: CORE FEATURES (Target 75%)")
    print("     ⚠ Hapus Lagu (70%)")
    print("     ⚠ Cari Artis (60%)")
    print("     ⚠ Laporan (65%)")
    print()
    
    print("  PHASE 3: ADVANCED FEATURES (Target 100%)")
    print("     ✗ Hapus Artis + CASCADE (0%)")
    print("     ✗ Filter & Sort Advanced (0%)")
    print()
    
    print("-" * width)
    print("  Keterangan:")
    print("     ✓ = Selesai | ⚠ = Dalam Pengembangan | ✗ = Belum Mulai")
    print("-" * width)
    print()
