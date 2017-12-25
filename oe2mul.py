def oddeven(n):
	if n%2==0:
		print("even")
	else:
		print("odd")
def mul2():
	try:
		m=int(input())
		n=int(input())
		oddeven(m*n)
	except:
		print('invalid')
