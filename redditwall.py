import praw
import config
import time
import os

#Getting OAUTH object. Configure these in config.py.
print("Trying to log in to reddit.\n")
try:
    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Pull wallpapers from /r/wallpapers")
except exception:
    print(exception)
print("Logged in successfully.\n")


topPosts = reddit.subreddit(config.subreddit).hot(limit=config.imagelimit)

#Variable to make sure it's an imagepost and not a text post or an album.
imagePost = None

for post in topPosts:
    if imagePost is None:
        url = post.url

#wget the url only if it has ".jpg" or ".png" in it.
        if ".jpg" not in url and ".png" not in url:

            print("URL is an album or a text post. Moving on.")
            imagePost = None

        else:

            imagePost = url
            print("URL = " + imagePost)

    if imagePost is not None:

#save it with the name given by the image host.
        imagepath = imagePost
        imagepath = imagepath.replace("https://i.redd.it/","")
        imagepath = imagepath.replace("http://i.imgur.com/","")

        os.system("wget -O " + config.imgDIR + "/" +imagepath+" " + imagePost)

        imagePost = None
    else:

        print("No images found.")
