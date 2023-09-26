from lib.track import Track

"""
When we create a new track
We can get its title and artist back
"""
def test_construct_track_and_get_title_and_artist():
    track = Track("My Title", "My Artist")
    assert track.title == "My Title"
    assert track.artist == "My Artist"

"""
Given a track with a title and artist
#format returns a string like TITLE by ARTIST
"""
def test_formats_title_and_artist():
    track = Track("Higher Place", "Malevolence")
    assert track.format() == "Higher Place by Malevolence"