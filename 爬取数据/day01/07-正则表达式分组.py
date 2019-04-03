import re
s = 'a b c d'
p1= re.compile('\w+\s+\w+')

print(p1.findall(s)) # 'a b','c d' 

p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s)) # 'a' 'c'

p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s)) #('a'b)('c'd') 


print(p1.split(s))
print(p2.split(s))
print(p3.split(s))