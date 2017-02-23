import pandas as pd
import time
import json
#from requests import Session
import urllib
import geocode
import re
import math

with open('uk_towns_and_cities.txt') as data_file:    
    read_data = data_file.read()
towns_and_cities=[re.sub(r'\(.+?\)\s*', '', x) for x in read_data.split("\n") if len(x) > 0]

with open('countries.txt') as f:    
    countries = f.read()
countries = [z.replace(" {Republic}", "") for z in countries.split("\n")]


def __add_to_dict_if_not_in(dictionary, word):
	if word in dictionary:
		if word not in dictionary.keys()
			dictionary[word] = 1
		else:
			dictionary[word] += 1


def extract_location(json_records):
	for article in flood_articles:
		print(article["title"])
		most_affected_places = {}
		content = article["content"].remove(".", "").remove(",", "").split(" ") + article["title"].split(" ")
		caps = [i for i in content if i.istitle()]
		for word in caps:
			if word in towns_and_cities:
				if word in towns_and_cities: 
					most_affected_places = __add_to_dict_if_not_in(most_affected_places, word)

			elif word in countries:
				if word in most_affected_places:
					most_affected_places = __add_to_dict_if_not_in(most_affected_places, word)

		print(most_affected_places)
		print()


with open('1275_guardian.json') as data_file:    
    data = json.load(data_file)

flood_articles = []
flood_words = ["flood"]

for article in data:
	title = article["title"]
	if "flood" in title:
		flood_articles.append(article)


extract_location(flood_articles)

