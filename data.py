subreddit_list = ['animemes', 'manga', 'animenocontext', 'animebikinis', 'animegifs', 'animeow_irl', 'animephonewallpapers', 'animesketch', 'animevectorwallpapers', 'animewallpaper', 'anime_faces', 'ANI_COMMUNISM', 'AskAnime', 'awwnimate', 'bannedfromanime_irl', 'BokuNoHeroAcademia', 'CuteLittleFangs', 'DDLC', 'DoritoHair', 'droppedanime', 'ecchi', 'endcard', 'existentialanime', 'ftfanime', 'hentai_irl', 'JapaneseASMR', 'lightnovels', 'loli_irl',
                  'Manga_Collection', 'metaanime', 'Moescape', 'monogatariplot', 'nihilate', 'noveltranslations', 'pantsu', 'patchuu', 'PockyKiss', 'porn_irl', 'pouts', 'qualityanime', 'roboragi', 'shorthairedwaifus', 'smugs', 'StitchesOfAnime', 'SUBSFUCKINGWHERE', 'toomeirlforanime_irl', 'trashwaifus', 'trueanime', 'TwoDeeArt', 'UQHolder', 'WaifuForLaifu', 'WaifusForTrump', 'watchinganime', 'weeabootales', 'WhatAWeeb', 'wholesomeyaoi', 'wholesomeyuri', 'yuri', 'yshirt']

# Add wholesomeanimemes after September 10
# Add hentai after August 11

# keyphrase
sauce_request = r"((w+h+a*t+ *)|(w+h+e+r+e *))+('*i*s+ *)*(t+h+e+ *)*(a+n+i+m+e+s* *)*(s+a+u+c+e+s*)|(s+a+u+c+e+s*\?+)|^(s+a+u+c+e+s*)$"

# sauce provided by OP checker
sauce_provided_regex = r"((t+h+i+s+ *)|(h+e+r*e+ *))+('*i*s+ *)*(t+h+e+ *)*(s+a+u+c+e+)|(!+s+a+u+c+e+)|^(s+a+u+c+e+:)"

# sauce request checker
sauce_regex = r"([\{]+[A-Za-z0-9-:/!? ]+[\}]+)|([\]]+[A-Za-z0-9-:/!? ]+[\[]+)|([\<]+[A-Za-z0-9-:/!? ]+[\>]+)|([\|]+[A-Za-z0-9-:/!? ]+[\|]+)|([\(]+[0-9]{1,7}[\)]+)"


bots = ['Roboragi', 'nHentaiTagBot']

sauce_reply = "Thank you for providing sauce! I will ensure that it is passed on to anyone who asks for it in the comments later on. This subreddit needs more people like you! Arigato!!"

default_replies = [
    '''Konnichiwa! No one has provided the sauce so far.


___
^(If you are seeing this message and know the sauce, please reply with the sauce by either using [u/Roboragi tags](https://www.reddit.com/r/Roboragi/wiki/index#wiki\_how\_do\_i\_use\_it.3F) or writing 'sauce:' followed by the description you want. I will deliver it to anyone who asks for it on this submission in the future.)''',
    '''Ohiyo!! No one has provided the sauce so far.


___
^(If you are seeing this message and know the sauce, please reply with the sauce by either using [u/Roboragi tags](https://www.reddit.com/r/Roboragi/wiki/index#wiki\_how\_do\_i\_use\_it.3F) or writing 'sauce:' followed by the description you want. But it's not like I want you to give sauce or anything ba-BAKA!! >.<)''',
    '''Yare yare daze, no one has provided the sauce using bots so far.


___
^(If you are seeing this message and know the sauce, please reply with the sauce by either using [u/Roboragi tags](https://www.reddit.com/r/Roboragi/wiki/index#wiki\_how\_do\_i\_use\_it.3F) or writing 'sauce:' followed by the description you want so that I can give the damn sauce to any annoying bitch that asks for it in the future)'''
]
