import requests
import json
from datetime import datetime

class ApiLokal():
    now = datetime.now() # current date and time

    cur_date = now.strftime("%Y-%m-%d")

    def jadwal_sholat(self):
        url = "https://api.banghasan.com/sholat/format/json/jadwal/kota/667/tanggal/" + self.cur_date
        response = requests.get(url)
        json_data= json.loads(response.text)
        if json_data['jadwal']:
            jadwal = json_data['jadwal']['data']
            title = "Jadwal Sholat Wilayah Jakarta \n"
            tanggal = jadwal['tanggal'] + "\n\n"
            sholat_pagi = "Imsak: " + jadwal['imsak'] + "\n" + "Subuh: " + jadwal['subuh'] + "\n" + "Terbit: " + jadwal['terbit'] + "\n" + "Dhuha: " + jadwal['dhuha'] + "\n"
            sholat_sore = "Dzuhur: " + jadwal['dzuhur'] + "\n" + "Ashar: " + jadwal['ashar'] + "\n" + "Maghrib: " + jadwal['maghrib'] + "\n" + "Isya: " + jadwal['isya'] 
            string_jadwal = title + tanggal + sholat_pagi + sholat_sore
            return(string_jadwal)        
    
    def instagram_media(self, ig_url):
        api_url = "http://sosmeeed.herokuapp.com:80/api/instagram/media"
        ig_url = ig_url.split("/")
        ig_short_code = ig_url[4]
        response = requests.post(api_url, {'shortcode':ig_short_code})
        json_data= json.loads(response.text)
        if json_data['success']:
            text = ' '.join(json_data['data']['hashtags'])
            isi_gambar = list()
            isi_video = ""
            for media in json_data['data']['medias']:
                if media['type'] == 'image':
                    media_url = media['url']
                    isi_gambar.append(media_url)
                elif media['type'] == 'video':
                    media_url = media['url']
                    isi_video = media_url

            if len(isi_gambar) > 0:
                ig_dict = {
                    "text": text,
                    "gambar": isi_gambar
                    }
                return ig_dict
            elif len(isi_video) > 0:
                ig_dict = {
                    "text": text,
                    "video": isi_video
                    }
                return ig_dict
