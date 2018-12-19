#!/usr/bin/env python
# -*- coding: utf-8 -*-


###################################################################
#                                                                 #
#                       EULER PROJECT :                           #
#                                                                 #
###################################################################


def problem1_1(n) :
   s=0
   for i in range(n) :
      if i%3==0 or i%5==0 :
         s=s+i
   return s

         
def problem1_2(n) :
   s=0
   i=0
   while i<n :
      s=i+s
      i=i+3
   i=0
   while i<n :
      s=i+s
      i=i+5
   i=0
   while i<n :
      s=s-i
      i=i+15
   return s

print(1,problem1_2(1000))

def problem2(n) :
   u=1
   v=2
   s=1
   while v<=n:
      s=v+s
      t=v
      v=u+v
      u=t
   return s

print(2,problem2(4*10**6))
      
def crible(n):
   l=list(range(n+1))
   l[1]=0
   i=2
   while i*i<=n :
      if l[i]!=0 :
         j=i+i
         while j<=n :
            l[j]=0
            j=j+i
      i=i+1
   liste=[]
   for i in range(n+1) :
      if l[i]!=0 :
         liste.append(l[i])
   return liste

def problem3_1(n):
   c=crible(n)
   i=0
   while n!=1 :
      if n%c[i]==0 :
         n=n/c[i]
      else :
         i=i+1
   return c[i]
         
def problem3_2(n):
   i=2
   while n!=1 :
      if n%i==0 :
         n=n/i
      else :
         i=i+1
   return i

print(3,problem3_2(600851475143))

