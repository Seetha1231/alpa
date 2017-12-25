def mul(n1,n2):
	mul=int(n1)*int(n2)
	print(str(mul))

def main():
	try:
		a=input()
		b=input()
		mul(a,b)
	except:
		print('invalid')
main()
