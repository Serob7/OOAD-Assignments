from validators import not_empty_string

class Album:
    @not_empty_string('Title', 1)
    @not_empty_string('Artist', 2)
    @not_empty_string('Release date', 3)

    def __init__(self, title, artist, release_date):
        self.title = title
        self.artist = artist
        self.release_date = release_date
        self.songs = []

    def add_song_to_album(self, song):
        self.songs.append(song)


