# reddit-wallpaper
gets top post &amp; downloads it

Simply change your `python r.get_subreddit('yourSubredditHere')`
and `/your/path/to/wallpaper/wp_`

***

Works best if you run the script
with scheduled tasks / Crontab.

crontab example:
0 1,12,20 * * * python /home/pi/Documents/downloader.py
