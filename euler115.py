m = 50

memory = {}

def count(n) :
	if n<m :
		return 1
	try :
		return memory[n]
	except :
		s = count(n-1)
		for i in range(m,n+1) :
			s+=count(n-i-1)
		memory[n] = s
		return s

f=0
i=0
while f<10**6 :
	i+=1
	f = count(i)

print(i)