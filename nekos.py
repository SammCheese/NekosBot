import os, random, requests, io

nekos_categories = {
    "femdom": "SFW",
    "tickle": "SFW",
    "ngif": "SFW",
    "erofeet": "SFW",
    "meow": "SFW",
    "erok": "SFW",
    "poke": "SFW",
    "eroyuri": "SFW",
    "kiss": "SFW",
    "8ball": "SFW",
    "lizard": "SFW",
    "slap": "SFW",
    "cuddle": "SFW",
    "goose": "SFW",
    "avatar": "SFW",
    "fox_girl": "SFW",
    "hug": "SFW",
    "gecg": "SFW",
    "pat": "SFW",
    "feet": "SFW",
    "smug": "SFW",
    "kemonomimi": "SFW",
    "holo": "SFW",
    "wallpaper": "SFW",
    "woof": "SFW",
    "baka": "SFW",
    "feed": "SFW",
    "neko": "SFW",
    "gasm": "SFW",
    "waifu": "SFW",
    "eron": "SFW",
    "erokemo": "SFW",
    "classic": "NSFW",
    "les": "NSFW",
    "hololewd": "NSFW",
    "lewdk": "NSFW",
    "keta": "NSFW",
    "feetg": "NSFW",
    "nsfw_neko_gif": "NSFW",
    "kuni": "NSFW",
    "tits": "NSFW",
    "pussy_jpg": "NSFW",
    "cum_jpg": "NSFW",
    "pussy": "NSFW",
    "lewdkemo": "NSFW",
    "lewd": "NSFW",
    "cum": "NSFW",
    "spank": "NSFW",
    "smallboobs": "NSFW",
    "Random_hentai_gif": "NSFW",
    "nsfw_avatar": "NSFW",
    "boobs": "NSFW",
    "solog": "NSFW",
    "bj": "NSFW",
    "yuri": "NSFW",
    "trap": "NSFW",
    "anal": "NSFW",
    "blowjob": "NSFW",
    "holoero": "NSFW",
    "hentai": "NSFW",
    "futanari": "NSFW",
    "solo": "NSFW",
    "pwankg": "NSFW"
}

SFW_categories = []
NSFW_categories = []

for key in nekos_categories:
    if nekos_categories[key] == "SFW":
        SFW_categories.append(key)
    elif nekos_categories[key] == "NSFW":
        NSFW_categories.append(key)
    
all_categories = SFW_categories + NSFW_categories

class nekos_class:
    def __init__(self, choice, categories):
        if choice.lower() == "random":
            self.choice = random.choice(categories)

        else:
            self.choice = choice

    def get_url(self):
        base_url = f"https://www.nekos.life/api/v2/img/{self.choice}"
        resp = requests.get(base_url)
        url = resp.json()["url"]

        return(url)

    def show_image(self, url):
        GETimage = requests.get(url)
        Image = io.BytesIO(GETimage.content)
        return(Image)