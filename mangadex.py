import requests
import json

# MangaDex API (no authentication needed)
class MangaDex():
    manga_url = ""
    manga_info = ""
    manga_cover = ""
    manga_synopsis = ""

    def __init__(self, manga_url):
        self.manga_url = manga_url

    # translates mangadex genre/theme IDs from the json file
    def get_genre_names(self, id_list):
        with open('mangadex_tags.json', 'r') as f:
            genre_dict = json.load(f)
        genres = list()
        for ids in id_list:
            genres.append(genre_dict[str(ids)]['name'])        
        return ", ".join(genres)

    def get_info(self):
        url_parts = self.manga_url.split('/')
        manga_id = url_parts[4]

        api_url = "https://mangadex.org/api/v2/manga/" + manga_id
        response = requests.get(api_url)
        json_data= json.loads(response.text)
        if json_data['code'] == 200:
            result = json_data['data']
            title = "Title: " + result['title'] + " \n"
            authors = "Authors: " + ", ".join(result['author']) + " \n"
            artists = "Artists: " + ", ".join(result['artist']) + " \n"
            genre = "Genre: " + self.get_genre_names(result['tags']) + " \n"
            chapters = "Last Chapter: " + str(result['lastChapter']) + " \n"
            views = "Total Views: " + str(result['views']) + " \n"
            rating = "Rating: " + str(result['rating']['bayesian']) + " \n"
            search_result = title + authors + artists + genre + chapters + views + rating
            main_cover = result['mainCover']
            paragraph = result['description'].split('\n')
            paragraph = paragraph[0]
            if (len(paragraph) > 250):
                synopsis = paragraph[0:250] + "..."
            else:
                synopsis = paragraph[0:250]

            # set the variables
            self.manga_info = search_result
            self.manga_cover = main_cover
            self.manga_synopsis = synopsis

            return True
        else:
            return False