def countd(n):
	print(n+1)
def main():
	try:
		n=int(input())
		countd(n)
	except:
		print('invalid')
main()
