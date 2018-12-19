from math import sqrt

def are_anagram(m1, m2) :
	a = list(m1)
	b = list(m2)
	a.sort()
	b.sort()
	return a == b and m1!=m2

file = open('words.txt', 'r')
content = file.read()
file.close()

words = content.split(',')

anagram = []
for u in words :
	for v in words :
		if are_anagram(u,v) :
			anagram.append([u,v])

#anagram = [['ACT', 'CAT'], ['ARISE', 'RAISE'], ['BOARD', 'BROAD'], ['BROAD', 'BOARD'], ['CARE', 'RACE'], ['CAT', 'ACT'], ['CENTRE', 'RECENT'], ['COURSE', 'SOURCE'], ['CREATION', 'REACTION'], ['CREDIT', 'DIRECT'], ['DANGER', 'GARDEN'], ['DEAL', 'LEAD'], ['DIRECT', 'CREDIT'], ['DOG', 'GOD'], ['EARN', 'NEAR'], ['EARTH', 'HEART'], ['EAST', 'SEAT'], ['EAT', 'TEA'], ['EXCEPT', 'EXPECT'], ['EXPECT', 'EXCEPT'], ['FILE', 'LIFE'], ['FORM', 'FROM'], ['FORMER', 'REFORM'], ['FROM', 'FORM'], ['GARDEN', 'DANGER'], ['GOD', 'DOG'], ['HATE', 'HEAT'], ['HEART', 'EARTH'], ['HEAT', 'HATE'], ['HOW', 'WHO'], ['IGNORE', 'REGION'], ['INTRODUCE', 'REDUCTION'], ['ITEM', 'TIME'], ['ITS', 'SIT'], ['LEAD', 'DEAL'], ['LEAST', 'STEAL'], ['LIFE', 'FILE'], ['MALE', 'MEAL'], ['MEAL', 'MALE'], ['MEAN', 'NAME'], ['NAME', 'MEAN'], ['NEAR', 'EARN'], ['NIGHT', 'THING'], ['NO', 'ON'], ['NOTE', 'TONE'], ['NOW', 'OWN'], ['ON', 'NO'], ['OWN', 'NOW'], ['PHASE', 'SHAPE'], ['POST', 'SPOT'], ['POST', 'STOP'], ['QUIET', 'QUITE'], ['QUITE', 'QUIET'], ['RACE', 'CARE'], ['RAISE', 'ARISE'], ['RATE', 'TEAR'], ['REACTION', 'CREATION'], ['RECENT', 'CENTRE'], ['REDUCTION', 'INTRODUCE'], ['REFORM', 'FORMER'], ['REGION', 'IGNORE'], ['SEAT', 'EAST'], ['SHAPE', 'PHASE'], ['SHEET', 'THESE'], ['SHOUT', 'SOUTH'], ['SHUT', 'THUS'], ['SIGN', 'SING'], ['SING', 'SIGN'], ['SIT', 'ITS'], ['SOURCE', 'COURSE'], ['SOUTH', 'SHOUT'], ['SPOT', 'POST'], ['SPOT', 'STOP'], ['STEAL', 'LEAST'], ['STOP', 'POST'], ['STOP', 'SPOT'], ['SURE', 'USER'], ['TEA', 'EAT'], ['TEAR', 'RATE'], ['THESE', 'SHEET'], ['THING', 'NIGHT'], ['THROW', 'WORTH'], ['THUS', 'SHUT'], ['TIME', 'ITEM'], ['TONE', 'NOTE'], ['USER', 'SURE'], ['WHO', 'HOW'], ['WORTH', 'THROW']]
Lmax = max(len(u) for u,v in anagram)


def chiffres(n) :
	i = 0
	while n :
		n//=10
		i+=1
	return i

def decomp(n) : 
	d = []
	while n :
		d.append(n%10)
		n//=10
	d.reverse()
	return d

squares = {}
for i in range(1,Lmax+1) :
	squares[i] = []

i = 1
while i*i < 10**Lmax :
	squares[chiffres(i*i)].append(i*i)
	i+=1


maximum = 0
for m1,m2 in anagram :
	N = len(m1)
	for n in squares[N] :
		d = decomp(n)
		dico = {}
		ok = True
		for i in range(N) :
			if d[i] not in dico.values() and m1[i] not in dico.keys() :
				dico[m1[i]] = d[i]
			else : 
				try : 
					if dico[m1[i]] != d[i] :
						ok = False
				except :
					ok = False
		if ok :
			n2 = 0
			for i in range(N) :
				n2+=dico[m2[i]]*10**(N-i-1)
			if sqrt(n2)==int(sqrt(n2)) and chiffres(n2)==N: 
				if n>maximum : 
					maximum = n
				if n2>maximum :
					maximum = n2
print(maximum)