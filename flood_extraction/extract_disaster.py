
# coding: utf-8

# In[34]:

import pandas as pd
import json
import urllib2
import re


# In[99]:

#path = 'http://recoin.cloudapp.net/data/news_theguardian.json'
#path ='Git/disaster_datathon/floods.json'
path ='851_guardian_files.json'
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


# In[76]:

term_file = 'FloodTerms.txt'
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
#print gw
#print "|".join(gw)
#print "|".join(fw)


# In[108]:

#terms = ['disaster','flood','earthquake', 'More']

#terms_re = "|".join(terms)
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
for i in xrange(len(match_cont)) :
    cnt_title = match_title[i][0]+match_title[i][1]
    cnt_cont = match_cont[i][0] + match_cont[i][1]
    if cnt_title+cnt_cont > 10:
        print i,match_title[i],match_cont[i]
        print df.ix[i]
    #print len(re.findall("|".join(gw),cont))

