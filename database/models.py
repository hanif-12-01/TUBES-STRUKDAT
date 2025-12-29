

class Artist:
    # MLL PARENT NODE 
    def __init__(self, nama_artis, genre, tahun_debut):
        self.nama_artis = nama_artis    # Nama artis - KEY UNIK (string)
        self.genre = genre              # Genre musik (string)
        self.tahun_debut = tahun_debut  # Tahun debut (integer)
        self.songs = []                 # MLL CHILD LIST (list of lagu)
    
    def add_song(self, judul_lagu):
        self.songs.append(judul_lagu)
    
    def remove_song(self, judul_lagu):
        # IMPLEMENTASI SEMENTARA - BELUM OPTIMAL
        for i, song in enumerate(self.songs):
            if song.lower() == judul_lagu.lower():
                self.songs.pop(i)
                return True
        return False
    
    def song_count(self):
        return len(self.songs)
    
    def has_song(self, judul_lagu):
        for song in self.songs:
            if song.lower() == judul_lagu.lower():
                return True
        return False
    
    def to_dict(self):

        return {
            'nama_artis': self.nama_artis,
            'genre': self.genre,
            'tahun_debut': self.tahun_debut,
            'songs': self.songs
        }
    
    @staticmethod
    def from_dict(data):
        artist = Artist(
            data['nama_artis'],
            data['genre'],
            data.get('tahun_debut', 2000)
        )
        artist.songs = data.get('songs', [])
        return artist
