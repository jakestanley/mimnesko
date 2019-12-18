#!/usr/bin/env python

import json
from _sha256 import sha256
from datetime import datetime
from cmd import Cmd

ENCODING = 'utf8'

version = '0.0.1'
data = list()
print("MIMNESKO v" + version)

with open('database.json') as json_file:
    # data = json.load(json_file)
    # for p in data['records']:
    #     print('Note: ' + p['note'])
    #     print('Time: ' + datetime.fromisoformat(p['time']).strftime("%A, %d. %B %Y %I:%M%p"))
    #     print('\tTags: ' + ', '.join(p['tags']))


    def get_tags():
        _tags = set()
        for d in data:
            for t in d['tags']:
                _tags.add(t)
        return _tags


class NeskoPrompt(Cmd):
    prompt = 'NESKO> '
    intro = "Commands: note, tags, find"

    def do_tag(self, inp):
        _args = inp.split(' ')
        _tags = set()
        _hashes = set()
        for a in _args:
            if len(a) > 0:
                if a[0] == '#':
                    _tags.add(a)
                elif len(a) > 1:
                    _hashes.add(a)

        if len(_tags) > 0 and len(_hashes) > 0:
            print('tagging')  # TODO

    def do_tags(self, inp):
        print(', '.join(get_tags()))
    #
    # def do_tagged(self, inp):
    #     for d in datums:
    #         if d['tags'].

    def do_note(self, inp):
        content = dict()

        content['time'] = datetime.now().isoformat()
        content['note'] = inp

        record = dict()
        record['content'] = content
        record['tags'] = set()
        record['hash'] = sha256(json.dumps(content).encode(ENCODING)).hexdigest()

        print("Record: {0}".format(record.__str__()))
        data.append(record)

    def do_list(self, inp):
        for d in data:
            print("Record: {0}".format(d.__str__()))

    def default(self, line):
        print('command: ' + line + " not handled by default")


prompt = NeskoPrompt()
prompt.cmdloop()
