# in terminal --> pip3 install requests

# import requests

# class MovieClient(object):
#     def __init__(self):
#         self.sess = requests.Session()
#         self.base_url = "http://www.omdbapi.com/?apikey=ebaa4487&r=json&type=movie&"

#     def search(self, search_string):
#         """
#         Searches the API for the supplied search_string, and returns
#         a list of Media objects if the search was successful, or the error response
#         if the search failed.
#         Only use this method if the user is using the search bar on the website.
#         """

#         search_string = "+".join(search_string.split())
#         page = 1

#         search_url = f"s={search_string}&page={page}"
#         print(self.base_url + search_url)
#         resp = self.sess.get(self.base_url + search_url)
#         if resp.status_code != 200:
#             raise ValueError(
#                 "Search request failed; make sure your API key is correct and authorized"
#             )

# client = MovieClient()
# client.search("Interstellar")
# client.search("Guardians")