from time import time
t = time()

nmax = 100
both = 9*nmax+1

#decreasing
lastdigit = [1]*10

for i in range(1,nmax) :
	lastdigit = [sum(lastdigit[i:])+1 for i in range(10)]
	lastdigit[0]-=1
decreasing = sum(lastdigit)

#increasing
lastdigit = [1]*10

for i in range(1,nmax) :
	lastdigit = [sum(lastdigit[:i+1]) for i in range(10)]
increasing = sum(lastdigit)

print(decreasing+increasing-both-1)
print(time()-t)