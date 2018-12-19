def fibo(k) :
	if k==1 : 
		return 1
	a = 1
	b = 1
	for i in range(k-2) :
		a, b = b, a+b
	return b

N = 10
my_numbers = [fibo(i) for i in range(2,N+1)]
print(my_numbers)

n_max = fibo(N)+1
entiers = list(range(n_max))
i = 2
while i*i <= n_max :
	if entiers[i]!=0 :
		for j in range(i+1,n_max) :
			if j%i==0 :
				entiers[j] = 0
	i+=1
premiers = []
for i in range(2,n_max) :
	if entiers[i]!=0 :
		premiers.append(i)

print(premiers[:10])

def decomposition(k) :
	i=0
	dec = []
	while k>1 :
		if k%premiers[i]==0: 
			dec.append(premiers[i])
			k/=premiers[i]
		else :
			i+=1
	return dec


decomps = {0:[], 1:[]}
def decomp3(i) : 
	try : 
		return decomps[i]
	except : 
		decomp = []
		j = 0
		while j<len(premiers) and premiers[j]<=i :
			if premiers[j]==i : 
				decomp.append(premiers[j])
			elif premiers[j]<=i-2 :
				for u in decomp3(i-premiers[j]) :
					a = (u*premiers[j])%1e9
					if not(a in decomp) :
						decomp.append(a)
			j+=1
		decomps[i] = decomp
		return decomp


s = 0
for i in my_numbers :
	s+= sum(decomp3(i))
print(s)


