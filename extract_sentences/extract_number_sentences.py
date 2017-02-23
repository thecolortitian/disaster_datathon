#-*- coding:utf-8 -*-

import re
from nltk.tokenize import sent_tokenize


def extract_number_sentences(content):
    sents = sent_tokenize(content)
    res_table = map(lambda x: re.findall(r"\d+",x), sents)
    res_sent=[]
    for j in xrange(len(res_table)):
        res=res_table[j]
        if len(res)>0 :
            for k in reversed(xrange(len(res))):
                digit=res[k]
                #print digit
                if int(digit) > 1900 and int(digit) < 2100:
                    res.pop(k)
        #print res
        if len(res) > 0:
            res_sent.append(sents[j])
    return res_sent
    
#print extract_number_sentences(u'At the age of nine, my cousin Chris Simpson talked of being a missionary like his Methodist great- and great-great-grandfathers. The impulse waned in religious terms but triumphed in a different field: journalism. Since his death, aged 53, from a suspected heart attack on assignment in Senegal, tributes have poured in from old hands and from younger ones whom Chris trained and helped until his sudden and unexpected death. He worked for the BBC in Angola during the 1990s civil war, in Rwanda after the 1994 genocide and in the Central African Republic and Senegal. Freelance radio, print and online work took him to a dozen other African countries where talking to ordinary people gave his writing its striking context and warmth. He was born in Perth, Scotland, and brought up in Cheltenham, where both his parents, William and Margaret (nee Briscoe), were teachers. He was educated at Cheltenham college independent school, where his father taught history, and took a degree in politics at Manchester University. He went on to study international reporting at City University, London, and cut his teeth on West Africa magazine. He then spent four years with BBC World Service radio at Bush House. Thus prepared, he began two decades of journalism from the continent he loved. He worked for the BBC for a decade. Much of his work was read by those with a particular interest in Africa, but he enjoyed many outings on BBC Radio 4’s feature programme From Our Own Correspondent. These gave rein to his wry style; Africa observed by a modern William Boot (the deceptively bumbling hero of Evelyn Waugh’s Scoop). Chris fell into things, whether a ditch or a scam involving a fake policeman, made spaghetti of computer leads and lost endless credit cards and mobiles. But, as Kate Adie said when the programme re-ran a piece in tribute, his hallmarks were “insight, sympathy, much humour and knowledge lightly worn”. He gave a voice to those too seldom heard. In terms of making a conventional name, Chris’s modesty and readiness to share information was not always in his best interest but won him a host of devoted friends. Andy Kershaw, his fellow broadcaster, finished his autobiography only because Chris gave up three weeks to interview him, asking the questions that he felt readers would want answered. Similar devotion was shown to students in West Africa, where he spent six years from 2005 training broadcasters for the United Nations Integrated Regional Information Networks. One of their many grieving Facebook posts has a line which would have delighted Chris: “More African than you, I have not known.” He is survived by his father, William, and sisters, Bridget and Gillian.')
