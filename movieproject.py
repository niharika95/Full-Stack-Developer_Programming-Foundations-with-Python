import webbrowser

class Movie():
    """This class provides information about movies."""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, genre, posterImage, trailer):
        self.title = title
        self.genre = genre
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailer

    def showTitle(self):
        print(self.title)

    def showGenre(self):
        print(self.genre)

    def showPosterImage(self):
        webbrowser.open(self.poster_image_url)

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
