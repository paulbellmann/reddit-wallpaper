# Gets current top post
# by paulbellmann

import praw
import urllib
import os.path

r = praw.Reddit(user_agent='wallpaper downloader /u/user')

def getImage(subreddit):
	submissions = r.get_subreddit(subreddit).get_top_from_day(limit=1)
	submission = submissions.next()
	# set path and file name here
	myPath = "/Users/user/Pictures/wp_" + str(submission.id) + ".jpg"

	if not os.path.isfile(myPath):
		urllib.urlretrieve(submission.url, myPath)
		print submission.title + " saved."

getImage('EarthPorn')
getImage('Wallpaper')
