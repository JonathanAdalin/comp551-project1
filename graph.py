import os
import re

output_location = 'out/'
output_file = 'adalin-burgett-scott_spa.xml'

with open(os.path.join(output_location, output_file), 'r') as output_file:
    content = output_file.read()
    utterances = re.findall('\"1\">.*?</', content)

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

print "<10 " + str(count["<10"])
print "<20 " + str(count["<20"])
print "<30 " + str(count["<30"])
print "<40 " + str(count["<40"])
print "<50 " + str(count["<50"])
print ">50 " + str(count[">50"])
