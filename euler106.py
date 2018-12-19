from time import time
t = time()


def special(n) :
	if n==1 :
		return [1]
	else :
		s = special(n-1)
		m = s[(n-1)//2]
		return [m]+[m+u for u in s]

def disjoint2(l) : 
	res = [([],[])]
	for e in l :
		res2 = []
		for a,b in res :
			if a or b :
				res2.append((a+[e],b))
			res2.append((a,b+[e]))
			res2.append((a,b))
		res = res2.copy()
	return res

def clear(l) :
	res = []
	for u in l :
		if u[0] and u[1] :
			res.append(u)
	return res 

def indices(n) :
	liste = clear(disjoint2(list(range(n))))
	needed = []
	for a,b in liste :
		if len(a)==len(b) and len(a)>1:
			valid = True
			if a[0]>b[0] :
				a,b = b,a
			for j in range(len(a)) :
				if a[j]>b[j] :
					valid = False
			if not valid :
				needed.append((a,b))
	return needed

for i in range(13) :
	print(len(indices(i)))
print(time()-t)
