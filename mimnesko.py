#!/usr/bin/env python

import json
from datetime import datetime

version = '0.0.1'
print("MIMNESKO v" + version)

with open('database.json') as json_file:
    data = json.load(json_file)
    for p in data['records']:
        print('Note: ' + p['note'])
        print('Time: ' + datetime.fromisoformat(p['time']).strftime("%A, %d. %B %Y %I:%M%p"))
        print('\tTags: ' + ', '.join(p['tags']))

