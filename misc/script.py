import os

p = '/Users/telliott/Dropbox/Github-math/quickgeo/files'
L = [fn for fn in os.listdir(p) if fn.endswith('.tex')]
rL = []

for fn in L:
    fh = open(p + '/' + fn,'r')
    s = fh.read()
    sL = s.strip().split('\n')
    for line in sL:
        if line.startswith('%'):
            continue
        if 'png' in line:
            try:
                rL.append(line.split()[3:])
            except:
                rL.append(line)

rL.sort()
for e in rL:
    print(e)