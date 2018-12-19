from time import time

t = time()
display = ['01', '04', '06', '16', '25', '36', '46', '64', '81']
display = [[int(u[0]), int(u[1])] for u in display]

def parts_among(l, n) :
	if n==0 : 
		return [[]]
	elif n==len(l) :
		return [l]
	else :
		return [[l[0]]+u for u in parts_among(l[1:], n-1)]+[u for u in parts_among(l[1:], n)]

part6 = parts_among([0,1,2,3,4,5,6,7,8,6], 6)

s=0
for i in range(len(part6)) : 
	for j in range(i) :
		valid = True
		for u in display :
			a,b = u
			if not((a in part6[i] and b in part6[j]) or (b in part6[i] and a in part6[j])):
				valid  = False
		if valid : 
			s+=1
print(s)
print(time()-t)