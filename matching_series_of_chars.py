#matching series of range of characters
import re
a = re.findall('[h-m]at','sat,hat,mat,pat')

for i in a:
    print(i)

print('not including starting characters which are h-m')
a = re.findall('[^h-m]at','sat,hat,mat,pat')

for i in a:
    print(i)
