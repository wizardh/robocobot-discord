import requests
import json
import os

from urllib.parse import urlencode
from datetime import datetime

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

class Tweet():
    media_type = ""

    def __init__(self, url, bearer_key):
        self.tweet_url = url
        self.bearer_key = bearer_key

    def get_info(self):
        url_parts = self.tweet_url.split('/')
        tweet_id = url_parts[5]
        api_url = "https://api.twitter.com/1.1/statuses/show.json?include_entities=true&tweet_mode=extended&id="
        response = requests.get(api_url + tweet_id, auth=BearerAuth(self.bearer_key))            
        json_data= json.loads(response.text)
        
        if json_data['extended_entities']:
            text = json_data['full_text']
            includes = json_data['extended_entities']
            isi_gambar = list()
            isi_video = ""
            for media in includes['media']:
                if media['type'] == 'photo':
                    media_url = media['media_url_https']
                    isi_gambar.append(media_url)
                if media['type'] == 'video' or media['type'] == 'animated_gif':
                    raw_url = media['video_info']['variants'][0]['url']
                    media_url = raw_url.split('?')
                    isi_video = media_url[0]
                    text = media['media_url_https']
            
            if len(isi_gambar) > 0:
                tweet_dict = {
                    "text": text,
                    "gambar": isi_gambar
                    }
                return tweet_dict
            elif len(isi_video) > 0:
                tweet_dict = {
                    "text": text,
                    "video": isi_video
                    }
                return tweet_dict
            
