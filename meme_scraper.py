import praw, requests, re, os
from PIL import Image
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='', 
        client_secret='',
        user_agent='Meme Scraper',
        username='',
        password='')

subreddit = reddit.subreddit('dankmemes')
top_posts = subreddit.top('day',limit=20)
dt = dt.datetime.today()

path = "./Memes/" + str(dt.month) + "_" + str(dt.day) + "/"
if not os.path.exists(path):
    os.makedirs(path)


for post in top_posts:
    url = (post.url)
    file_name = url.split("/")
    if len(file_name) == 0:
        file_name = re.findall("/(.*?)", url)
    file_name = file_name[-1]
    if "." not in file_name:
        file_name -= ".jpg"
    r = requests.get(url)
    if r.status_code == 200:
        f = open(path+file_name,'wb')
        f.write(r.content)
        f.close()

