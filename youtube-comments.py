# Jonathan Adalin

import os
import json
from xml.sax.saxutils import escape

# Helper functions

def parse_comment_json(json_file, json_location):
    global conversation_count, formatted_content
    with open(os.path.join(json_location, json_file)) as json_file:
        comment_list = json.loads(json_file.read())
        for comment in comment_list:
            if comment['hasReplies'] == True:
                for reply in comment['replies']:
                    # Ignore recursive comments
                    if '\n' not in reply['commentText']:
                        formatted_content \
                            += '<s>' \
                            + '<utt uid="1">' \
                            + comment['commentText'] \
                            + '</utt>' \
                            + '<utt uid="2">' \
                            + reply['commentText'] \
                            + '</utt>' \
                            + '</s>\n'
                        conversation_count += 1

# Main

conversation_count = 0
formatted_content = ''
outputPath = 'out/'
outputFile = 'youtube_esp.xml'
json_location = 'json/'

json_files = os.listdir(json_location)
for json_file in json_files:
    parse_comment_json(json_file, json_location)

outputXml = open(os.path.join(outputPath, outputFile), 'w+')
# outputXml.write(formatted_content.encode('utf-8', 'ignore'))
outputXml.write(escape(formatted_content.encode('utf-8', 'ignore')))
outputXml.close()

print 'Gathered ' + str(conversation_count) + ' conversations.'
