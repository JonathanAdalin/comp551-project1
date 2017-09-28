import os
import json
from xml.sax.saxutils import escape

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
                            + escape(comment['commentText']).encode('utf-8', 'ignore') \
                            + '</utt>' \
                            + '<utt uid="2">' \
                            + escape(reply['commentText']).encode('utf-8', 'ignore') \
                            + '</utt>' \
                            + '</s>\n'
                        conversation_count += 1

conversation_count = 0
formatted_content = ''
output_location = 'out/'
output_file = 'youtube_spa.xml'
json_location = 'json/'

json_files = os.listdir(json_location)
for json_file in json_files:
    parse_comment_json(json_file, json_location)

output_xml = open(os.path.join(output_location, output_file), 'w+')
output_xml.write(formatted_content)
output_xml.close()

print 'Gathered ' + str(conversation_count) + ' conversations.'
