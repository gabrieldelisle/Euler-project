memory = {}

def count(n) :
	if n<0 :
		return 0
	if n==0 :
		return 1

	try :
		return memory[n]
	except :
		s = 0
		for i in range(1,5) :
			s+=count(n-i)
		memory[n] = s
		return s

print(count(50))