import webbrowser
class Movie():
    """Class Moview has the two functions.
    --intit-- function is used to intialize the instance variables.
    show_trailer fucntion is to display the trailer from the yout ube URL"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Function to fetch the movie information.
        Values of self, movie_title, movie_storyline, poster_image, trailer_youtube
        will be passed from the entertainment_Center.py and passed to this function.
        Instance variables are created to store the movie information
        Parameters
        ----------
        movie_tile : str
        Movie tile should be passed as String.
        movie_storyline : str
        Movie storyline should be passed as String with the one liner description
        about the movie.
        poster_image : str
        URL to the poster should be passed as String. Respected movies poster
        image URL should be passed here.
        trailer_youtube : str
        Movies youtube trailer URL should be passed as String
        Returns
        -------
        Instance variables with assigned values respectively"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Function to open the web browser. which will take the YOutube URL from the above function and trailer is played"""
        webbrowser.open(self.trailer_youtube_url)
        pass
