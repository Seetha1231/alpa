def f(l):
	for i in range(len(l)):
		if i==l[i]:
			print(i)
	
def main():
	try:
		n=int(input())
		l=[]
		for i in range(n):
			l.append(int(input()))
		f(l)
	except:
		print('invalid')
main()
