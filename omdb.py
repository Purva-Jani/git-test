# in terminal --> pip3 install omdbapi

import omdbapi
from omdbapi.movie_search import GetMovie

movie = GetMovie(api_key="ebaa4487")
print(movie.get_movie("Interstellar"))