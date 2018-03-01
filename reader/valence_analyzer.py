import json
import string
import unicodedata
import csv
from empath import Empath

with open('1000.json', 'r') as f:
	post_bank = json.loads(f.read())

with open('1000_rank.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	lexicon = Empath()
	count = 0
	for pid, info in post_bank.iteritems():
		print info['title']
		comments = unicodedata.normalize('NFKD', info['comment_block']).encode(
			'ascii', 'ignore').translate(None, string.punctuation)
		if (len(comments)) > 100:
			valence_score = lexicon.analyze(comments, normalize=True)['negative_emotion']
			spamwriter.writerow([valence_score, info['url']])
			count += 1

	print count