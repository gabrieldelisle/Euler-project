def chiffres(n) :
	while n :
		yield n%10
		n//=10

N_max = 2

l = [81]
while len(l)<30 :
	for j in range(3,10) :
		print(int((N_max/2)**(1/j)+1),int(N_max**(1/j)+1))
		for i in range(int((N_max/2)**(1/j)+1),int(N_max**(1/j)+1)):
			if sum(chiffres(i**j))==i :
				l.append(i**j)

	N_max*=2

l.sort()
print(l)
print(l[29])