import discord
import os
import secrets
from decouple import config

# module lokal
from jikan import Jikan
from vtuber import VTuber
from mangadex import MangaDex
from tweet import Tweet
from apilokal import ApiLokal

# module interlokal
from hentai import Hentai, Format, Utils, Sort, Option
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
YT_API_KEY = os.environ['YT_API_KEY']
TWITTER_BEARER_KEY = os.environ['TWITTER_BEARER_KEY']

client = discord.Client()

robo_greeting = ["harobo", "halobo", "hellobo", "hallobo"]

@client.event
async def on_ready():
  print ('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    ori_msg = msg
    msg = msg.lower() # ignore the caps from user chat
    if any(word in msg for word in robo_greeting):
        await message.channel.send('Harobo~')

    if msg.startswith('!commands'):
        vt_command = 'Search VTuber latest video: `roboco jadwal [vtuber name]`'
        mal_command = 'Search from MAL database: `roboco mal [anime/manga/people/character] [search query]`'
        hentai_command = 'Search from nhentai database: `roboco doujin [detail/cari] [id/search query]`'
        await message.channel.send(vt_command + '\n\n' + mal_command + '\n\n' + hentai_command)
        return
    
    if msg.startswith("apakah") and msg.endswith("?"):
        jawaban = ['iya', 'nggak', 'iya banget', 'nggak banget', 'iya kali', 'nggak deh']
        await message.channel.send(secrets.choice(jawaban))
        return

    # Handles 'roboco mal' command, search the query using Jikan (MyAnimeList) API
    if msg.startswith('roboco mal'):
        msg_query = msg.split()
        if len(msg_query) < 4 :
            await message.channel.send('Please complete your search query~ \n `roboco mal [anime/manga/people/character] [your query]`')
            return 
        else:
            category = msg_query[2]
            query = msg_query[3]

            if len(msg_query) > 3 :
                for i in msg_query[4:]:
                    query = query + " " + i

            jikan_info = Jikan(category, query)
            get_info = jikan_info.get_info()
            await message.channel.send(get_info)
            return

    # Handles 'roboco jadwal sholat' command, search the query using Jikan (MyAnimeList) API
    if msg.startswith('roboco jadwal sholat') or msg.startswith('roboco jadwal shalat'):
        info_sholat = ApiLokal()
        get_info = info_sholat.jadwal_sholat()
        await message.channel.send(get_info)
        return

    # Handles 'roboco jadwal' command, get the latest video using Youtube API 
    if msg.startswith('roboco jadwal'):
        msg_query = msg.split()
        if len(msg_query) < 3 :
            await message.channel.send('Please complete your search query~ \n `roboco jadwal [vtuber name]`')
            return 
        else:
            alias = msg_query[2]
            if len(msg_query) > 2 :
                for i in msg_query[3:]:
                    alias = alias + " " + i

            vtuber_info = VTuber(alias, YT_API_KEY)
            get_info = vtuber_info.get_info()
            await message.channel.send(get_info)
            return

    # Handles 'mangadex manga title url' command, search the query using mangadex API
    if msg.startswith('https://mangadex.org/title/'):
        md_info = MangaDex(msg)
        get_info = md_info.get_info()
        if(get_info):
            embed = discord.Embed()
            embed.set_image(url=md_info.manga_cover)
            await message.channel.send(md_info.manga_info + "\n\n" + md_info.manga_synopsis, embed = embed)
            return
    
    # Handles 'roboco doujin' command, fetch data from nhentai using Hentai API 
    if msg.startswith('roboco doujin'):
        msg_query = msg.split()
        if len(msg_query) < 3 :
            await message.channel.send('Please complete your search query~ \n `roboco doujin [detail/cari] [ID/query]`')
            return 
        else:
            category = msg_query[2]
            query = msg_query[3]

            if len(msg_query) > 3 :
                for i in msg_query[4:]:
                    query = query + " " + i

            if (category == 'cari'):
                result = ""
                i = 0
                for doujin in Utils.search_by_query(query, sort=Sort.Popular):
                    i += 1
                    if i <= 5:
                        result = result + str(i) + ". ID: " + str(doujin.id) + "\n" + str(doujin) + "\n"                
                await message.channel.send(result)
                return
                
            elif (category == 'detail'):
                doujin = Hentai(query)

                tags = list()
                for ids in doujin.tag:
                    tags.append(ids.name)

                artists = list()
                for ids in doujin.artist:
                    artists.append(ids.name)

                title = "Title: " + str(doujin.title()) + "\n\n"
                artist = "Artitsts: " + ", ".join(artists) + "\n\n"
                tag = "Tags: " + ", ".join(tags)
                doujin_info = title + artist + tag
                await message.channel.send(doujin_info)
                return

            elif (category == 'detail-img'):
                doujin = Hentai(query)

                tags = list()
                for ids in doujin.tag:
                    tags.append(ids.name)

                artists = list()
                for ids in doujin.artist:
                    artists.append(ids.name)

                title = "Title: " + str(doujin.title()) + "\n\n"
                artist = "Artitsts: " + ", ".join(artists) + "\n\n"
                tag = "Tags: " + ", ".join(tags)
                doujin_info = title + artist + tag

                message_dict = {
                    'image': doujin.cover,
                    'info': doujin_info,
                }
                
                embed = discord.Embed()
                embed.set_image(url=doujin.cover)
                await message.channel.send(doujin_info, embed = embed)
                return

    # Handles 'instagram url' command, post the media with 3rd party's API
    if msg.startswith('https://www.instagram.com'):
        insta = ApiLokal()
        get_info = insta.instagram_media(ori_msg)
        if(get_info):
            cek_tipe = "gambar"
            for tipe, content in get_info.items():
                if tipe == "gambar":
                    cek_tipe = "gambar"
                elif tipe == "video":
                    # video_url = content
                    cek_tipe = "video"

            if cek_tipe == "gambar": 
                for gambar in get_info['gambar']:
                    embed = discord.Embed()
                    embed.set_image(url=gambar)
                    await message.channel.send(get_info['text'], embed = embed)
                return

            elif cek_tipe == "video":
                embed = discord.Embed()
                embed.description = "Sorry, can't show you the video!" 
                await message.channel.send(get_info['text'], embed = embed)
                return

    # Handles 'twitter with image/video url' command, post the media with twitter API
    # # ps: discord didn't really need this... this is from the LINE version of robocobot 
    # if msg.startswith('https://twitter.com/') or msg.startswith('https://mobile.twitter.com/'):
    #     tweet_data = Tweet(msg, TWITTER_BEARER_KEY)
    #     get_info = tweet_data.get_info()
    #     if(get_info):
    #         cek_tipe = "gambar"
    #         for tipe, content in get_info.items():
    #             if tipe == "gambar":
    #                 cek_tipe = "gambar"
    #             elif tipe == "video":
    #                 preview_url = get_info['text']
    #                 video_url = content
    #                 cek_tipe = "video"

    #         if cek_tipe == "gambar": 
    #             await message.channel.send(get_info)
    #             return
    #         elif cek_tipe == "video":
    #             await message.channel.send(video_url)
    #             return

client.run(DISCORD_TOKEN)
