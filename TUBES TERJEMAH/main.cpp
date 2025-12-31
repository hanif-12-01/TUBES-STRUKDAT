#include <iostream>
#include <limits>
#include "katalog.h" // Include header, kompilasi bersama katalog.cpp

using namespace std;

// Bersihkan layar (cross-platform)
void clearScreen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

// Tunggu sampai pengguna menekan Enter (lebih andal untuk interaktif)
void waitForEnter() {
    cout << "\n[Tekan Enter untuk kembali...]";
    string dummy;
    getline(cin, dummy);
}

int main() {
    List L;
    createList(L);

    // Data Dummy (Biar tidak kosong saat dijalankan)
    adrArtis a1 = createElementArtis("Tulus", "Pop", 2011);
    insertLastArtis(L, a1);
    insertLastLagu(a1, createElementLagu("Hati-Hati di Jalan"));
    insertLastLagu(a1, createElementLagu("Monokrom"));

    adrArtis a2 = createElementArtis("Sheila on 7", "Rock", 1996);
    insertLastArtis(L, a2);
    insertLastLagu(a2, createElementLagu("Sephia"));
    insertLastLagu(a2, createElementLagu("Dan"));
    insertLastLagu(a2, createElementLagu("Melompat Lebih Tinggi"));

    int pilihan, tahun;
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
        cout << "Pilih: ";
        cin >> pilihan;
        cin.ignore(); 

        switch(pilihan) {
            case 1:
                cout << "Nama Artis: "; getline(cin, nama);
                cout << "Genre: "; getline(cin, genre);
                cout << "Tahun Debut: "; cin >> tahun;
                insertLastArtis(L, createElementArtis(nama, genre, tahun));
                break;
            case 2:
                cout << "Masukkan Nama Artis: "; getline(cin, nama);
                pFound = searchArtis(L, nama);
                if (pFound != NULL) {
                    cout << "Judul Lagu: "; getline(cin, judul);
                    insertLastLagu(pFound, createElementLagu(judul));
                } else {
                    cout << "Artis tidak ditemukan!" << endl;
                }
                break;
            case 3:
                showAllData(L);
                break;
            case 4:
                cout << "Nama Artis: "; getline(cin, nama);
                pFound = searchArtis(L, nama);
                if (pFound != NULL) {
                    cout << "Judul Lagu yg dihapus: "; getline(cin, judul);
                    deleteLagu(pFound, judul);
                } else {
                    cout << "Artis tidak ditemukan!" << endl;
                }
                break;
            case 5:
                cout << "Nama Artis yg dihapus: "; getline(cin, nama);
                deleteArtis(L, nama);
                break;
            case 6:
                cout << "Cari Nama Artis: "; getline(cin, nama);
                pFound = searchArtis(L, nama);
                if (pFound != NULL) {
                    cout << "Ditemukan: " << pFound->info.nama << " - " << pFound->info.genre << endl;
                } else {
                    cout << "Tidak ditemukan." << endl;
                }
                break;
            case 7:
                cout << "Total Lagu di Database: " << countTotalLagu(L) << endl;
                showMostProductiveArtis(L);
                break;
        }

        if (pilihan != 0) {
            waitForEnter();
            clearScreen();
        }

    } while (pilihan != 0);

    return 0;
}