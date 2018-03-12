#solving backslash problem
import re
r = 'here is \\ronaldo'
print(re.search(r'\\ronaldo',r))
#this treats backslashes as special
