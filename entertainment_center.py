'''Enntertainment Center
Initalize a list of movies and generate an HTML file including this content, 
producing a movie trailer website.
'''
import fresh_tomatoes
import media

movies = []

# Creating movies
forrest_gump = media.Movie("Forrest Gump", 
		"https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
		"https://www.youtube.com/watch?v=bLvqoHBptjg",
		8.8)

inception = media.Movie("Inception", 
		"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
		"https://www.youtube.com/watch?v=66TuSJo4dZM",
		8.8)

avatar = media.Movie("Avatar", 
		"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
		"https://www.youtube.com/watch?v=5PSNL1qE6VY",
		7.9)

the_social_network = media.Movie("The Social Network",
		"https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
		"https://www.youtube.com/watch?v=lB95KLmpLR4",
		7.7)

leon = media.Movie("Leon",
		"https://upload.wikimedia.org/wikipedia/en/0/03/Leon-poster.jpg",
		"https://www.youtube.com/watch?v=Dc1KzpMnuX0",
		8.6)

wolf_wall_street = media.Movie("The Wolf of Wall Street",
		"https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
		"https://www.youtube.com/watch?v=iszwuX1AK6A",
		8.2)

def addMovie(movie):
	movies.append(movie)

addMovie(forrest_gump);
addMovie(inception);
addMovie(avatar);
addMovie(the_social_network);
addMovie(leon);
addMovie(wolf_wall_street);

# Generate HTML file
fresh_tomatoes.open_movies_page(movies)
