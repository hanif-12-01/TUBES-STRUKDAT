#ifndef KATALOG_H
#define KATALOG_H

#include <iostream>
#include <string>

using namespace std;

// --- DEFINISI STRUKTUR DATA MLL ---

// 1. Definisi Pointer
typedef struct elmArtis *adrArtis;
typedef struct elmLagu *adrLagu;

// 2. CHILD NODE (LAGU)
// Syarat Gambar: Data anak berupa TIPE DASAR (String)
struct elmLagu {
    string judul;       // <--- Tipe Dasar (Hanya String)
    adrLagu next;       // Pointer ke lagu berikutnya
};

// 3. PARENT NODE (ARTIS)
// Syarat Gambar: Data parent berupa RECORD/STRUCT
struct DataArtis {
    string nama;
    string genre;
    int tahunDebut;
};

struct elmArtis {
    DataArtis info;     // <--- Record (Struct)
    adrArtis next;      // Pointer ke artis berikutnya
    adrLagu firstLagu;  // Pointer ke list anak (Head of Child)
};

// 4. LIST PARENT
struct List {
    adrArtis first;
};

// --- PROTOTYPE FUNGSI ---

// Pembuatan List & Element
void createList(List &L);
adrArtis createElementArtis(string nama, string genre, int tahun);
adrLagu createElementLagu(string judul);

// Manajemen Parent (Artis) - CRUD
void insertLastArtis(List &L, adrArtis P);
void deleteArtis(List &L, string nama); // Delete Cascade
adrArtis searchArtis(List L, string nama);
void showAllData(List L);

// Manajemen Child (Lagu) - CRUD
void insertLastLagu(adrArtis P, adrLagu C);
void deleteLagu(adrArtis P, string judul);

// Pengolahan Data (Sesuai Syarat: Min/Max/Counting)
int countTotalLagu(List L);
void showMostProductiveArtis(List L); // Max Logic

#endif