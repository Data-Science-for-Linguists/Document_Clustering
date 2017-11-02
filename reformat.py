import json
import glob


template = {'articles':[]}
for filename in glob.glob('data/wiki_*'):
    with open(filename, 'r+') as f:
        s = f.read()
        s = s.replace('}', '},', s.count('}')-1) # replace all but last one to form valid json
        s = s.replace('\n', '')
        s = "{'articles': [" + s + "]}"
        json.dumps(f,s)
        print(filename)
    break


