try:
	n=int(input())
	for i in range(1,n+1):
		print(str(n)+'*'+str(i)+'='+str(n*i))
except:
	print('invalid')
