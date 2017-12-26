def countdigs(n):
	c=0
	while(n!=0):
		n//=10
		c+=1
	print(c)
def main():
	try:
		n=int(input())
		countdigs(n)
	except:
		print('invalid')
main()
