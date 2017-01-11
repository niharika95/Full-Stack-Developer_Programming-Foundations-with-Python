import movieproject
import fresh_tomatoes

toyStory = movieproject.Movie("Toy Story", "Animation", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = movieproject.Movie("Avatar", "Sci-fi", "https://resizing.flixster.com/1sUvLZ6JH-67S874Ia_qKiEpO_A=/206x305/v1.bTsxMTE3Njc5MjtqOzE3Mjc0OzEyMDA7ODAwOzEyMDA", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
theNotebook = movieproject.Movie("The Notebook", "Romance", "https://s-media-cache-ak0.pinimg.com/originals/b1/3f/f7/b13ff7d7e0cec53c15abc9b9f7237800.jpg", "https://www.youtube.com/watch?v=FC6biTjEyZw")
theConjuring = movieproject.Movie("The Conjuring", "Horror", "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg", "https://www.youtube.com/watch?v=Vjk2So3KvSQ")
shutterIsland = movieproject.Movie("Shutter Island", "Suspense", "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg", "https://www.youtube.com/watch?v=5iaYLCiq5RM")
clueless = movieproject.Movie("Clueless", "Comedy", "https://upload.wikimedia.org/wikipedia/en/2/21/Clueless.jpg", "https://www.youtube.com/watch?v=bq1KKG-dh1M")

movies = [toyStory, avatar, theNotebook, theConjuring, shutterIsland, clueless]
fresh_tomatoes.open_movies_page(movies)





##toyStory.showTitle()
##toyStory.showGenre()
##toyStory.showPosterImage()
##toyStory.showTrailer()
##avatar.showTitle()
##avatar.showGenre()
##avatar.showPosterImage()
##avatar.showTrailer()
##theNotebook.showTitle()
##theNotebook.showGenre()
##theNotebook.showPosterImage()
##theNotebook.showTrailer()
##theConjuring.showTitle()
##theConjuring.showGenre()
##theConjuring.showPosterImage()
##theConjuring.showTrailer()
##shutterIsland.showTitle()
##shutterIsland.showGenre()
##shutterIsland.showPosterImage()
##shutterIsland.showTrailer()
##clueless.showTitle()
##clueless.showGenre()
##clueless.showPosterImage()
##clueless.showTrailer()
