try:
	f=1
	n=int(input())
	for i in range(1,n+1):
		f*=i
	print(f)
except:
	print('invalid')
