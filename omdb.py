# in terminal --> pip3 install omdbapi

import omdbapi
from omdbapi.movie_search import GetMovie

userInp = input("what's your favorite movie?\n")
movie = GetMovie(api_key="ebaa4487")
print(movie.get_movie(userInp))
