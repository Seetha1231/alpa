def main():
	try:
		x=int(input())
		y=int(input())
		x=x^y
		y=x^y
		x=x^y
		print(x,y)
	except:
		print('invalid')
main()
