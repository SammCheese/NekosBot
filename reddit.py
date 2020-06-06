import os,json,random,requests,io,praw

r=praw.Reddit(client_id='',
				   client_secret='',
				   password='',
				   user_agent='',
				   username='')


with open('config.json','r') as configFile:
	config=json.load(configFile)

class Reddit_API:
    def __init__(self,chosensubreddit):
        self.chosensubreddit=chosensubreddit

    def get_submissions(self,chosensubreddit):
        chosensubreddit=chosensubreddit.lower()
        image_subreddit=r.subreddit(chosensubreddit)
        image_submissions=image_subreddit.hot(limit=20)
        image_urls=[]
        for i in image_submissions:
            image_url=i.url
            if image_url.endswith('.png') or image_url.endswith('.jpg') or image_url.endswith('.jpeg'):    
                image_urls.append(image_url)
        return image_urls
        
    def GET_image(self,image_urls):
        url=random.choice(image_urls)
        form=url[-4:]                        # Grab the format
        GETimage=requests.get(url)
        if GETimage.status_code==200:
            Image=io.BytesIO(GETimage.content)
        
        reddit_Image_name=str(random.randint(0,100))
        return form,Image,reddit_Image_name
