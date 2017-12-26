def main():
	try:
		n=int(input())
		if n%2!=0:
			n-=1
		print(n)
	except:
		print('invalid')
main()
