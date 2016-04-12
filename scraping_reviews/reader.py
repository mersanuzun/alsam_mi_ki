import codecs
import json
from urllib2 import *
import urllib
import requests

data = []
fo = open('reviews.json', 'r')
reviews = json.load(fo)
output = open('logitect_comments.txt', 'a')

nlp_tools = ["spellcheck", "deasciifier", "normalize"]
#nlp_tools = ["spellcheck","deasciifier", "normalize", "Vowelizer"]
for r in reviews:
   c = r['text'].replace(',', '').encode('utf8')
   for tool in nlp_tools:
       url = "http://tools.nlp.itu.edu.tr/SimpleApi?tool=" + tool + "&input=%s&token=Ct5UbJhP4a40iygJAUxsvl6nNLqsiDPY"% c.replace(' ', '%20')
       try:
          conn = urlopen(url)
       except:
          print tool, c
       c = conn.read().strip()
       if "Invalid parameter: Usage" in c:
          break
   print c
   if tool == nlp_tools[-1]:   
      output.write(c + "\n")

