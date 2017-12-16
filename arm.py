try:
	n=int(input())
	temp=n
	ams=0
	while(temp!=0):
		rem=temp%10
		ams=ams+rem*rem*rem
		temp=int(temp/10)
	if n==ams :
		print('armstrong number')
	else :
		print ('not armstrong')
except :
	print('invalid')
