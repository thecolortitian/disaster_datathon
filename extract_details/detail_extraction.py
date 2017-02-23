
import json



with open('1275_guardian.json') as data_file:    
    d = json.load(data_file)

data = []
flood_words = ["flood"]

for article in d:
	title = article["title"]
	if "flood" in title:
		data.append(article)


times = ["yesterday", "today", "this morning"]

for t in times:
	for article in data:
		content = article["content"].split(" ") #creates a list of all words in article
		if t in content:
			print("RECENT")
		
