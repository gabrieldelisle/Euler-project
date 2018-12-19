from roman import *

file = open('roman.txt', 'r')
content = file.read()
file.close()
s = 0
for u in content.split('\n') :
	s+= len(u) - len(roman(dec(u)))
print(s)