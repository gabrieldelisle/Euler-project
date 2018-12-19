# from time import time
# t = time()

# n_max = 1000004
# integers = list(range(n_max))
# integers[1]=0
# i = 2
# while i*i <= n_max :
# 	if integers[i]!=0 :
# 		for j in range(2,(n_max-1)//i+1) :
# 			integers[j*i] = 0

# 	i+=1
# primes = [u for u in integers if u!=0]

# print(len(primes))


# s=0
# a0=1

# Z = 1000

# post = [[i*j%Z for i in range(Z)]  for j in range(Z)]
# pre = [[0]*Z for i in range(Z)]
# for i in range(Z) :
# 	for j in range(Z) :
# 		pre[i][post[i][j]]=j


# print("pre-computation done :", time()-t)

# t = time()

# for i in range(2,len(primes)-1) :
# 	p1=primes[i]
# 	p2=primes[i+1]


# 	if p1>a0 :
# 		a0*=10
# 		print(a0)
	
# 	l=pre[p2%Z][p1%Z]
# 	if a0>=Z :
# 		while (p2*l)%a0!=p1 :
# 			l+=Z
# 		s+=p2*l

# 	else :
# 		a=a0
# 		while (a+p1)%p2!=0 :
# 			a+=a0
# 		s+=a+p1

# print(s)
# print(time()-t)


from time import time
t = time()

n_max = 1000004
integers = list(range(n_max))
integers[1]=0
i = 2
while i*i <= n_max :
	if integers[i]!=0 :
		for j in range(2,(n_max-1)//i+1) :
			integers[j*i] = 0

	i+=1
primes = [u for u in integers if u!=0]

print(len(primes))


s=0
a0=0

Z = 10

post = [[i*j%Z for i in range(Z)]  for j in range(Z)]
pre = [[0]*Z for i in range(Z)]
for i in range(Z) :
	for j in range(Z) :
		pre[i][post[i][j]]=j


print("pre-computation done :", time()-t)

t = time()

for i in range(2,len(primes)-1) :
	p1=primes[i]
	p2=primes[i+1]


	if p1>Z**a0 :
		a0+=1
	
	l=0
	for j in range(a0) :
		pp1 = (p1-l*p2)//Z**j
		l += pre[p2%Z][pp1%Z]*Z**j
	s+=l*p2


	

print(s)
print(time()-t)


