artists_list = []  # MLL: LIST OF PARENT (Artist)
import json #untuk memasukkan dan menyimpan data dalam format JSON
import os #untuk operasi sistem seperti cek file dan path
from database.models import Artist #bacanya  dari file database.model.py itu kita mengimport Artist


# Path ke file database JSON
DB_PATH = os.path.join(os.path.dirname(__file__), 'music_db.json')



def load_database():

    global artists_list
    
    if not os.path.exists(DB_PATH):
        print("Database belum ada, membuat data awal...")
        initialize_default_data()
        save_database()
        return
    
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        artists_list = [Artist.from_dict(a) for a in data.get('artists', [])]
        
        total_songs = sum(artist.song_count() for artist in artists_list)
        print(f"Database loaded: {len(artists_list)} artis, {total_songs} lagu")
    
    except Exception as e:
        print(f"Error loading database: {e}")
        initialize_default_data()


def save_database():

    try:
        data = {
            'artists': [artist.to_dict() for artist in artists_list]
        }
        
        with open(DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print("Database berhasil disimpan!")
    
    except Exception as e:
        print(f"Error saving database: {e}")


def initialize_default_data():

    global artists_list
    
    artists_list = []
    
    # Contoh artis 1
    tulus = Artist("Tulus", "Pop", 2011)
    tulus.add_song("Hati-Hati di Jalan")
    tulus.add_song("Monokrom")
    artists_list.append(tulus)
    
    # Contoh artis 2
    sheila = Artist("Sheila on 7", "Pop Rock", 1996)
    sheila.add_song("Dan")
    sheila.add_song("Sephia")
    artists_list.append(sheila)
    
    print("Data default berhasil dibuat!")


def get_artist(name):

    for artist in artists_list:
        if artist.nama_artis.lower() == name.lower():
            return artist
    return None

# Fungsi untuk mengambil semua artis (agar akses selalu update)
def get_all_artists():
    return artists_list


def add_artist(nama_artis, genre, tahun_debut):

    if get_artist(nama_artis):
        return False
    
    new_artist = Artist(nama_artis, genre, tahun_debut)
    artists_list.append(new_artist)
    return True


def delete_artist(name):
    artist = get_artist(name)
    if not artist:
        return False
    
    # IMPLEMENTASI SEMENTARA
    artists_list.remove(artist)
    return True


def add_song_to_artist(artist_name, judul_lagu):
    artist = get_artist(artist_name)
    if not artist:
        return False
    
    if artist.has_song(judul_lagu):
        return False
    
    artist.add_song(judul_lagu)
    return True


def delete_song_from_artist(artist_name, judul_lagu):
    artist = get_artist(artist_name)
    if not artist:
        return False
    
    return artist.remove_song(judul_lagu)


def search_artist(keyword):
    results = []
    for artist in artists_list:
        if keyword.lower() in artist.nama_artis.lower():
            results.append(artist)
    return results


def count_total_songs():

    total = 0
    for artist in artists_list:
        total += artist.song_count()
    return total


def get_artist_with_most_songs():

    if not artists_list:
        return (None, 0)
    
    # IMPLEMENTASI SEMENTARA - BELUM OPTIMAL
    max_artist = artists_list[0]
    max_count = max_artist.song_count()
    
    for artist in artists_list:
        if artist.song_count() > max_count:
            max_artist = artist
            max_count = artist.song_count()
    
    return (max_artist, max_count)


def get_all_artists_sorted_by_songs():
    artist_counts = [(artist, artist.song_count()) for artist in artists_list]
    
    # BUBBLE SORT - IMPLEMENTASI SEMENTARA
    # TODO: Ganti dengan algoritma sorting yang lebih efisien
    n = len(artist_counts)
    for i in range(n):
        for j in range(0, n-i-1):
            if artist_counts[j][1] < artist_counts[j+1][1]:
                artist_counts[j], artist_counts[j+1] = artist_counts[j+1], artist_counts[j]
    
    return artist_counts
