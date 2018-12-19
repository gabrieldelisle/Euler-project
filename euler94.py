from math import gcd, sqrt
from time import time

t = time()

p_max = 10**9
m_max = int(sqrt(p_max/2))+1

primary = []
for m in range(1, m_max) :
	n1 = int(m/sqrt(3))
	n2 = int((2-sqrt(3))*m)
	for n in [n1,n2] :
		if n>0 and (m+n)%2==1 and gcd(n,m)==1 : 
			primary.append([m*m-n*n, 2*m*n, m*m+n*n])

def without_doubles(l) :
    a = []
    for u in l :
        u.sort()
        if u not in a :
            a.append(u)
    return a

primary = without_doubles(primary)

s = 0
for u in primary :
	a,b,c = u
	if b<a :
		a,b = b,a
	if abs(2*a-c)<=1 and 2*(a+c)<=p_max:
		s+=2*(a+c)
print(s)
print(time()-t)

# t = time()

# def integer(n) :
# 	return n-int(n)==0

# s = 0
# for i in range(2, p_max//3+2) :
# 	for j in range(i-1, i+2) :
# 		if integer(sqrt(i*i-j*j/4)) :
# 			s+=j+2*i

# print(s)
# print(time()-t)

# # (m2+n2)//2 = m2-n2

# n2 = m2 / 3 (-1)

# (m2+n2)//2 = 2mn
# d = 12
# n = m(2+s(3))