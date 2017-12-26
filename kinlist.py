def checkkn(l,k):
	if k in l:
		return 'yes'
	return 'no'
def main():
	try:
		n=int(input())
		k=int(input())
		l=[]
		for i in range(n):
			l.append(int(input()))
		print(checkkn(l,k))
	except:
		print('invalid')
main()
