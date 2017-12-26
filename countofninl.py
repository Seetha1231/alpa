def norep(l,k):
	c=0
	for i in l:
		if k==i:
			c=c+1
	return c
def main():
	try:
		n=int(input())
		k=int(input())
		l=[]
		for i in range(n):
			l.append(int(input()))
		print(norep(l,k))
	except:
		print('invalid')
main()
