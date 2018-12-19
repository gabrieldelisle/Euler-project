from math import log

n_max = 100000
integers = list(range(n_max))
integers[1]=0
i = 2
while i*i <= n_max :
	if integers[i]!=0 :
		for j in range(1,(n_max-1)//(i*i)+1) :
			integers[j*i*i] = 0

	i+=1
radicals = [u for u in integers if u!=0]


i = 2
while i*i <= n_max :
	if integers[i]!=0 :
		for j in range(2,(n_max-1)//i+1) :
			integers[j*i] = 0

	i+=1
primes = [u for u in integers if u!=0]

print(radicals[:20])

def decomp(n) :
	if integers[n] :
		return [n]
	dec = []
	i=0
	while n!=1 :
		if n%primes[i]==0 :
			if primes[i] not in dec :
				dec.append(primes[i])
			n//=primes[i]
		else :
			i+=1
	return dec

M=100000
pos = 10000
eps = 1e-3

s = 1
sold = 0
for u in radicals :
	sold = s
	def count(m, l) :
		global s
		pmax = int(log(M/m+eps)/log(l[0]))
		if len(l)==1 :
			s+=pmax
		else :
			for i in range(1,pmax+1) :
				count(m*l[0]**i, l[1:])
	count(1,decomp(u))
	if s>pos :
		break

pos-=sold


memory = []
def issues(m, l) :
	if len(l)==0 :
		memory.append(m)
	else :
		pmax = int(log(M/m+eps)/log(l[0]))
		for i in range(1,pmax+1) :
			issues(m*l[0]**i, l[1:])
issues(1,decomp(u))

memory.sort()
res = memory[pos-1]
print(res)