def palyndrome(n):
   l=[]
   while n>0 :
      l.append(n%10)
      n=n//10
      pal=True
   for i in range (len(l)//2) :
      if l[i]!=l[len(l)-i-1] :
         pal=False
   return pal
   

def problem4() :
   m=0
   for i in range(999,99,-1) :
      for j in range(999,i-1,-1) :
         if palyndrome(i*j) :
            if m<i*j :
               m=i*j
   return m

# print(4,problem4())

def problem5(n) :
   m=1
   c=crible(n)
   for i in range(len(c)) :
      j=c[i]
      while j<n :
         j=j*c[i]
      m=m*j//c[i]
   return m

print(5,problem5(20))

def problem6(n) :
   return (n*(n+1)/2)**2-n*(n+1)*(2*n+1)/6

print(6,problem6(100))

def estPremier(n) :
   p=True
   i=1
   while i*i<=n :
      i=i+1
      if n%i==0 :
         p=False
   return p

def problem7(n) :
   p=2
   l=1
   while l<n :
      p=p+1
      if estPremier(p) :
         l=l+1
   return p

# print(7,problem7(10001))

def int_to_list(n) :
   l=[]
   while n!=0 :
      l[0:0]=[n%10]
      n=n//10
   return l
   
def problem8(n) :
   m=0
   l=int_to_list(n)   
   for i in range(len(l)-13) :
      p=1
      for j in range (i,i+13) :
         p=p*l[j]
      if p>m :
         m=p
   return m

print(8, problem8(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450))

def problem9(n) :
   for a in range(1,n) :
      for b in range(1,n) :
         for c in range(1,n) :
            if a*a+b*b-c*c==0 and a+b+c==1000 :
               return [a,b,c,a*b*c]
   return -1

# print(9, problem9(500))

def problem10(n) :
   c=crible(n)
   s=0
   for e in c :
      s=s+e
   return s

# print(10, problem10(2*10**6))

def str_to_list(s) :
   l=""
   for i in range(len(s)) :
      if s[i]==' ' :
         l+=','
      else :
         l+=s[i]
   return l

def problem11(t) :
   m=0
   for i in range(17) :
      for j in range(17) :
         p=t[i][j]*t[i+1][j]*t[i+2][j]*t[i+3][j]
         if p>m :
            m=p
         p=t[i][j]*t[i][j+1]*t[i][j+2]*t[i][j+3]
         if p>m :
            m=p
         p=t[i][j]*t[i+1][j+1]*t[i+2][j+2]*t[i+3][j+3]
         if p>m :
            m=p
         p=t[i+3][j]*t[i+2][j+1]*t[i+1][j+2]*t[i][j+3]
         if p>m :
            m=p
   return m

print(11, problem11([[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
[52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
[24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
[67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
[24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
[21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
[78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
[16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],
[86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
[19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
[4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
[88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
[4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
[20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
[20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
[1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]))

def problem14(n) :
    p=0
    for i in range(1,n) :
        m=0
        k=i
        while k!=1 :
            m=m+1
            if k%2==0 :
                k=k/2
            else :
                k=3*k+1
        if m>p :
            p=m
            l=i
    return l

# print(14, problem14(10**6))

def pascal(n,k) :
    m=1
    for i in range(n-k+1,n+1) :
        m=m*i
    for i in range(1,k+1) :
        m=m//i
    return m

def pgcd(a,b):
    while a!=0 and b!=0 :
        if a>b :
            a=a%b
        else :
            b=b%a
    return a+b

def M(n) :
    l=[]
    for i in range(n+1) :
        for j in range(n+1) :
            for k in range(n+1) :
                if pgcd(pgcd(i,j),k)==1 :
                    l.append([i,j,k])
    return l
                
def problem16(n) :
   s=0
   while n>0 :
      s=n%10+s
      n=n//10
   return s

print(16, problem16(2**1000))

def problem19(jour, numero) :
   n=0
   m1=[31,28,31,30,31,30,31,31,30,31,30,31]
   m2=[31,29,31,30,31,30,31,31,30,31,30,31]
   j=numero%7
   for i in range(1901,2001) :
      if (i%4==0 and i%100!=0) or i%400==0 :
         m=m2
      else :
         m=m1
      for k in m :
         j=(j+k)%7
         if j==jour :
            n=n+1
   return n

print(19, problem19(6,1))

def factorielle(n) :
   m=1
   for i in range(1,m+1) :
      if i%5!=0 :
         m=m*i
      elif i%2!=0 :
         m=m//2
   return m

def somme_diviseurs(i) :
   s=0
   for j in range(1,i) :
      if i%j==0 :
         s=j+s
   return s

def problem21(n) :
   s=0
   l=[]
   for i in range(1,n) :
      d=somme_diviseurs(i)
      if somme_diviseurs(d)==i and d!=i:
         s=s+i
         l.append(i)
   return s,l
   
# print(21, problem21(10000))
   
def cycle(a,i) :
   r=[]
   t=0
   c=[]
   b= True
   j0=0
   while b :
       r.append(a%i)
       t=t+1
       c.append(a//i)
       a=10*r[t-1]
       for j in range(t-1) : 
           if r[t-1]==r[j] :
               j0=t-j-1
       b= a!=0 and j0<=0
   return j0, c
   
   
def problem26(n) :
    i0=0
    t0=0
    for i in range(1,n) : 
        t=cycle(1,i)[0]
        if t>t0 :
            t0=t
            i0=i
    return i0, t0
            
# print(26, problem26(1000))
            
def problem504(m) :
   n=0
   t=[]
   for i in range(1,m) :
      for j in range(1,m) :
         for k in range(1,m) :
            for l in range(1,m) :
               s=i+j+k+l
               if (int(s**(1/2)))**2==s :
                  n=n+1
                  t.append(s)
   return n,t

print(504, problem504(100))

def problem506(m):
   j=0
   s=0
   l=[1,2,3,4,3,2]
   for i in range(1,m+1) :
      f=0
      v=0
      while j>0 and f<i:
         f=f+l[j]
         v=(v*10+l[j])
         j=(j+1)%6
      g=(i-f)//15
      for k in range(g) :
         v=(v*10**6+123432)%123454321
      f=f+g*15
      while f<i:
         f=f+l[j]
         v=(v*10+l[j])
         j=(j+1)%6
      
      s=(v+s)%123454321
   return s

print(506, problem506(10**14))

def test(n) :
   a=1
   for i in range(n) :
      a=1
   return a
   
