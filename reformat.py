import glob


for filename in glob.glob('data/wiki*'):
    with open(filename, 'r+') as f:
        s = f.read()
        s = s.replace('}', '},', s.count('}')-1) # replace all but last one to form valid json
        s = s.replace('\n', '')
        s = '{"articles": [' + s + ']}'
        print(s)
        with open(filename+'.json', 'w') as f2:
            f2.write(s)
        print(filename)
