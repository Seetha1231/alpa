def lastjump(l,n):
	i=0
	while i<n:
		i+=l[i]
		try:
			if i==l[i]:
				return True
		except:
			return False
      
def main():
	l=[]
	n=int(input())
	for i in range(n):
		l.append(int(input()))
	print(lastjump(l,n))

main()
