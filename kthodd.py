def kodd(l,k):
	c=0
	for i in range(len(l)):
		if l[i]%2!=0:
			c=c+1
			if c==k:
				return l[i]
	return 'none'
def main():
	try:
		n=int(input())
		k=int(input())
		l=[]
		for i in range(n):
			l.append(int(input()))
		print(kodd(l,k))
	except:
		print('invalid')
main()
