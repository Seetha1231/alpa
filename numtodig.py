try:
	n=int(input())
	stri=''
	while(n!=0):
		stri+=str(n%10)
		n//=10
	for i in range(len(stri)-1,-1,-1):
		print(stri[i])
except:
	print('invalid')
