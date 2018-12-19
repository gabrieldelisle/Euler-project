from time import time
t = time()

bina = {}
def binary(k) :
	if k in bina :
		return bina[k]
	bina[k] = len(bin(k))-3+sum([int(u) for u in bin(k)[3:]])
	return bina[k]

m = [0,0,1,2]
for k in range(4,201) :
	b = binary(k)
	if m[k-1]<= b-2 :
		b=m[k-1]+1
	if m[k-2]<=b-2 :
		b=m[k-2]+1
	m.append(b)

M=max(m)

def addone(l) :
	if len(l)<=M :
		for i,u in enumerate(l) :
			for v in l[i:] :
				s = u+v
				if s<=200 and len(l)<=m[s] :
					m[s] = len(l)
					addone(l+[s])
addone([1])

print(m)
print(time()-t)
