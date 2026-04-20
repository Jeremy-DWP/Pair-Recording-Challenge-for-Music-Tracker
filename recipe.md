User Story

As a user
So that I can keep track of my music listening 
I want to add tracks I've listened to and see a list of them

Design the class interface

```python
class MusicTracker:

    def __init__(self):
        # parameters:
        #track list - empyt_list
        # side effects:
        #none
        pass

    def add_tracks(self, track):
        # Parameters 
        # track_string_representing_a_music_track
        # returns - nothing
        # side effects
        # added a track to the track list
        pass

    def get_tracks(self):
        # Parameter
        # None
        # Retun
        # Returns a list of the tracks that have been added
        # Side Effects
        # None

```

## Examples as Tests

```python

"""
adds one track returns a list of one track
"""
music_tracker = MusicTracker()
music_tracker.add("Don't believe the hype")
music.tracker.get_tracks() # -> ["Don't believe the hype"]


"""
add multiple tracks
returns a list of multiple tracks
"""
music_tracker = MusicTracker()
music_tracker.add("Don't believe the hype")
music_tracker.add("War pigs")
music_tracker.add("Rocket man")
music.tracker.get_tracks() # -> ["Don't believe the hype", "War pigs","Rocket man"]

"""
When first created returns no tracks
"""
music_tracker = MusicTracker()
music.tracker.get_tracks() # -> []

"""
If passed a track that is not a string
returns an error
"""
music_tracker = MusicTracker()
music_tracker.add(2) # -> Error track of the wrong data type
```