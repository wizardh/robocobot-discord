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