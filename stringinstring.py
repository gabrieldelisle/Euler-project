def shortestin(s) :
	occ = {}
	for a in s :
		try :
			occ[a]+=1
		except :
			occ[a]=1
	alphabet = occ.keys()
	n = len(alphabet)

	for u in alphabet :
		occ[u] = 0
	n_inter = 0

	begin = 0
	end = 0
	s_min = s
	n_min = len(s)

	while 1 :
		if n_inter == n :
			if n_inter<n_min :
				n_min = n_inter
				s_min = s[begin:end]
			occ[s[begin]]-=1
			if occ[s[begin]] == 0 :
				n_inter-=1
			begin+=1

		else :
			if end>=len(s) :
				return s_min
			if occ[s[end]] == 0 :
				n_inter+=1
			occ[s[end]]+=1
			end+=1

print(shortestin("caabbaac"))