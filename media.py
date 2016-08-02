import webbrowser

class Movie():

        '''
        This class stores movie data with title, movie storyline,
        poster image and trailer from youtube
        '''

        def __init__(self, movie_title, movie_storyline,
		     poster_image, trailer_youtube):

		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube


        def show_trailer(self):

                '''This function shows the trailer of a movie'''

                webbrowser.open(self.trailer_youtube_url)
