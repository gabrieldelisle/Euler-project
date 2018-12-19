from time import time
t = time()

def obtained(l) :
	if len(l)==1 :
		return l
	total = []
	for i in range(len(l)) :
		for u in obtained(l[:i]+l[i+1:]) :
			total.append(u*l[i])
			total.append(u+l[i])
			if u>l[i] :
				total.append(u-l[i])
			else : 
				total.append(l[i]-u)
			if l[i]!=0 :
				total.append(u/l[i])
			if u!=0 :
				total.append(l[i]/u)
	occ = {}
	for u in total :
		occ[u] = 1
	return list(occ.keys())

def int_only(l) :
	l2 = []
	for u in l :
		if u-int(u)==0:
			l2.append(int(u))
	l2.sort()
	return l2

def highest(l) :
	i=0
	while l[i]==i :
		i+=1
	return i-1

h_max = 10
for a in range(1,10) : 
	for b in range(a+1,10) :
		for c in range(b+1,10) :
			for d in range(c+1,10) : 
				l = int_only(obtained([a,b,c,d]))
				h = highest(l)
				if h>h_max :
					h_max = h
					print([a,b,c,d],h)

print(time()-t)