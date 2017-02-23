
# coding: utf-8

# In[34]:

import pandas as pd
import json
import urllib2
import re


# In[99]:

#path = 'http://recoin.cloudapp.net/data/news_theguardian.json'
#path ='Git/disaster_datathon/floods.json'
path ='../news_source_files/851_guardian_files.json'
#docs = [json.loads(l) for l in open(path)]
docs = []
#response = urllib2.urlopen(path)
idx = 0
for l in open(path):
    #print l
    docs.append(json.loads(l.strip()))
    #print docs
    #if len(docs) == 2:
    #    break

#df=pd.read_json(path)
df=pd.DataFrame(docs)
#idx = 0
#for t in df.title:
#    print idx,t
#    idx+=1
#df

#

term_file = 'FloodTerms_filtered.txt'
gw = []
sfw = []
gfw = []
words={}
#specific=False
sec = ""
for line in open(term_file):
    if line.startswith('['):
        sec = line.strip()[1:-1]
        #print sec
    #if line.strip().endswith("Words"):
    #    if 'Flooding' in line:
    #        specific = True
    #    continue
    elif len(line.strip()) == 0 :
        continue
    else:
        if sec not in words:
            words[sec]=[]
        words[sec].append(line.strip().lower())
        #if specific:
        #    fw.append(line.strip().lower())
        #else:
        #    gw.append(line.strip().lower())
gw = words['Generic Words']
sfw = words['Specific Flooding Words']
gfw = words['Generic Flooding Words']
#print gw
#print "|".join(gw)
#print "|".join(fw)


# In[108]:

#terms = ['disaster','flood','earthquake', 'More']

#terms_re = "|".join(terms)
match_title=[]
match_cont=[]
th = 10
th_prop = 0.01
for title in df['title'] : 
    matches_gw = {x for x in gw if x in title.lower()}
    matches_gfw = {x for x in gfw if x in title.lower()}
    matches_sfw = {x for x in sfw if x in title.lower()}
    match_title.append((len(matches_sfw),len(matches_gw),len(matches_gfw)))
    #print idx,len(matches_gw),len(matches_fw)
for cont in df['content']:
    matches_gw = {x for x in gw if x in cont.lower()}
    matches_gfw = {x for x in gfw if x in cont.lower()}
    matches_sfw = {x for x in sfw if x in cont.lower()}
    match_cont.append((len(matches_sfw),len(matches_gw),len(matches_gfw)))
    #print idx,len(matches_gw),len(matches_fw)
cnt = 0
for i in xrange(len(match_cont)) :
    if match_title[i][0]+match_cont[i][0] > 0:
        print i
        print df.ix[i]
    elif 'flood' in df['content'][i].lower() or 'flood' in df['title'][i].lower():
        
        cnt_title = match_title[i][1]+match_title[i][2]
        cnt_cont = match_cont[i][1]+match_cont[i][2]
        if cnt_title+cnt_cont > 0:
            prop_title = cnt_title*1.0/len(df['title'][i].split())
            prop_cont = cnt_cont*1.0/len(df['content'][i].split())
            #print i,prop_title, prop_cont
            if prop_title > 0.1 and prop_cont > th_prop:
                print i,prop_title,prop_cont
                print df.ix[i]
            if cnt_title+cnt_cont>th:
                print i,cnt_title,cnt_cont
                print df.ix[i]


