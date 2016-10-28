# Gets current top post
# by paulbellmann

import praw
import urllib
import os.path

r = praw.Reddit(user_agent='wallpaper downloader /u/pwneed')

def getImage():
	submissions = r.get_subreddit('wallpaper').get_top_from_day(limit=1)
	submission = submissions.next()
	# set path and file name here
	myPath = "/home/pi/Pictures/Wallpaper/wp_" + str(submission.id) + ".jpg"

	if not os.path.isfile(myPath):

getImage()
