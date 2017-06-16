import praw
import config
import time
import os

print("Logging in!")
reddit = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "Pull wallpapers from /r/wallpapers")
print("Logged in successfully \o/")


topPosts = reddit.subreddit(config.subreddit).hot(limit=25)
imagePost = None
for post in topPosts:
    if imagePost is None:
        url = post.url
        if ".jpg" not in url and ".png" not in url:
            print("URL is an album or a text post. Moving on.")
            imagePost = None
        else:
            imagePost = url
            print("URL = " + imagePost)
    if imagePost is not None:
        imagepath = imagePost
        imagepath = imagepath.replace("https://i.redd.it/","")
        imagepath = imagepath.replace("http://i.imgur.com/","")
        os.system("wget -O " + config.imgDIR +imagepath+" " + imagePost)
        imagePost = None
    else:
        print("No images found.")
