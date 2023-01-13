# Brian Sprouse, Chandana Rao, Purva Jani
# omdb.py
# 1/18/23

# in terminal --> pip3 install omdbapi

# import statements (install in terminal)
import omdbapi
import json
from omdbapi.movie_search import GetMovie

# gets the user's favorite movie using the api
userInp = input("name a movie:\n")
movie = GetMovie(api_key='ebaa4487')
infoJSON = movie.get_movie(userInp)

# converts the data using JSON for readability
infoAsObject = json.dumps(infoJSON)
infoPython = json.loads(infoAsObject)

# function getUserInfo
# postcondition: returns the details of the user's movie
def getUserInfo():
    # if movie not in database
    if (infoPython == 'Movie not found!'):
        return None
    # grabs movie characteristics
    else:
        return (infoPython['title'], infoPython['released'], infoPython['rated'], 
        infoPython['runtime'], infoPython['genre'], infoPython['director'], infoPython['plot'] )

# function editGrammar
# parameters: genre, plot
# postcondition: returns genre and plot made grammatically coherent
def editGrammar(genre, plot):
    # sets genre and plot to lowercase
    genre = genre.lower()
    plot = plot[0].lower() + plot[1:]

    # inserts 'and' after last comma
    if (',' in genre):
        i = len(genre) - 1
        while (genre[i] != ','):
            i -= 1
        genre = genre[:i + 1] + " and" + genre[i + 1:]
    
    return genre, plot

# function showSummary
# postcondition: displays the movie synopsis
def showSummary():
    # nothing shown if movie not in database
    if (getUserInfo() == None):
        print(infoPython)
    else:
        # variables
        title, date, rating, length, genre, director, plot = getUserInfo()

        # edits genre and plot for grammar
        genre, plot = editGrammar(genre, plot)

        # prints summary in paragraph form
        print(title + " was released on " + date + ". In this movie with a runtime of " + length
        + " and a " + rating + " rating, director " + director + " presents us with a film packed with "
        + genre + ". In " + title + ", " + plot)

# calls the function to show the synopsis
showSummary()
