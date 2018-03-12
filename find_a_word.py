import re
if re.findall('inform','we need to inform him'):
    print(True)

all = re.findall('inform','we need to inform him with the latest information')
for i in all:
    print(i)
