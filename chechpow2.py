def main():
	try:
		f=0
		a=int(input())
		while(a!=0):
			a=a/2
			if a==1:
				f=1
				break
		if f!=1:
			print('no')
		else :
			print('yes')
	except:
		print('invalid')
main()
