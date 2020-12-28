import requests
import json

# We're using jikan to get the MyAnimeList data
class Jikan():
    valid_categories = ["anime", "manga", "people", "character"]

    def __init__(self, category, query):
        self.category = category
        self.query = query

    def get_info(self):
        if self.category in self.valid_categories:
            response = requests.get("https://api.jikan.moe/v3/search/" + self.category + "?q=" + self.query)
            json_data= json.loads(response.text)
            if json_data['results']:
                result_url = json_data['results'][0]['url'] + " \n"
                if self.category == "anime" or self.category == "manga" :
                    content = "*" + json_data['results'][0]['title'] + "*   : " + json_data['results'][0]['synopsis']
                    search_result = result_url + content 
                elif self.category == "people" or self.category == "character":
                    name = "*" + json_data['results'][0]['name'] + "*"
                    search_result = result_url + name             
                return(search_result)
            else:
                return("Sorry, I can't find anything~")
        else:
            return("Please specify what you want to search~ \n `roboco mal [anime/manga/people/character] [your query]`")