class MusicTracker:

    def __init__(self):
        self.track_list = []

    def add_tracks(self, track):
        if not isinstance(track, str):
            raise Exception("Error track of the wrong data type")
        
        self.track_list.append(track)

    def get_tracks(self):
        return self.track_list