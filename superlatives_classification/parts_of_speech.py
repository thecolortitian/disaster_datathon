# Jo Munson, 2017
# Disaster_Datathon
# verb, noun, adjective, adverb extractor

# -*- coding: utf-8 -*-

import nltk
import json

f = '851_guardian_files.json'

guardian = json.loads(f)
text = nltk.word_tokenize('No person has been more influential in the reduction of narcissism than James Paris, born in Leeds.')
token = nltk.pos_tag(text)

