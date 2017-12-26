def small2(l,k):
	l.sort()
	return l[k-1]
def main():
	try:
		n=int(input())
		k=int(input())
		l=[]
		for i in range(n):
			l.append(int(input()))
		print(small2(l,k))
	except:
		print('invalid')
main()
