import webbrowser
class Movie():
    """Class Moview has the two functions. --intit-- function is used to intialize the instance variables. show_trailer fucntion is to display the trailer from the yout ube URL"""
   
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
	 """Function to fetch the movie information. Values of self, movie_title, movie_storyline, poster_image, trailer_youtube will be passed from the entertainment_Center.py and passed to this function. Instance variables are created to store the movie information"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
	""" Function to open the web browser """
        webbrowser.open(self.trailer_youtube_url)
    pass
