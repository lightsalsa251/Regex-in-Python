#matching a single character
import re

r = '12345'

print('Matches:',len(re.findall('\d{5}',r)))
#\d matches any numbers
#\D matches any thing but a number

num = '123 1234 12345 123456 1234567'
print('Matches:',len(re.findall('\d{5,7}',num)))
