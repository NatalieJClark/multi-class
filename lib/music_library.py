class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self._tracks = []

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Returns:
        #   Nothing
        self._tracks.append(track)

    def all(self):
        # Returns:
        #   A list of instances of Track
        return self._tracks
    
    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: a string
        # Returns:
        #   a list of Track instances with titles that include the keyword
        return [track for track in self._tracks if keyword in track.title]
    