#dealing with whitespaces
import re

r = '''keep the
flag flying
high'''
print(r,
      '\n')

print('changing','\n')
reg = re.compile('\n')
r = reg.sub(' ',r)

print(r)
