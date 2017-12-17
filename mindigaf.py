def leastdig():
	n=input()
	k=int(input())
	l=[]
	for i in n:
		l.append(i)
	l.sort()
	s=''
	g=len(l)-k
	for i in range(g):
		s=s+l[i]
	print(int(s))
try:
	leastdig()
except:
	print('invalid')
