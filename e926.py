import requests, random, io, json


class e926_class:
    def __init__(self, tags):
        if tags == "random":
            self.tags = ""
        else:
            self.tags = '+'.join(tags)


    def get_urls(self, PID):
        urls = []
        headers = {
            "Host": "e926.net",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "close",
            "Cookie": "__cfduid=d9e7c47b7c23872a3d5cff5dfd1f55c2b1559494392; blacklist_avatars=true; blacklist_users=false;e621=BAh7BjoPc2Vzc2lvbl9pZCIlYjQ4OTNmMTBkZTgyZmUzYTQ1ZTI5N2NkZWVlN2E4MDE%3D--2e6ebc8a41d4c77b41c43d92e39706bcd7e83e43",
            "Upgrade-Insecure-Requests": "1",
            "If-None-Match": "W/\"5eb88240b11c702440fd0b69a981cd4b\"",
            "Cache-Control": "max-age=0"
        }

        url = f"https://e926.net/post/index.json?page={PID}&tags={self.tags}"

        request = requests.get(url, headers=headers)
        data = request.json()

        try:
            for i in range(len(data)):
                urls.append(data[i]["file_url"])
            image_url = random.choice(urls)
        except IndexError:
            image_url = "Error"

        return(image_url)


    def get_image(self, url):
        GETimage = requests.get(url)
        Image = io.BytesIO(GETimage.content)
        return(Image)