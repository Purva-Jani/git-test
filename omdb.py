# in terminal --> pip3 install omdbapi

import omdbapi
import json
from omdbapi.movie_search import GetMovie

# gets the user's favorite movie
userInp = input("what's your favorite movie?\n")
movie = GetMovie(api_key='ebaa4487')
infoJSON = movie.get_movie(userInp)

# converts the data using JSON for readability
infoAsObject = json.dumps(infoJSON)
infoPython = json.loads(infoAsObject)

# returns the genre and country of the user's movie
def getUserInfo():
    return infoPython['genre'], infoPython['country']

# stores the genre and country in variables
userGenre, userCountry = getUserInfo()
print(userGenre)
print(userCountry)
