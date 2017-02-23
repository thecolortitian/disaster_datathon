# write-html-2-mac.py
import webbrowser
import pandas as pd
import json
import urllib2
import re

f = open('dashboard.html','w')
path ='../flood_extraction/851_guardian_files.json'
docs = []

idx = 0
for l in open(path):
    #print l
    docs.append(json.loads(l.strip()))

df=pd.DataFrame(docs)

term_file = '../flood_extraction/FloodTerms.txt'
gw = []
fw = []
specific=False
for line in open(term_file):
    if line.strip().endswith("Words"):
        if 'Flooding' in line:
            specific = True
        continue
    elif len(line.strip()) == 0 :
        continue
    else:
        if specific:
            fw.append(line.strip().lower())
        else:
            gw.append(line.strip().lower())

match_title=[]
match_cont=[]
idx = 0
for title in df['title'] : 
    matches_gw = {x for x in gw if x in title}
    matches_fw = {x for x in fw if x in title}
    match_title.append((len(matches_gw),len(matches_fw)))
    #print idx,len(matches_gw),len(matches_fw)
    idx+=1 
idx = 0
for cont in df['content']:
    matches_gw = {x for x in gw if x in cont}
    matches_fw = {x for x in fw if x in cont}
    match_cont.append((len(matches_gw),len(matches_fw)))
    #print idx,len(matches_gw),len(matches_fw)
    idx+=1

message = """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Disaster Dashboard</title>
		<link rel="stylesheet" type="text/css" href="dashboard.css">
	</head>
	<body>
		<div id="mainDiv">
			<table id="tblDashboard">
				<tr id="headingRow">
					<th>Incident</th>
					<th>Severity</th>
					<th>News Links</th>
					<th>Location</th>
					<th>Resiliance</th>
				</tr>"""

for i in xrange(len(match_cont)) :
    cnt_title = match_title[i][0]+match_title[i][1]
    cnt_cont = match_cont[i][0] + match_cont[i][1]
    if cnt_title+cnt_cont > 10:
    	message+="""
    		<tr>
    			<td>Flood</td>
    			<td>Serious</td>
    			<td><a target="_blank" href='""" + str(df.ix[i]['url']) + """'>""" + str(df.ix[i]['url']) + """</a</td>
    			<td>Location</td>
				<td>Resiliance</td>
			</tr>"""

message+="""
			</table>
		</div>
	</body>
</html>
"""

f.write(message)
f.close()

#Change path to reflect file location
filename = 'file:///Users/samikanza/Documents/Datathon/disaster_datathon/public_html/' + 'dashboard.html'
webbrowser.open_new_tab(filename)