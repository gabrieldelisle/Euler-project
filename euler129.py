from time import time


# def R(k) :
# 	return sum([10**i for i in range(k)])


# def Rmod(k,n) :
# 	m = 0
# 	m10 = 1
# 	for i in range(k) :
# 		m+=m10
# 		m10*=10
# 		m10%=n
# 	return m%n

def A(n) :
	k=1
	rkmodn = 1
	m10 = 1
	while rkmodn!=0 :
		k+=1
		m10*=10
		m10%=n
		rkmodn+=m10
		rkmodn%=n
	return k

t = time()

for n in range(10**6,3**13) :
	if n%2!=0 and n%5!=0 and A(n)>10**6 : 
		print(n, A(n))
		break

print(time() - t)