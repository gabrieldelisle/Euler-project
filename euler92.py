from time import time

t=time()
n_max = 7


square = [i*i for i in range(10)]
def next(n) :
	s = 0
	while n :
		s+=square[n%10]
		n//=10
	return s
	# return sum([int(u)**2 for u in str(n)])

memorized = {}
def dynamic_end(n) :
	if n==89 or n==1 or n==0:
		return n
	else :
		try : 
			return memorized[n]
		except :
			following = dynamic_end(next(n))
			if n<=9*n_max:
				memorized[n] = following
		return following



firsts = []
for i in range(81*n_max+1) :
	firsts.append(dynamic_end(i))
print(time()-t)

def end(n) : 
	return firsts[next(n)]

# s = 0
# for i in range(2,10**n_max) :
# 	if end(i)==89 :
# 		s+=1

fact = [1]
m = 1
for i in range(1,n_max+1) : 
	m*=i
	fact.append(m)

def number(l) : 
	occ = {}
	for u in l :
		try :
			occ[u]+=1
		except :
			occ[u]=1
	t = fact[len(l)]
	for u in occ.values() :
		t//=fact[u]
	return t

s = 0
for a in range(10) :
	for b in range(a,10) :
		for c in range(b,10) :
			for d in range(c,10) :
				for e in range(d,10) :
					for f in range(e,10) :
						for g in range(f,10) :
							l = [a,b,c,d,e,f,g]
							n = 0
							for u in l :
								n*=10
								n+=u
							if end(n)==89 :
								s+=number(l)
print(s)
print(time()-t)