from time import time

t = time()
d = 1000

# ways = [[], [0,1]]
# i=1
# chiffres = 0
# while ways[i][i]%d!=0 :
# 	if chiffres!=len(str(i)) :
# 		chiffres=len(str(i))
# 		print(chiffres)
# 	i+=1
# 	ways.append([0])
# 	for j in range(1,i) :
# 		ways[i].append(ways[i][j-1]+ways[i-j][min(i-j,j)])
# 	ways[i].append(ways[i][i-1] + 1)

ways = [0,1]
i=1
while ways[i]%d!=0 :
	i+=1
	ways.append(0)
	sign = 1
	for j in range(1,i+1) :
		sign = -sign
		ways[i]+= sign * ( ways[i-j*(3*j-1)//2] + ways[i-j*(3*j+1)//2] )


print(i)
#echec