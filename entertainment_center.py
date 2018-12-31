import media
import fresh_tomatoes
two_pointO = media.Movie("2.0", "2.0 is a 2018 Indian Tamil-language science fiction action film", "https://upload.wikimedia.org/wikipedia/en/c/cf/2.0_film_poster.jpg", "https://www.youtube.com/watch?v=7cx-KSsYcjg")
#print(two_pointO.storyline)
avatar = media.Movie("Avatar", "A marine on an Alien Plant", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=wsnMbDdhCe8")
mersal = media.Movie("Mersal", "A Story of twins , as a magician and as a doctor", "https://upload.wikimedia.org/wikipedia/en/5/5c/Mersal_Theatrical_Release_Poster.jpg", "https://www.youtube.com/watch?v=gQDo5QuZTaw")
petta = media.Movie("Petta", "A Story of Hostel warden. Marana Mass Action film", "https://upload.wikimedia.org/wikipedia/en/c/c3/Petta_poster.jpg", "https://www.youtube.com/watch?v=FCB0ZfQ9Rzs")
CCV = media.Movie("Chekka Chivantha Vanam", "A Story of Don and his three sons fighting to acquire the position of Don", "https://upload.wikimedia.org/wikipedia/en/3/3e/Chekka_Chivantha_Vaanam.jpg", "https://www.youtube.com/watch?v=x2q5w-ThJeE")
Vikram_Vedha= media.Movie("Vikram Vedha", "War between a police officer and a criminal", "https://upload.wikimedia.org/wikipedia/en/0/03/Vikram_Vedha_poster.jpg", "https://www.youtube.com/watch?v=1sVr-uWZPjE")

movies = [two_pointO, avatar, mersal, petta, CCV, Vikram_Vedha]
fresh_tomatoes.open_movies_page(movies)



#print(avatar.storyline)
#avatar.show_trailer()
