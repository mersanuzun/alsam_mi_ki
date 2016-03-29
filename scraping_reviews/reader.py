import codecs
import json
data = []
fo = open('reviews.json', 'r')
a = json.load(fo)
for r in a:
   print "subject", r['subject'].encode('utf8')
   print "comment", r['text'].encode('utf8')
