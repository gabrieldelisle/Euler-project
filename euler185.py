from collections import deque
from time import time


test = [("90342", 2), ("70794", 0), ("39458", 2), ("34109", 1), ("51545", 2), ("12531", 1)]
real = [("5616185650518293", 2), ("3847439647293047", 1), ("5855462940810587", 3), ("9742855507068353", 3), ("4296849643607543", 3), ("3174248439465858", 1), ("4513559094146117", 2), ("7890971548908067", 3), ("8157356344118483", 1), ("2615250744386899", 2), ("8690095851526254", 3), ("6375711915077050", 1), ("6913859173121360", 1), ("6442889055042768", 2), ("2321386104303845", 0), ("2326509471271448", 2), ("5251583379644322", 2), ("1748270476758276", 3), ("4895722652190306", 1), ("3041631117224635", 3), ("1841236454324589", 3), ("2659862637316867", 2)] 






def match(string, guess, left) :
	maxi = len(guess[0][0])-len(string)
	s=0
	for u,i in guess :
		correct = sum([v==u[j] for j,v in enumerate(string)])
		if correct>i or i-correct>maxi:
			return False
		s+=correct
	return s>=left[len(string)]



def mastermind(guess) :
	N = len(guess[0][0])

	occ = [[0]*10 for i in range(N)]
	for u in guess :
		for i,c in enumerate(u[0]) :
			occ[i][int(c)]+=1
	occmax = [max(occ[i]) for i in range(N)]
	total = sum(b for a,b in guess)
	left = [total-sum(occmax[i:]) for i in range(N+1)]

	t0 = time()
	queue=deque([""])
	chiffres=0
	while queue :
		init = queue.popleft()
		if len(init)>chiffres :
			chiffres=len(init)
			print(chiffres, time()-t0)

		if len(init) == N :
			return init
		for i in range(10) :
			new = init+str(i)
			if match(new, guess, left) :
				queue.append(new)
	return None

def parts_among(l, n) :
	if n==0 : 
		return [[]]
	elif n==len(l) :
		return [l]
	else :
		return [[l[0]]+u for u in parts_among(l[1:], n-1)]+[u for u in parts_among(l[1:], n)]

def mastermind2(guess) :
	guess.sort(key=lambda x: x[1])
	N = len(guess[0][0])
	correct_max = max(guess, key = lambda x: x[1])[1]
	parts = [parts_among(list(range(N)),i) for i in range(correct_max+1)]
	print(len(parts[3]))

	queue=[([[str(c) for c in range(10)]]*N, 0)]
	while queue :
		test, i = queue.pop()
		if i==len(guess) :
			print(test)
			return ''.join([u[0] for u in test])
		for u in parts[guess[i][1]] :
			if all([guess[i][0][j] in test[j] for j in u])  :
				new = []
				for j in range(N) :
					if j in u :
						new.append([guess[i][0][j]])
					else :
						new.append([])
						for k in test[j] :
							if k!=guess[i][0][j] :
								new[j].append(k)
				if all([len(u)>0 for u in new]) :
					queue.append((new, i+1))
	return None


t = time()
print(mastermind(real))
print(time()-t)