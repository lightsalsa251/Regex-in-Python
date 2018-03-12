import re
s = 'we need to inform him the latest information'
#gives starting and ending indices of all that we find

for i in re.finditer('inform',s):
    loctup = i.span()
    print(loctup)
