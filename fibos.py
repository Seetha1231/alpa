def fib(n):
	if n==1 or n==0:
		return(n)
	else :
		return fib(n-1)+fib(n-2)
try:
	n=int(input())
	sum=0
	for i in range(0,n):
		print(fib(i))
except:
	print('invalid')
