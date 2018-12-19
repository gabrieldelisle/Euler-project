from time import time
n_max = 1000000-1

t = time()
# divisors = []
# for i in range(n_max+1) :
# 	divisors.append([])

# for d in range(1, n_max//2+1) :
# 	for k in range(2, n_max//d+1) :
# 		divisors[k*d].append(d)

# print(time()-t)
# successor = [sum(u) for u in divisors]
# print(time()-t)

done = []
for i in range(n_max+1) :
	done.append(False)

l_max = 0
k_max = 0
for k0 in range(1,n_max+1) :
	chain = []
	k = k0
	while k<=n_max and not done[k] :
		chain.append(k)
		done[k] = True
		k = successor[k]
	if k in chain :
		l = len(chain)-chain.index(k)
		if k<=n_max and l>l_max :
			l_max = l
			k_max = k

print(k_max, l_max)
