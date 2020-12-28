import time

# dictionary of VTuber's YT ID with their aliases
vtuberIDs ={'UCp6993wxpyDPHUpavwDFqgg': ['tokino', 'sora', 'tokino sora', 'sora-chan', 'tokino soda'],
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
            'UC7fk0CB07ly8oSl0aqKkqFg': ['nakiri', 'ayame', 'nakiri ayame', 'ayame-chan'],
            'UC1suqwovbL1kzsoaZgFZLKg': ['yudzuki', 'choco', 'yudzuki choco', 'choco-sensei'],
            'UCvzGlP9oQwU--Y0r9id_jnA': ['oozora', 'subaru', 'oozora subaru', 'subaww', 'duck'],
            'UCp-5t9SrOQwXMU7iIjQfARg': ['ookami', 'mio', 'ookami mio', 'mio-chan'],
            'UCvaTdHTWBGv3MKj3KVqJVCw': ['nekomata', 'okayu', 'nekomata okayu', 'okayun'],
            'UChAnqc_AY5_I3Px5dig3X1Q': ['inugami', 'korone', 'inugami korone', 'koro-chan'],
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
            }

def getIDByAliases(namesDict, query):
    start_time = time.time()
    keyName = False

    for id, aliases  in namesDict.items():
        if query in aliases:
            keyName = id

    print("--- %s seconds ---" % (time.time() - start_time))
    return  keyName

cari = str(input("Cari ID VTuber Hololive: "))
result = getIDByAliases(vtuberIDs, cari.lower())
print(result)
