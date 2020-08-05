subreddit_list = ['animemes', 'manga', 'anime_irl',
                  'animesuggest', 'animenocontext', 'animebikinis', 'animegifs', 'animeow_irl', 'animephonewallpapers', 'animesketch', 'animevectorwallpapers', 'animewallpaper', 'anime_faces', 'ANI_COMMUNISM', 'AskAnime', 'awwnimate', 'awwnime', 'bannedfromanime_irl', 'BokuNoHeroAcademia', 'CuteLittleFangs', 'DDLC', 'DoritoHair', 'droppedanime', 'ecchi', 'endcard', 'existentialanime', 'ftfanime', 'hentai_irl', 'JapaneseASMR', 'lightnovels', 'loli_irl', 'Manga_Collection', 'metaanime', 'Moescape', 'monogatariplot', 'nihilate', 'noveltranslations', 'pantsu', 'patchuu', 'PockyKiss', 'porn_irl', 'pouts', 'qualityanime', 'roboragi', 'shorthairedwaifus', 'smugs', 'StitchesOfAnime', 'SUBSFUCKINGWHERE', 'toomeirlforanime_irl', 'trashwaifus', 'trueanime', 'TwoDeeArt', 'UQHolder', 'WaifuForLaifu', 'WaifusForTrump', 'watchinganime', 'weeabootales', 'WhatAWeeb', 'wholesomeyaoi', 'wholesomeyuri', 'yuri', 'yshirt']

# Add wholesomeanimemes after September 10
# Add hentai after August 11

# keyphrase
sauce_request = r"(w+h+a*t+ *)+('*i*s+ *)*(t+h+e+ *)*(s+a+u+c+e+s*)|(s+a+u+c+e+s*\?+)|^(s+a+u+c+e+s*)$"

# sauce checker
sauce_regex = r"([\{]+.+?[\}]+)|([\]]+.+?[\[]+)|([\<]+.+?[\>]+)|([\|]+.+?[\|]+)|([\(]+[0-9]{,7}[\)]+)"
sauce_keyword = r"!sauce"

bots = ['Roboragi', 'nHentaiTagBot']

default_replies = [
    "Konnichiwa! No one has provided the sauce using bots so far. If you are seeing this message and know the sauce, please reply with the sauce enveloped inside {}, <>, ||, (), or ][ ([a detailed explanation](https://www.reddit.com/r/Roboragi/wiki/index#wiki_how_do_i_use_it.3F)) so that I can automatically provide the sauce to any user who asks for it in the future.",
    "Ohiyo!! No one has provided the sauce using bots so far. If you are seeing this message and know the sauce, please reply with the sauce enveloped inside {}, <>, ||, (), or ][ ([a detailed explanation.](https://www.reddit.com/r/Roboragi/wiki/index#wiki_how_do_i_use_it.3F)) But it's not like I want you to give sauce or anything ba-BAKA!! >.<",
    "Yare yare daze, no one has provided the sauce using bots so far. If you are seeing this message and know the sauce, reply with the sauce enveloped inside {}, <>, ||, (), or ][ ([a detailed explanation](https://www.reddit.com/r/Roboragi/wiki/index#wiki_how_do_i_use_it.3F)) so that I can give the damn sauce to any annoying bitch that asks for it in the future"
]
