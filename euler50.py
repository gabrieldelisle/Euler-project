from math import sqrt

maxp = 1000000
entiers = list(range(maxp))
i = 2
while i*i <= maxp :
	if entiers[i]!=0 :
		for j in range(i+1,maxp) :
			if j%i==0 :
				entiers[j] = 0
	i+=1
premiers = []
for i in range(2,maxp) :
	if entiers[i]!=0 :
		premiers.append(i)
print('beginning')

def is_premier(n) :
	i=0
	p=2
	while p*p<=n :
		if n%p==0 :
			return False
		i+=1
		p = premiers[i]
	return True

maxn = 1000000
s = 0
maxi = 0
maxj = 0
maxs = 0
for i in range(len(premiers)) :
	s=premiers[i]
	j=0
	while s<=maxn and i+j<len(premiers)-1:
		j+=1
		s+=premiers[i+j]
		if is_premier(s) and j>maxj and s<=maxn:
			maxj = j
			maxs = s
			maxi = i

print(maxs, maxj, maxi)
