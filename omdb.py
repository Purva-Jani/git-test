# in terminal --> pip3 install omdbapi

import omdbapi
from omdbapi.movie_search import GetMovie

clientInp = input("what's your favorite movie?\n")
movie = GetMovie(api_key="ebaa4487")
print(movie.get_movie(clientInp))
# print(movie.get_data('genre', 'language', 'imdbrating'))
# print(movie.get_data('director', 'actors', 'awards', 'plot'))

def getMovieRecommendations():
    movieName = clientInp
    
    

