from math import log10
from time import time

# N = 10000
# Cmax = int(log10(N)*3)
# cubes = [i*i*i for i in range(1,N)]
# construction = []
# for i in range(Cmax+1) :
# 	construction.append([])
# 	for j in range(i+1) :
# 		construction[i].append([])
# for c in cubes : 
# 	ch = len(str(c))
# 	for i in range(ch+1) : 
# 		construction[ch][i].append(str(c)[:i])

# def permutation(n) :
# 	chiffres = len(str(n))
# 	def rec(inter, restants, nb=0) :
# 		if inter=='0' or not(inter in construction[chiffres][nb]) :
# 			return []
# 		if len(restants)>0 :
# 			suivant = []
# 			for i in range(len(restants)) :
# 				suivant+=rec(inter+restants[i], restants[:i]+restants[i+1:], nb+1)
# 			return suivant
# 		else :
# 			return [inter]

# 	res = []
# 	for u in rec("", str(n)) :
# 		k = int(u)
# 		if not(k in res) :
# 			res.append(k)
# 	return res



# def prob(n) :
# 	avancement = 0
# 	i = 0
# 	while i<len(cubes) :
# 		if cubes[i]>10**avancement : 
# 			print(avancement)
# 			avancement+=1
# 		p = permutation(cubes[i])
# 		for u in p :
# 			j = cubes.index(u)
# 			del(cubes[j])
# 			ch =len(str(u))
# 			for k in range(ch+1) :
# 				del(construction[ch][k][j])
# 		if len(p) == n :
# 			return cubes[i]
# 	return 0

# t = time()
# z = prob(5)
# print(z)
# print(time()-t)

N = 10000
cubes = [str(i*i*i) for i in range(N)]

def same_figures(a,b) :
	if len(a) == len(b) :
		c,d = list(a), list(b)
		try : 
			for i in range(len(a)) :
				del(d[d.index(c[0])])
				del(c[0])
			return True
		except : 
			pass
		return False

def prob2(n) :
	avancement = 0
	for i in range(N) :
		if len(cubes[i])>avancement : 
			print(avancement)
			avancement+=1
		count = 0
		for j in range(i+1, N) :
			if same_figures(cubes[i], cubes[j]) :
				count+=1
		if count == n-1 :
			return cubes[i]
	return 0

t = time()
print(prob2(5))
print(time()-t)