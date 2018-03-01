import praw
import time
import json

with open('../data/reddit_credentials.txt', 'r') as f:
	reddit_credentials = map(lambda x: x[:-1], f.readlines())

reddit = praw.Reddit(client_id=reddit_credentials[0],
	client_secret=reddit_credentials[1],
	user_agent=reddit_credentials[2])

count = 1
timestamp = time.time() # DEBUG: - 24 * (3600 * 24)
post_bank = {}
for i in range(365):
	for submission in reddit.subreddit('design_critiques').submissions(
		timestamp - (3600 * 24), timestamp):
		post_bank[submission.id] = {
			'title': submission.title,
			'url': submission.url,
			'comment_block': ''}
		for c in submission.comments.list():
			if hasattr(c, 'body'):
				post_bank[submission.id]['comment_block'] += c.body + ' '
		print count
		count += 1
	timestamp -= 3600*24
	print 'day ' + str(i)
	if count >= 1000:
		break
	time.sleep(1)

with open('1000.json', 'w') as f:
	json.dump(post_bank, f)