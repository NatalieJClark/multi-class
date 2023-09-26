from lib.music_library import MusicLibrary
from lib.track import Track
"""
When we add two tracks
We get the tracks back in the track list
"""
def test_add_multiple_tracks_and_lists_them():
    music_library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.all() == [track_1, track_2]

"""
When we add two tracks
And we search for the title of one of the tracks
We get the matching track back
"""
def test_searches_by_title():
    music_library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("Always The Hard Way") == [track_1]

"""
When we add two tracks
And we search for a small part of a word in the title
We get the matching track back
"""
def test_searches_by_part_of_title():
    music_library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("lace") == [track_2]

"""
When we add two tracks
And we search for a word not in any track title
We get an empty list back
"""
def test_search_word_not_in_any_title():
    music_library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("zzz") == []


