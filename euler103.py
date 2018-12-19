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


def indices_needed(n) :
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

indices2 = [indices_needed(i) for i in range(8)]

def rules(l) :
	for i in range(1,len(l)//2+1) :
		if sum(l[:i+1])<=sum(l[len(l)-i:]) :
			return False

	for a,b in indices2[len(l)] :
		sa,sb = sum([l[i] for i in a]), sum([l[i] for i in b])
		if sa==sb :
			return False
	return True

def stringify(l) :
	s = ""
	for u in l :
		s+=str(u)
	return s

def optimum(n, ecart) :

	def recursion(n, s, mini, maxi) :
		if n==0 :
			return [[]]
		else :
			l = []
			for i in range(max(s[0]-ecart,mini), min(s[0]+ecart, maxi//len(s)+1)) :
				for u in recursion(n-1, s[1:], i+1, maxi-i) :
					new = [i]+u
					if len(s)<6 or rules(new) :
						l.append(new)
			return l

	s = special(n)
	m = sum(s)
	print(s,m)

	tests = recursion(n,s,s[0]-ecart, m-1)
	for l in tests:
		ml = sum(l)
		if ml<m :
			s = l
			m=ml
	return s,m

s,m = optimum(7,4)
print(s,m)
print(stringify(s))
print(time()-t)