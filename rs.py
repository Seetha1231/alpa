def f(l):
	l.sort(reverse=True)
	s=''
	c=0
	new=''
	for i in l:
		s+=str(i)
		c+=1
	print(s)
	c=0
	for i in range(len(s)-1,-1,-1):
		if c==3:
			c=0
			new+=','
		new+=s[i]
		c=c+1
	print(new[::-1])
	
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
