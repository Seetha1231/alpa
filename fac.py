try:
	f=1
	n=int(input())
	if(n>=0):
		for i in range(1,n+1):
			f*=i
		print(f)
	else:
		print('please enter positive integer')
except:
	print('invalid')
