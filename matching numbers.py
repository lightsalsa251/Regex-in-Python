#matching phone numbers
# \w -> similar as [a-zA-Z0-9_]
# \W anything but above
import re
p = '412-555-1212'
#here \d can also be used
if re.search('\w{3}-\w{3}-\w{4}',p):
    print(True)

# \s = [\f\n\r\t\v]
# \S is opposite of \s

if re.search('\w{2,20}\s\w{2,20}','Shivang Ganjoo'):
    print(True)
