def checkrange(n):
	if n in range(1,11):
		print('yes')
	else :
		print('no')
def main():
	try:
		n=int(input())
		checkrange(n)
	except:
		print('invalid')
		
main()
