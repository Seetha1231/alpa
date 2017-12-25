def rotate(n,k,l):
	r=[]
	for i in range(n-k,n):
		r.append(l[i])
	for i in range(n-k):
		r.append(l[i])
	print(r)
def main():
	try:
		n=int(input())
		k=int(input())
		l=[]
		for i in range(n):
			l.append(int(input()))
		rotate(n,k,l)
	except:
		print('invalid')
main()
