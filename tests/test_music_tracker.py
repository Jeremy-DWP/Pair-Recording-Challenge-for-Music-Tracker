from lib.music_tracker import *
import pytest


# """
# When first created returns no tracks
# """
def test_mt_returns_empty_list_when_created():
    music_tracker = MusicTracker()
    result = music_tracker.get_tracks() # -> []
    assert result == []

# """
# adds one track returns a list of one track
# """

def test_mt_add_one_track_retunrs_one_track():
    music_tracker = MusicTracker()
    music_tracker.add_tracks("Don't believe the hype")
    result = music_tracker.get_tracks() # -> ["Don't believe the hype"]
    assert result == ["Don't believe the hype"]


# """
# add multiple tracks
# returns a list of multiple tracks
# """

def test_mt_returns_a_list_of_multiple_tracks():
    music_tracker = MusicTracker()
    music_tracker.add_tracks("Don't believe the hype")
    music_tracker.add_tracks("War pigs")
    music_tracker.add_tracks("Rocket man")
    result = music_tracker.get_tracks() 
    assert result == ["Don't believe the hype", "War pigs","Rocket man"]


# """
# If passed a track that is not a string
# returns an error
# """

def test_returns_an_error_with_wrong_data_type():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as err:
        music_tracker.add_tracks(2) # -> Error track of the wrong data type
    assert str(err.value) == "Error track of the wrong data type"
