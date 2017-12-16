try:
	x=int(input())
	y=int(input())
	t=max(x,y)
	while(True):
		if (t%x==0 and t%y==0) :
			break
		t=t+1
	print(t)
except:
	print('invalid
