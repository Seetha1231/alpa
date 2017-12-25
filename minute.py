def timetomin(t1,t2):
	l1=t1.split(':')
	l2=t2.split(':')
	(tt1,tt2)=(int(l1[0]),int(l2[0]))
	(tm1,tm2)=(int(l1[1]),int(l2[1]))
	if tt1<tt2:
		return False
	time=tt1-tt2
	mins=tm1-tm2
	mins+=(time*60)
	print('Minutes :',mins)
def main():
	try:
		t1=input()
		t2=input()
		timetomin(t1,t2)
	except:
		print('invalid')
main()
