def countd(l,n):
	(max,min)=(0,9999)
	for i in range(n):
		if max<l[i]:
			max=l[i]
		if min>l[i]:
			min=l[i]
	print(max,min)
def main():
	try:
		l=[]
		n=int(input())
		for i in range(n):
			l.append(int(input()))
		countd(l,n)
	except:
		print('invalid')
main()
