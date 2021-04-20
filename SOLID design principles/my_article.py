# SRP
from abc import abstractmethod


class Album:
    def __init__(self, name, artist, songs) -> None:
        self.name = name
        self.artist = artist
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def __str__(self) -> str:
        return f"Album {self.name} by {self.artist}\nTracklist:\n{self.songs}"

    # breaks the SRP
    def search_album_by_artist(self):
        """ Searching the database for other albums by same artist """
        pass


#########################################
album = Album("hello", "SHakira", ["1", "2"])
print(album)

album.remove_song("2")
album.add_song("3")
print(album)


#######################
# OCP


class Album:
    def __init__(self, name, artist, songs, genre) -> None:
        self.name = name
        self.artist = artist
        self.songs = songs
        self.genre = genre


# before
# class AlbumBrowser:
#     def search_album_by_artist(self, albums, artist):
#         return [album for album in albums if album.artist == artist]

#     def search_album_by_genre(self, albums, genre):
#         return [album for album in albums if album.genre == genre]


#################
class SearchBy:
    def is_matched(self, album):
        pass

    def __and__(self, other):
        return AndSearchBy(self, other)


class SearchByGenre(SearchBy):
    def __init__(self, genre):
        self.genre = genre

    def is_matched(self, album):
        return album.genre == self.genre


class SearchByArtist(SearchBy):
    def __init__(self, artist):
        self.artist = artist

    def is_matched(self, album):
        return album.artist == self.artist


class AlbumBrowser:
    def browse(self, albums, searchby):
        return [album for album in albums if searchby.is_matched(album)]


class AndSearchBy(SearchBy):
    def __init__(self, searchby1, searchby2):
        self.searchby1 = searchby1
        self.searchby2 = searchby2

    def is_matched(self, album):
        return self.searchby1.is_matched(album) and self.searchby2.is_matched(
            album
        )


LAWoman = Album(
    name="L.A. Woman",
    artist="The Doors",
    songs=["Riders on the Storm"],
    genre="Rock",
)

Trash = Album(
    name="Trash",
    artist="Alice Cooper",
    songs=["Poison"],
    genre="Rock",
)
albums = [LAWoman, Trash]

# this creates and AndSearchBy object
my_search_criteria = SearchByGenre(genre="Rock") & SearchByArtist(
    artist="The Doors"
)

browser = AlbumBrowser()
assert browser.browse(albums=albums, searchby=my_search_criteria) == [LAWoman]


############# LSP


class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def get_area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = value
        self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = value
        self._height = value


def get_squashed_height_area(Rectangle):
    Rectangle.height = 1
    area = Rectangle.get_area()
    return area


rectangle = Rectangle(5, 5)
square = Square(5)
assert get_squashed_height_area(rectangle) == 5  # expected 5
assert get_squashed_height_area(square) == 1  # expected 5
###########################


# class PlaySong:
#     def __init__(self, title):
#         self.title = title
#         self.sounds = []

#     def play_drums(self):
#         self.sounds.append("Ba-dum ts")

#     def play_guitar(self):
#         self.sounds.append("*Soul-moving guitar solo*")

#     def sing_lyrics(self):
#         self.sounds.append("NaNaNaNa")


# # This class is fine, just changing the guitsr and lyrics
# class PlayRockSong:
#     def play_guitar(self):
#         self.sounds.append("*Very metal guitar solo*")

#     def sing_lyrics(self):
#         self.sounds.append("I wanna rock and roll all night")


# # This breaks the ISP, we don't have lyrics
# class PlayInstrumentalSong:
#     def sing_lyrics(self):
#         raise Exception("No lyrics for instrumental songs")


from abc import ABCMeta


class PlaySongsLyrics:
    @abstractmethod
    def sing_lyrics(self, title):
        pass


class PlaySongsMusic:
    @abstractmethod
    def play_guitar(self, title):
        pass

    @abstractmethod
    def play_drums(self, title):
        pass


class PlayInstrumentalSong(PlaySongsMusic):
    def play_drums(self, title):
        print("Ba-dum ts")

    def play_guitar(self, title):
        print("*Soul-moving guitar solo*")


class PlayRockSong(PlaySongsMusic, PlaySongsLyrics):
    def play_guitar(self, title):
        print("*Very metal guitar solo*")

    def sing_lyrics(self, title):
        print("I wanna rock and roll all night")

    def play_drums(self, title):
        print("Ba-dum ts")


prs = PlayRockSong()
prs.sing_lyrics("Hi")
pim = PlayInstrumentalSong()
pim.sing_lyrics("Hi")
################ DIP ##################


# class AlbumStore:
#     albums = []

#     def add_album(self, name, artist, genre):
#         self.albums.append((name, artist, genre))


# class ViewRockAlbums:
#     def __init__(self, album_store):
#         for album in album_store:
#             if album[2] == "Rock":
#                 print(f"We have {album[0]} by {album[1]} in store.")
# class AlbumStore:
#     albums = []

#     def add_album(self, name, artist, genre):
#         self.albums.append((name, artist, genre))

#     def filter_by_genre(self, genre):
#         for album in self.albums:
#             if album[2] == "Rock":
#                 yield album[0]


# class ViewRockAlbums:
#     def __init__(self, album_store):
#         for album_name in album_store.filter_by_genre("Rock"):
#             print(f"We have {album_name} in store.")


# album_store = AlbumStore()
# album_store.add_album("Hi", "Artist", "Rock")

# viewer = ViewRockAlbums(album_store)