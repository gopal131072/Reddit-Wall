# Reddit-Wall
Small script to pull wallpapers from a required subreddit periodically.

## Dependencies
1. PRAW which is the python reddit api wrapper. Use the following command to install it with pip.
```
pip install praw
```
2. wget to download the images. You can get it from your appropriate package manager.

## Instructions
1. Clone this repo.
2. Edit config.py to enter your own OAUTH credentials.
3. Edit config.py to point to the subreddit you want and the directory
   where you want to store your files followed by a '/'.
4. Run redditwall.py.
