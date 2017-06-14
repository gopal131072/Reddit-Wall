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

topPosts = reddit.subreddit('animewallpaper').top(limit=10)
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
        os.system("wget " + imagePost)
        imagePost = None
    else:
        print("No images found.")
