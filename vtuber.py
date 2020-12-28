import requests
import json
import os

from urllib.parse import urlencode
from datetime import datetime

class VTuber():
    # dictionary of VTuber's YT ID with their aliases
    vtuber_ids = {
                'UCp6993wxpyDPHUpavwDFqgg': ['tokino', 'sora', 'tokino sora', 'sora-chan', 'tokino soda'],
                'UCDqI2jOz0weumE8s7paEk6g': ['roboco', 'roboko', 'roboco-san', 'roboko-san'],
                'UC5CwaMl1eIgY8h02uZw7u8A': ['hoshimachi', 'suisei', 'hoshimachi suisei', 'sui-chan'],
                'UC-hM6YJuNYVAmUWxeIr9FeA': ['sakura', 'miko', 'sakura miko', 'mikochi', 'miko-chan'],
                'UC0TXe_LYZ4scaW2XMyi5_kw': ['azki', 'azuki'],
                'UCD8HOxPs4Xvsm8H0ZxXGiBw': ['yozora', 'mel', 'yozora mel'],
                'UCdn5BQ06XqgXoAxIhbqw5Rg': ['shirakami', 'fubuki', 'shirakami fubuki', 'foob'],
                'UC1CfXB_kRs3C-zaeTG3oGyg': ['akai', 'haato', 'akai haato', 'haachama', 'haa-chama'],
                'UCFTLzh12_nrtzqBPsTCqenA': ['aki', 'rosenthal', 'aki rosenthal', 'akirose', 'akiroze'],
                'UCQ0UDLQCjY0rmuxCDE38FGg': ['natsuiro', 'matsuri', 'natsuiro matsuri'],
                'UC1opHUrw8rvnsadT-iGp7Cg': ['minato', 'aqua', 'minato aqua', 'aqua-chan', 'baqua'],
                'UCXTpFs_3PqI41qX2d9tL2Rw': ['murasaki', 'shion', 'murasaki shion', 'shion-chan'],
                'UC7fk0CB07ly8oSl0aqKkqFg': ['nakiri', 'ayame', 'nakiri ayame', 'ojou', 'ojou-chan', 'ayame-chan'],
                'UC1suqwovbL1kzsoaZgFZLKg': ['yudzuki', 'choco', 'yudzuki choco', 'choco-sensei'],
                'UCvzGlP9oQwU--Y0r9id_jnA': ['oozora', 'subaru', 'oozora subaru', 'subaww', 'duck', 'bebek'],
                'UCp-5t9SrOQwXMU7iIjQfARg': ['ookami', 'mio', 'ookami mio', 'mio-chan'],
                'UCvaTdHTWBGv3MKj3KVqJVCw': ['nekomata', 'okayu', 'nekomata okayu', 'okayun'],
                'UChAnqc_AY5_I3Px5dig3X1Q': ['inugami', 'korone', 'inugami korone', 'koro-chan', 'doog'],
                'UC1DCedRgGHBdm81E1llLhOQ': ['usada', 'pekora', 'usada pekora', 'peko'],
                'UCl_gCybOJRIgOXw6Qb4qJzQ': ['rushia', 'uruha rushia'],
                'UCCzUftO8KOVkV4wQG1vkUvg': ['houshou', 'marine', 'houshou marine', 'senchou'],
                'UCvInZx9h3jC2JzsIzoOebWg': ['shiranui', 'flare', 'shiranui flare'],
                'UCdyqAaZDKHXg4Ahi7VENThQ': ['shirogane', 'noel', 'shirogane noel', 'danchou'],
                'UC1uv2Oq6kNxgATlCiez59hw': ['tokoyami', 'towa', 'tokoyami towa', 'towa-sama'],
                'UCZlDXzGoo7d44bwdNObFacg': ['amane', 'kanata', 'amane kanata', 'ppt'],
                'UCa9Y57gfeY0Zro_noHRVrnw': ['himemori', 'luna', 'himemori luna'],
                'UCS9uQI-jC3DE0L4IpXyvr6w': ['kiryu', 'coco', 'kiryu coco', 'kaichou', 'asacoco'],
                'UCqm3BQLlJfvkTsX_hvm0UmA': ['tsunomaki', 'watame', 'tsunomaki watame'],
                'UCFKOVgVbGmX65RxO3EtH3iw': ['yukihana', 'lamy', 'yukihana lamy'],
                'UCUKD-uaobj9jiqB-VXt71mA': ['shishiro', 'botan', 'shishiro botan', 'shishiron'],
                'UCAWSyEs_Io8MtpY3m-zqILA': ['momosuzu', 'nene', 'momosuzu nene'],
                'UCK9V2B22uJYu3N7eR_BT9QA': ['omaru', 'polka', 'omaru polka', 'pol'],
                'UCOyYb1c43VlX9rc_lT6NKQw': ['ayunda', 'risu', 'ayunda risu', 'tupai'],
                'UCP0BspO_AMEe3aQqqpo89Dg': ['moona', 'hoshinova', 'moona hoshinova', 'maemuna'],
                'UCAoy6rzhSf4ydcYjJw3WoVg': ['airani', 'iofifteen', 'airani iofifteen', 'iofi', 'yopi'],
                'UCYz_5n-uDuChHtLo7My1HnQ': ['kureiji', 'ollie', 'kureiji ollie', 'zombie'],
                'UC727SQYUvx5pDDGQpTICNWg': ['anya', 'melfissa', 'anya melfissa', 'keris', 'kris'],
                'UChgTyjG-pdNvxxhdsXfHQ5Q': ['pavolia', 'reine', 'pavolia reine', 'kalkun'],
                'UCyl1z3jo3XHR1riLFKG5UAg': ['watson', 'amelia', 'watson amelia', 'ame'],
                'UCMwGHR0BTZuLsmjY_NT5Pwg': ['ninomae', 'inanis', 'ninomae inanis', 'ina', 'tako'],
                'UCoSrY_IQQVpmIRZ9Xf-y93g': ['gawr', 'gura', 'gawr gura', 'same'],
                'UCHsx4Hqa-1ORjQTh9TYDhww': ['takanashi', 'kiara', 'takanashi kiara', 'kusotori', 'chicken'],
                'UCL_qhgtOy0dy1Agp8vkySQg': ['mori', 'calliope', 'mori calliope', 'reaper', 'rapper'],                
                'UCpJtk0myFr5WnyfsmnInP-w': ['hana', 'macchia', 'hana macchia', 'hanamaki'],
                'UC5LyYg6cCA4yHEYvtUsir3g': ['uruha', 'ichinose', 'ichinose uruha', 'nose-san', 'nose-chan'],
                'UCl-3q6t6zdZwgIsFZELb7Zg': ['shirayuri', 'lily', 'shirayuri lily', 'pomaera'],                
                'UCajhBT4nMrg3DLS-bLL2RCg': ['amano', 'pikamee', 'amano pikamee', 'pika'],
                'UCrR7JxkbeLY82e8gsj_I0pQ': ['amicia', 'michella', 'amicia michella', 'cia'],
                'UCANDOlYTJT7N5jlRC3zfzVA': ['yuukoku', 'roberu', 'yuukoku roberu', 'yukoku', 'robel', 'son', 'winning son'],
                'UCMMBGMjrrWcRZmG_lW4jC-Q': ['pinocchiop', 'pinokiop', 'pino', 'pino-san'],
                'UCZ5dNZsqBjBzbBl0l_IdmXg': ['taka', 'radjiman', 'taka radjiman', 'takarajima', 'takamama'],
                'UCA3WE2WRSpoIvtnoVGq4VAw': ['zea', 'cornellia', 'zea cornellia'],
                'UCOmjciHZ8Au3iKMElKXCF_g': ['miyu', 'ottavia', 'miyu ottavia', 'otter'],
                'UCkL9OLKjIQbKk2CztbpOCFg': ['riksa', 'dhirendra', 'riksa dhirendra', 'jukut'],
                'UC8Snw5i4eOJXEQqURAK17hQ': ['rei', 'galilei', 'rei galilei', 'galileo'],
                'UCk5r533QVMgJUdWwqegH2TA': ['azura', 'cecillia', 'azura cecilla', 'zura', 'jura'],
                'UCoWH3sDpeXG1aXmOxveX4KA': ['nara', 'haramaung', 'nara haramaung', 'maung'],
                'UCyRkQSuhJILuGOuXk10voPg': ['layla', 'alstroemeria', 'layla alstroemeria'],
                'UCjFu-9GHnabzSFRAYm1B9Dw': ['etna', 'crimson', 'etna crimson'],
                'UC5qSx7KzdRwbsO1QmJc4d-w': ['siska', 'leontyne', 'sika leontyne'],
                'UCHjeZylSgXDSnor8wUnwU_g': ['bonnivier', 'pranaja', 'bonnivier pranaja', 'bobon', 'boni'],
                'UCMzVa7B8UEdrvUGsPmSgyjA': ['derem', 'kado', 'derem kado'],
                'UCijNnZ-6m8g85UGaRAWuw7g': ['nagisa', 'arcinia', 'nagisa arcinia', 'manggis'],
                'UC5yckZliCkuaEFbqzLBD7hQ': ['reza', 'avanluna', 'reza avanluna'],
                'UCKeAhJvy8zgXWbh9duVjIaQ': ['arurandis', 'aruran', 'pizza'],
                'UC9mf_ZVpouoILRY9NUIaK-w': ['rikka'],
                'UCD-miitqNY3nyukJ4Fnf4_A': ['tsukino', 'mito', 'tsukino mito', 'iinchou'],
                'UCdpUojq0KWZCN9bxXnZwz5w': ['ars', 'almal', 'ars almal'],
                'UCHK5wkevfaGrPr7j3g56Jmw': ['miyako', 'seto miyako', 'setomiya', 'myako'],
                'UCiMG6VdScBabPhJ1ZtaVmbw': ['kaga nazuna', 'nazuna', 'nazu-chan', 'nazu'],
                'UCIu-aUArYq_H84dBpCAokMA': ['shirayuki reid', 'reid', 'reido', 'reido-kun', 'reid-kun'],
                'UC0g1AE0DOjBYnLhkgoRWN1w': ['honma', 'himawari', 'honma himawari', 'honhima', 'hima-chan'],
                }

    def __init__(self, vtuber_name, yt_key):
        self.vtuber_name = vtuber_name.lower()
        self.yt_key = yt_key

    def get_id_by_aliases(self):
        keyName = "NA"
        for id, aliases  in self.vtuber_ids.items():
            if self.vtuber_name in aliases:
                keyName = id
        return  keyName

    def get_info(self):
        channel_id = self.get_id_by_aliases()
        if channel_id == "NA":
            return("Sorry, I don't know who " + self.vtuber_name + " is...")
        else:
            query = {
                    'key': self.yt_key,
                    'part': 'snippet',
                    'channelId': channel_id,
                    'maxResults': 1,
                    'order': 'date'
            }
            response = requests.get("https://www.googleapis.com/youtube/v3/search?" + urlencode(query))
            json_data= json.loads(response.text)
            if json_data['items']:
                item = json_data['items'][0]
                channel_title = item['snippet']['channelTitle'] + "'s latest video: \n\n"
                video_title = item['snippet']['title'] + " \n"
                video_url = "https://youtu.be/" + item['id']['videoId'] + " \n"
                broadcast_type = item['snippet']['liveBroadcastContent']
                publish_time = "Published: " + str(datetime.strptime(item['snippet']['publishTime'], "%Y-%m-%dT%H:%M:%SZ")) + "GMT \n"
                if broadcast_type == "none":
                    broadcast_type = "Status: archive \n"
                else:
                    broadcast_type = "Status: *" + broadcast_type + "* \n"
                return(channel_title + video_title + publish_time + broadcast_type + video_url)
            else:
                return("Sorry, I can't find anything on " + self.vtuber_name + "'s channel~")
