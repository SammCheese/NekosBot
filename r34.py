import requests, random, io, os
from lxml import html


class rule34_class:
    def __init__(self, tags):
        self.tags = '+'.join(tags)

    def get_urls(self, page_number):
        url_list = []
        base_url = f"https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags={self.tags}&pid={page_number}"
        index_page = requests.get(base_url)
        xml = html.fromstring(index_page.content)

        urls = xml.xpath("//post/@file_url")

        for url in urls:
            url_list.append(url)

        try:
            url = random.choice(url_list)
        except IndexError:
            url = "Error"
        return(url)

    def get_image(self, url):
        GETimage = requests.get(url)
        Image = io.BytesIO(GETimage.content)
        return(Image)