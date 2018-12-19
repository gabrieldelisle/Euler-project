from time import time

n_max = 100000
integers = list(range(n_max))
i = 2
while i*i <= n_max :
	if integers[i]!=0 :
		for j in range(i+1,n_max) :
			if j%i==0 :
				integers[j] = 0
	i+=1
primes = []
for i in range(2,n_max) :
	if integers[i]!=0 :
		primes.append(i)

limit = [primes.index(min(primes, key= lambda x:abs(x-(34427)/i))) for i in range(5,0,-1)]
print("limit : ", limit)
#uncomment to find a first 5 satisfying conditions, which give us a majoration a majoration
#limit = [100, 300, 1000, 3000, 10000]

def concat(i,j) :
	return int(str(i)+str(j))

def is_prime(n) :
	i=0
	while primes[i]*primes[i]<=n :
		if n%primes[i]==0 :
			return False
		i+=1
	return True

def works(p, others) : 
	for u in others :
		if not(is_prime(concat(u,p)) and is_prime(concat(p,u))) :
			return False
	return True

print('begin')

t = time()

#test[i] will contain every i-tuples satisfying the conditions
test = [[[p] for p in primes[:limit[0]]]]
for i in range(1,5) :
	test.append([])
	for u in test[i-1] :
		for p in primes[:limit[i]] :
			if max(u)<= p and works(p, u) :
				test[i].append( u+[p])
	print(len(test[i]), test[i][:5])
	print(min([sum(u) for u in test[i]]))

print("time : ", time()-t, " s")
