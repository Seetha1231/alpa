def max(l):
	m=-1
	for i in l:
		if m<i:
			m=i
	print(m)
	return m
  
def main():
	n=int(input())
	l=[]
	f=0
	for i in range(n):
		l.append(int(input()))
	m=max(l)
	print(m+n)
  
main()
