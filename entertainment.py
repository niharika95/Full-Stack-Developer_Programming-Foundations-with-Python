import movieproject

toyStory = movieproject.Movie("Toy Story", "This is about a boy who's toys come to life.", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toyStory.posterImage)

avatar = movieproject.Movie("Avatar", "This is about Avatar.", "posterImage", "trailer")
print(avatar.title)
