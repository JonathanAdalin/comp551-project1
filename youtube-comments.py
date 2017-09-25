# Jonathan Adalin

import os
import json

# Helper functions

def parse_comment_json(json_file, json_location):
    with open(os.path.join(json_location, json_file[0])) as json_file:
        comment_list = json.loads(json_file.read())
        for comment in comment_list:
            print comment['id']

# Main

json_location = 'json/'
json_files = [os.listdir(json_location)]
for json_file in json_files:
    parse_comment_json(json_file, json_location)
