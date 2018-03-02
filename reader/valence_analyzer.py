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
		for comm in info['comment_bank']:
			comment = unicodedata.normalize('NFKD', comm).encode('ascii', 'ignore').translate(None, string.punctuation)
		if (len(comment)) > 50:
			valence_score = \
				lexicon.analyze(comment, normalize=True)['negative_emotion'] \
				- lexicon.analyze(comment, normalize=True)['positive_emotion']
			spamwriter.writerow([valence_score, info['url'], comment[:20]])
			count += 1

	print count