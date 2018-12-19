from time import time
t = time()

nmax = 10**7
amax = nmax//4+1

#even numbers
b=2
s=0
for a in range(4, amax+1,2) :
	while a**2-b**2>nmax :
		b+=2
	s+=(a-b)//2
#not even numbers 

b=1
for a in range(3, amax+1,2) :
	while a**2-b**2>nmax :
		b+=2
	s+=(a-b)//2

print(s)
print(time()-t)