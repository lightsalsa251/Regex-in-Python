#replacing a string
import re
food = 'rat mat'
reg = re.compile('[r]at')
food = reg.sub('food',food)
print(food)
