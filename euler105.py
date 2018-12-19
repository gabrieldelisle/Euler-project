from time import time
t = time()


def special(n) :
	if n==1 :
		return [1]
	else :
		s = special(n-1)
		m = s[(n-1)//2]
		return [m]+[m+u for u in s]

def disjoint2(l) : 
	res = [([],[])]
	for e in l :
		res2 = []
		for a,b in res :
			if a or b :
				res2.append((a+[e],b))
			res2.append((a,b+[e]))
			res2.append((a,b))
		res = res2.copy()
	return res

def clear(l) :
	res = []
	for u in l :
		if u[0] and u[1] :
			res.append(u)
	return res 

indices = [clear(disjoint2(list(range(n)))) for n in range(13)]
print('indices computed')
print(time()-t)

def rules(l) :
	for a,b in indices[len(l)] :
		sa,sb = sum([l[i] for i in a]), sum([l[i] for i in b])
		if len(a)>len(b) :
			if sa<=sb :
				return False
		elif len(a)<len(b) :
			if sa>=sb :
				return False
		else :
			if sa==sb :
				return False
	return True

def doublons(l) :
	for i in range(len(l)) :
		if l[i] in l[:i]+l[i+1:] :
			return True
	return False

indices2 = []
for i in range(len(indices)) :
	indices2.append([])
	for a,b in indices[i]:
		if len(a)==len(b) :
			indices2[i].append((a,b))
print('indices2 computed')
print(time()-t)
print(indices2[4])


def rules2(l) :
	l.sort()
	i=2
	j = len(l)-1
	while i<j :
		if sum(l[:i])<=sum(l[j:]) :
			return False
		i+=1
		j-=1
	for a,b in indices2[len(l)] :
		sa,sb = sum([l[i] for i in a]), sum([l[i] for i in b])
		if sa==sb :
			return False
	return True

file = open('sets.txt', 'r')
content = file.read()
file.close()
sets = content.split('\n')
s = 0
for e in sets :
	a = [int(u) for u in e.split(',')]
	if rules(a) :
		s+=sum(a)
print(s)
print(time()-t)