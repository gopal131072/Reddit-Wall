# Reddit-Wall
Small script to pull wallpapers(or any images really) from a required subreddit.

## Dependencies
1. PRAW which is the python reddit api wrapper. Use the following command to install it with pip.
```
pip install praw
```
2. [wget](http://wget.addictivecode.org/Faq.html#download) to download the images.

## Instructions
1. Clone this repo.
2. Edit config.py to enter your own OAUTH credentials, point it to the subreddit you want, the directory
   where you want to store your files and the limit on the number of posts to scan.
3. In redditwall.py where topPosts is initialized decide how to sort the posts.(Default is hot.)
4. Run redditwall.py.
