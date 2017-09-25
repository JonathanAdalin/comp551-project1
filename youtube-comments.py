# Jonathan Adalin

import os
import json

# Helper functions

def parse_comment_json(json_file, json_location):
    global conversationCount
    with open(os.path.join(json_location, json_file)) as json_file:
        comment_list = json.loads(json_file.read())
        for comment in comment_list:
            if comment['hasReplies'] == True:
                # print 'PARENT ID ' + comment['user']
                # print 'PARENT CONTENT ' + comment['commentText']
                for reply in comment['replies']:
                    # Ignore recursive comments
                    if '\n' not in reply['commentText']:
                        # print '    CHILD ID ' + reply['user']
                        # print '    CHILD CONTENT ' + reply['commentText']
                        conversationCount += 1

# Main

conversationCount = 0
json_location = 'json/'
json_files = os.listdir(json_location)
for json_file in json_files:
    parse_comment_json(json_file, json_location)

print conversationCount
