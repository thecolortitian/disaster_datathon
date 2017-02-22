with open('positive_words.txt') as f:
    raw = f.readlines()

for i in range(len(raw)):
    raw[i] = raw[i].split(',')

raw = [item for sublist in raw for item in sublist]

for i in range(len(raw)):
    raw[i] = raw[i].strip(' ').strip('\n').strip('\xc2\xa0').split('\xe2\x80\x93')

raw = [item for sublist in raw for item in sublist]

print(raw)

for r in raw:
    print(r)