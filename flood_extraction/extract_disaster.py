
# coding: utf-8

import pandas as pd
import json
import urllib2
import re


#path ='../news_source_files/851_guardian_files.json'
path = '../news_source_files/1275_guardian.json'
docs = json.load(open(path))
#docs = [json.loads(l) for l in open(path)]
df=pd.DataFrame(docs)

term_file = 'FloodTerms_filtered.txt'
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
th_prop_cont = 0.001
th_prop_title = 0.05
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
for i in xrange(len(match_cont)) :
    isDisaster=False
    if match_title[i][0]+match_cont[i][0] > 0:
        #print i
        #print df.ix[i]
        isDisaster=True
        #disasters.append(i)
    elif 'flood' in df['content'][i].lower() or 'flood' in df['title'][i].lower():
        cnt_title = match_title[i][1]+match_title[i][2]
        cnt_cont = match_cont[i][1]+match_cont[i][2]
        if cnt_title+cnt_cont > 0:
            prop_title = cnt_title*1.0/len(df['title'][i].split())
            prop_cont = cnt_cont*1.0/len(df['content'][i].split())
            #print i,prop_title, prop_cont
            if (prop_title > th_prop_title and prop_cont > th_prop_cont) or prop_cont > th_prop_cont*2:
                #print i,prop_title,prop_cont,cnt_title,cnt_cont
                #print df.ix[i]
                isDisaster=True
            elif cnt_title+cnt_cont>th:
                #print i,cnt_title,cnt_cont,prop_title,prop_cont
                #print df.ix[i]
                isDisaster=True
    if isDisaster:
        res = sorted(map(int,re.findall("20[0-1][0-9]|19[0-9][0-9]",df.ix[i]['content'])))
        publication_year = int(df.ix[i]['publication_date'].split('-')[0])
        if len(res)==0 or (publication_year-res[-1] <10 and publication_year-res[-1] >=0):
            disasters.append(i)
print disasters
"""            
conts = df.iloc[disasters]['content']
idx = 0
for cont in conts:
    res = sorted(map(int,re.findall("20[0-1][0-9]|19[0-9][0-9]",cont)))
    selected=df.ix[disasters[idx]]
    publication_year = int(selected['publication_date'].split('-')[0])
    if len(res)==0 or (publication_year-res[-1] <10 and publication_year-res[-1] >=0):
        print selected['_id'],selected['publication_date'],res
    #else:
    #    print selected
    idx+=1
print idx
"""
