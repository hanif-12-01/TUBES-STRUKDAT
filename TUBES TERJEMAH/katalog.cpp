#include "katalog.h"

void createList(List &L) {
    L.first = NULL;
}

adrArtis createElementArtis(string nama, string genre, int tahun) {
    adrArtis P = new elmArtis;
    P->info.nama = nama;
    P->info.genre = genre;
    P->info.tahunDebut = tahun;
    P->next = NULL;
    P->firstLagu = NULL;
    return P;
}

adrLagu createElementLagu(string judul) {
    adrLagu P = new elmLagu;
    P->judul = judul;
    P->next = NULL;
    return P;
}

// --- FUNGSI UTAMA PARENT (ARTIS) ---

void insertLastArtis(List &L, adrArtis P) {
    if (L.first == NULL) {
        L.first = P;
    } else {
        adrArtis Q = L.first;
        while (Q->next != NULL) {
            Q = Q->next;
        }
        Q->next = P;
    }
}

adrArtis searchArtis(List L, string nama) {
    adrArtis P = L.first;
    while (P != NULL) {
        if (P->info.nama == nama) {
            return P;
        }
        P = P->next;
    }
    return NULL;
}

void deleteArtis(List &L, string nama) {
    adrArtis P = searchArtis(L, nama);
    
    if (P == NULL) {
        cout << "Artis tidak ditemukan!" << endl;
        return;
    }

    // 1. DELETE CASCADE: Hapus semua lagu (anak) dulu sebelum hapus artis
    adrLagu C = P->firstLagu;
    while (C != NULL) {
        adrLagu temp = C;
        C = C->next;
        delete temp;
    }
    P->firstLagu = NULL;

    // 2. HAPUS ARTIS DARI LIST
    if (P == L.first) {
        L.first = P->next;
    } else {
        adrArtis Q = L.first;
        while (Q->next != P) {
            Q = Q->next;
        }
        Q->next = P->next;
    }
    delete P;
    cout << "Artis dan semua lagunya berhasil dihapus." << endl;
}

// --- FUNGSI UTAMA CHILD (LAGU) ---

void insertLastLagu(adrArtis P, adrLagu C) {
    if (P->firstLagu == NULL) {
        P->firstLagu = C;
    } else {
        adrLagu Q = P->firstLagu;
        while (Q->next != NULL) {
            Q = Q->next;
        }
        Q->next = C;
    }
}

void deleteLagu(adrArtis P, string judul) {
    if (P->firstLagu == NULL) {
        cout << "Lagu kosong." << endl;
        return;
    }

    adrLagu C = P->firstLagu;
    adrLagu prev = NULL;
    bool found = false;

    while (C != NULL) {
        if (C->judul == judul) {
            found = true;
            break;
        }
        prev = C;
        C = C->next;
    }

    if (found) {
        if (prev == NULL) {
            P->firstLagu = C->next;
        } else {
            prev->next = C->next;
        }
        delete C;
        cout << "Lagu berhasil dihapus." << endl;
    } else {
        cout << "Lagu tidak ditemukan." << endl;
    }
}

// --- VIEW & PENGOLAHAN DATA ---

void showAllData(List L) {
    if (L.first == NULL) {
        cout << "Data Kosong." << endl;
        return;
    }

    adrArtis P = L.first;
    while (P != NULL) {
        cout << "---------------------------------" << endl;
        cout << "Artis : " << P->info.nama << " (" << P->info.genre << ")" << endl;
        cout << "Debut : " << P->info.tahunDebut << endl;
        
        adrLagu C = P->firstLagu;
        if (C == NULL) {
            cout << "   (Belum ada lagu)" << endl;
        } else {
            int i = 1;
            while (C != NULL) {
                cout << "   " << i << ". " << C->judul << endl;
                C = C->next;
                i++;
            }
        }
        P = P->next;
    }
}

// Fitur Counting: Menghitung total lagu di seluruh list
int countTotalLagu(List L) {
    int total = 0;
    adrArtis P = L.first;
    while (P != NULL) {
        adrLagu C = P->firstLagu;
        while (C != NULL) {
            total++;
            C = C->next;
        }
        P = P->next;
    }
    return total;
}

// Fitur MAX: Menampilkan artis dengan lagu terbanyak
void showMostProductiveArtis(List L) {
    if (L.first == NULL) return;

    adrArtis P = L.first;
    adrArtis maxArtis = P;
    int maxCount = 0;

    // Hitung max awal
    adrLagu C = P->firstLagu;
    while(C != NULL) { maxCount++; C = C->next; }

    P = P->next;
    while (P != NULL) {
        int currentCount = 0;
        C = P->firstLagu;
        while(C != NULL) { currentCount++; C = C->next; }

        if (currentCount > maxCount) {
            maxCount = currentCount;
            maxArtis = P;
        }
        P = P->next;
    }

    cout << "\n=== ARTIS PALING PRODUKTIF ===" << endl;
    cout << "Nama        : " << maxArtis->info.nama << endl;
    cout << "Jumlah Lagu : " << maxCount << endl;
}