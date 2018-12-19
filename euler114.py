m = 3

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


print(count(50))