#match words with a particular pattern
import re

s = 'Sat,hat,mat,pat'
#S is uppercase so it will not be printed
a = re.findall('[shmp]at',s)
for i in a:
    print(i)
