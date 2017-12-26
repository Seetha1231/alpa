def fibo(n):
	if n==1 or n==0:
		return(n)
	else :
		return fibo(n-1)+fibo(n-2)
try:
	n=int(input())
	sum=0
	for i in range(0,n):
		print(fibo(i))
except:
print('invalid')
