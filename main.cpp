#include <iostream>
#include <limits>
#include <string>
#include "katalog.h"

using namespace std;

void clearScreen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

void waitForEnter() {
    cout << "\n[Tekan Enter untuk kembali...]";
    string dummy;
    getline(cin, dummy);
}

int readMenuChoice() {
    string line;
    cout << "Pilih: ";
    if (!getline(cin, line)) return 0; // treat EOF as exit
    try {
        size_t pos;
        int val = stoi(line, &pos);
        if (pos != line.size()) return -1;
        return val;
    } catch (...) {
        return -1;
    }
}

int main() {
    List L;
    createList(L);

    string namaFile = "music_db..csv"; // file in project

    cout << "=== LOADING DATABASE: " << namaFile << " ===" << endl;
    bool loaded = loadFromCSV(namaFile, L);
    if (loaded) cout << "[OK] Database berhasil dimuat dari CSV." << endl;
    else cout << "[WARN] File CSV tidak ditemukan atau kosong. Menggunakan data dummy." << endl;

    if (!loaded) {
        // fallback data
        adrArtis a1 = createElementArtis("Tulus", "Pop", 2011);
        insertLastArtis(L, a1);
        insertLastLagu(a1, createElementLagu("Hati-Hati di Jalan"));
        insertLastLagu(a1, createElementLagu("Monokrom"));

        adrArtis a2 = createElementArtis("Sheila on 7", "Rock", 1996);
        insertLastArtis(L, a2);
        insertLastLagu(a2, createElementLagu("Sephia"));
        insertLastLagu(a2, createElementLagu("Dan"));
        insertLastLagu(a2, createElementLagu("Melompat Lebih Tinggi"));
    }

    int pilihan = -1;
    int tahun;
    string nama, genre, judul;
    adrArtis pFound;

    do {
        cout << "\n=== APLIKASI KATALOG MUSIK ===" << endl;
        cout << "1. Tambah Artis Baru" << endl;
        cout << "2. Tambah Lagu ke Artis" << endl;
        cout << "3. Tampilkan Semua Data" << endl;
        cout << "4. Hapus Lagu" << endl;
        cout << "5. Hapus Artis (Beserta Lagunya)" << endl;
        cout << "6. Cari Artis" << endl;
        cout << "7. Laporan (Total & Artis Terproduktif)" << endl;
        cout << "0. Keluar" << endl;

        pilihan = readMenuChoice();
        if (pilihan == -1) {
            cout << "Pilihan tidak valid. Masukkan angka." << endl;
            continue;
        }

        switch (pilihan) {
            case 1:
                cout << "\n--- TAMBAH ARTIS BARU ---" << endl;
                cout << "Nama Artis: "; getline(cin, nama);
                cout << "Genre: "; getline(cin, genre);
                cout << "Tahun Debut: ";
                {
                    string t; getline(cin, t);
                    try { tahun = stoi(t); } catch(...) { tahun = 0; }
                }
                insertLastArtis(L, createElementArtis(nama, genre, tahun));
                cout << "[OK] Artis berhasil ditambahkan!" << endl;
                break;

            case 2:
                cout << "\n--- TAMBAH LAGU KE ARTIS ---" << endl;
                cout << "Masukkan Nama Artis: "; getline(cin, nama);
                pFound = searchArtis(L, nama);
                if (pFound != NULL) {
                    cout << "Judul Lagu: "; getline(cin, judul);
                    insertLastLagu(pFound, createElementLagu(judul));
                    cout << "[OK] Lagu berhasil ditambahkan!" << endl;
                } else {
                    cout << "[X] Artis tidak ditemukan!" << endl;
                }
                break;

            case 3:
                cout << "\n--- TAMPILKAN SEMUA DATA ---" << endl;
                showAllData(L);
                break;

            case 4:
                cout << "\n--- HAPUS LAGU ---" << endl;
                cout << "Nama Artis: "; getline(cin, nama);
                pFound = searchArtis(L, nama);
                if (pFound != NULL) {
                    cout << "Judul Lagu yg dihapus: "; getline(cin, judul);
                    deleteLagu(pFound, judul);
                } else {
                    cout << "[X] Artis tidak ditemukan!" << endl;
                }
                break;

            case 5:
                cout << "\n--- HAPUS ARTIS ---" << endl;
                cout << "Nama Artis yg dihapus: "; getline(cin, nama);
                deleteArtis(L, nama);
                break;

            case 6:
                cout << "\n--- CARI ARTIS ---" << endl;
                cout << "Cari Nama Artis: "; getline(cin, nama);
                pFound = searchArtis(L, nama);
                if (pFound != NULL) {
                    cout << "[OK] Ditemukan: " << pFound->info.nama << " - " << pFound->info.genre << endl;
                } else {
                    cout << "[X] Tidak ditemukan." << endl;
                }
                break;

            case 7:
                cout << "\n=== LAPORAN KATALOG MUSIK ===" << endl;
                cout << "Total Lagu di Database: " << countTotalLagu(L) << endl;
                showMostProductiveArtis(L);
                break;

            case 0:
                cout << "\nTerima kasih! Program selesai." << endl;
                break;

            default:
                cout << "Pilihan tidak valid." << endl;
        }

        if (pilihan != 0) {
            waitForEnter();
            clearScreen();
        }

    } while (pilihan != 0);

    return 0;
}