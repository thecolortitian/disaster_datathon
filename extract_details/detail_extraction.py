import pandas as pd
import time
import json
#from requests import Session
import urllib
import geocode
import nltk


with open('floods.json') as data_file:    
    data = json.load(data_file)


times = ["yesterday", "today", "this morning"]

for t in times:
	for article in data:
		content = article["content"].split(" ") #creates a list of all words in article
		if t in content:
			print("RECENT")
		