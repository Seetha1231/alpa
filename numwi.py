try:
	n=input()
	(d,c)=(0,0)
	for i in n:
		if i.isnumeric():
			d=d+1
		else:
			c=c+1
	print("number of words :"+str(c))
	print('number of integers:'+str(d))
except:
	print('invalid')
	
