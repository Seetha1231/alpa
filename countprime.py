try:
	s=int(input())
	e=int(input())
	c=0
	if s==1:
		s+=1
	for j in range(s,e+1):
		flag=0
		for i in range(2,int(j/2)+1):
			if j%i ==0:
				flag=1
				break
		if flag==1:
			continue
		c=c+1
	print(c)
except:
	print('invalid')
