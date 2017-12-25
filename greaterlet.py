def count(str):
	(max,c)=(-1,0)
	r=[]
	for i in range(len(str)):
		if str[i] in r:
			continue
		r.append(str[i])
		for j in range(len(str)):
			if str[i]==str[j] :
				c=c+1
		if max<c:
			max=c
		c=0
	return max
def maxcount(string):
	l=[]
	max=-1
	stri=string.split(' ')
	for i in stri:
		l.append(count(i))
	for i in range(len(l)):
		if max<l[i]:
			max=l[i]
			ind=i
	print(stri[ind])
def main():
	try:
		str=input()
		maxcount(str)
	except:
		print('invalid')
main()
