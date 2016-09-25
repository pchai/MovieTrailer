import webbrowser

class Movie():

	def __init__(self, movie_title, poster_image, trailer_youtube, imdb_score):
		"""Movie class
		Data structure for represnting a movie

		Args:
	        movie_title (str): Movie title
	        poster_image (str): Movie poster image url
	        trailer_youtube (str): Movie trailer video url
	        imdb_score (double): Movie IMDB score
		"""
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.movie_imdb_score = imdb_score
