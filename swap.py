def main():
	try:
		x=int(input())
		y=int(input())
		t=x
		x=y
		y=t
		print(x,y)
	except:
		print('invalid')
main()
