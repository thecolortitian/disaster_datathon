import webbrowser
import pandas as pd
import time
import json
import urllib.request
import math
import re
import nltk
from nltk.tokenize import sent_tokenize

f = open('dashboard.html','w')
towns_and_cities = []
countries = []

with open('../location_extraction/uk_towns_and_cities.txt') as towns_and_cities_file:    
    read_data = towns_and_cities_file.read()
towns_and_cities=[re.sub(r'\(.+?\)\s*', '', x) for x in read_data.split("\n") if len(x) > 0]
towns_and_cities_file.close()

with open('../location_extraction/countries.txt') as countries_file:    
    countries = countries_file.read()
countries = [z.replace(" {Republic}", "") for z in countries.split("\n")]
countries_file.close()

def extract_location(title,content):
	dictionary = {}	
	most_affected_places = {}
	dictionary[title] = []
	new_content = content.replace(".", "").replace(",", "").split(" ") + title.split(" ")
	caps = [i for i in new_content if i.istitle()]

	for word in caps:
		index_of_word = caps.index(word)
		if caps[index_of_word - 1] + " " + word in content:
			word = caps[index_of_word - 1] + " " + word 
		elif (index_of_word+1) < len(caps) and word + " " + caps[index_of_word + 1]  in content:
			word = caps[index_of_word - 1] + " " + word 
	for word in caps:
		if word in towns_and_cities:
			if word in towns_and_cities: 
				most_affected_places = __add_to_dict_if_not_in(most_affected_places, str(word))
		elif word in countries:
			if word in most_affected_places:
				most_affected_places = __add_to_dict_if_not_in(most_affected_places, str(word))

	list_of_lists  = [[k, most_affected_places[k]] for k in most_affected_places]
	
	list_of_lists = sorted(list_of_lists, key = lambda x: (-x[1]))
	dictionary[title] = [x[0] for x in list_of_lists]
	
	return dictionary

def __add_to_dict_if_not_in(dictionary, word):
	if (len(dictionary) == 0) or (word not in dictionary.keys()):
		dictionary[word] = 1
	else:
		dictionary[word] += 1

	return dictionary

def extract_number_sentences(content):
    sents = sent_tokenize(content)
    res_table = (list(map(lambda x: re.findall(r"\d+",x), sents)))
    res_sent=[]
    for j in range(len(res_table)):
        res=res_table[j]
        if len(res)>0 :
            for k in reversed(range(len(res))):
                digit=res[k]
                #print digit
                if int(digit) > 1900 and int(digit) < 2100:
                    res.pop(k)
        #print res
        if len(res) > 0:
            res_sent.append(sents[j])
    return res_sent

##################     extracting flood data         ########################
path = '../news_source_files/1275_guardian.json'
docs = json.load(open(path))
df=pd.DataFrame(docs)

term_file = '../flood_extraction/FloodTerms_filtered.txt'
gw = []
sfw = []
gfw = []
words={}
sec = ""
for line in open(term_file):
    if line.startswith('['):
        sec = line.strip()[1:-1]
    elif len(line.strip()) == 0 :
        continue
    else:
        if sec not in words:
            words[sec]=[]
        words[sec].append(line.strip().lower())
gw = words['Generic Words']
sfw = words['Specific Flooding Words']
gfw = words['Generic Flooding Words']

match_title=[]
match_cont=[]
th = 10
th_prop_cont = 0.01
th_prop_title = 0.1
for title in df['title'] : 
    matches_gw = {x for x in gw if x in title.lower()}
    matches_gfw = {x for x in gfw if x in title.lower()}
    matches_sfw = {x for x in sfw if x in title.lower()}
    match_title.append((len(matches_sfw),len(matches_gw),len(matches_gfw)))
for cont in df['content']:
    matches_gw = {x for x in gw if x in cont.lower()}
    matches_gfw = {x for x in gfw if x in cont.lower()}
    matches_sfw = {x for x in sfw if x in cont.lower()}
    match_cont.append((len(matches_sfw),len(matches_gw),len(matches_gfw)))
cnt = 0
disasters=[]


##################     creating HTML         ########################
message = """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="initial-scale=1.0, user-scalable=no">
		<title>Disaster Dashboard</title>
		<link rel="stylesheet" type="text/css" href="dashboard.css">
	</head>
	<body>
		<div id="notmap">
			<table id="tblDashboard">
				<tr id="headingRow">
					<th>Incident</th>
					<th>Severity</th>
					<th>News Links</th>
					<th>Location</th>
					<th>Stats</th>
				</tr>"""

for i in range(len(match_cont)) :
    isDisaster=False
    if match_title[i][0]+match_cont[i][0] > 0:
        isDisaster=True
    elif 'flood' in df['content'][i].lower() or 'flood' in df['title'][i].lower():
        cnt_title = match_title[i][1]+match_title[i][2]
        cnt_cont = match_cont[i][1]+match_cont[i][2]
        if cnt_title+cnt_cont > 0:
            prop_title = cnt_title*1.0/len(df['title'][i].split())
            prop_cont = cnt_cont*1.0/len(df['content'][i].split())
            if (prop_title > th_prop_title and prop_cont > th_prop_cont) or prop_cont > th_prop_cont*2:
                isDisaster=True
            elif cnt_title+cnt_cont>th:
                isDisaster=True
    if isDisaster:
        res = sorted(map(int,re.findall("20[0-1][0-9]|19[0-9][0-9]",df.ix[i]['content'])))
        publication_year = int(df.ix[i]['publication_date'].split('-')[0])
        if len(res)==0 or (publication_year-res[-1] <10 and publication_year-res[-1] >=0):
            disasters.append(i)
        location = {}
        location = extract_location(df.ix[i]['title'],df.ix[i]['content'])

        message+="""
	    		<tr>
	    			<td>Flood</td>
	    			<td><img class="traffic-light" src="images/red-traffic-light.png"/></td>
	    			<td><a target="_blank" href='""" + str(df.ix[i]['url']) + """'>""" + str(df.ix[i]['url']) + """</a</td>
	    			<td>""" + str(location[df.ix[i]['title']])[1:-1] + """</td>
					<td></td>
				</tr>"""

				#+ str(extract_number_sentences(df.ix[i]['content']))[1:-1] + 

message+="""
			</table>
		</div>
		<div id="map"></div>
		<script src="dashboard.js"></script>
	    <script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js">
	    </script>
	    <script async defer
	    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDRiLdGWV3Qt2J1YefTRe0tsCo9Ky736ks&callback=initMap">
	    </script>
	</body>
</html>
"""

f.write(message)
f.close()

#Change path to reflect file location
filename = 'file:///Users/samikanza/Documents/Datathon/disaster_datathon/public_html/' + 'dashboard.html'
webbrowser.open_new_tab(filename)
