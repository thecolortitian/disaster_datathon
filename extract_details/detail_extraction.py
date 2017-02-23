import pandas as pd
import time
import json
#from requests import Session
import urllib
import geocode
import nltk


with open('1275_guardian.json') as data_file:    
    d = json.load(data_file)

data = []
flood_words = ["flood"]

for article in d:
	title = article["title"]
	if "flood" in title:
		flood_articles.append(article)

for t in times:
	for article in data:
		content = article["content"].split(" ") #creates a list of all words in article
		if t in content:
			print("RECENT")
		
