import os
import re
import operator
from itertools import izip

output_location = './'
output_file = 'adalin-burgett-scott_spa.xml'

with open(os.path.join(output_location, output_file), 'r') as output_file:
    content = output_file.read()
    utterances = re.findall('[0-9]\">(.*?)</utt', content)

print "\nUtterances: " + str(len(utterances))

# Words per utterance

count = {"<10":0, "<20":0, "<30":0, "<40":0, "<50":0, ">50": 0}
for utterance in utterances:
    word_count = len(utterance.split())
    if word_count < 10:
        count["<10"] += 1
    elif word_count < 20:
        count["<20"] += 1
    elif word_count < 30:
        count["<30"] += 1
    elif word_count < 40:
        count["<40"] += 1
    elif word_count < 50:
        count["<50"] += 1
    else:
        count[">50"] += 1

print "\nWord count distribution per utterance"

print "<10 " + str(count["<10"])
print "<20 " + str(count["<20"])
print "<30 " + str(count["<30"])
print "<40 " + str(count["<40"])
print "<50 " + str(count["<50"])
print ">50 " + str(count[">50"])

# Most popular words

d = {}
for utterance in utterances:
    words = utterance.split()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
sorted_d = sorted(d.items(), key=operator.itemgetter(1))

print "\nMost used words"
for i in range(len(sorted_d) - 10, len(sorted_d)):
    print sorted_d[i]

# Most popular phrases

d = {}
for utterance in utterances:
    words = utterance.split()
    phrases = [' '.join(pair) for pair in izip(words[:-1], words[1:])]
    for phrase in phrases:
        if phrase in d:
            d[phrase] += 1
        else:
            d[phrase] = 1
sorted_d = sorted(d.items(), key=operator.itemgetter(1))

print "\nMost used phrases"
for i in range(len(sorted_d) - 20, len(sorted_d)):
    print sorted_d[i]
