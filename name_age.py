import re
name = '''Janice is 22 and Theon is 33
        Gabriel is 44 and Joey is 21'''

ages = re.findall(r'\d{1,3}',name)#{1,3} as all numbers are 2 digits
names = re.findall(r'[A-Z][a-z]*',name)
print(ages)
age = {}
x = 0

for each in names:
    age[each] = ages[x]
    x+=1

print(age)
