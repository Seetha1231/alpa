def encode(str1,str2):
	(n1,n2)=(len(str1),len(str2))
	(enstr1,enstr2)=('','')
	for i in range(n1):
		c=ord(str1[i])
		c=c+10
		if c > 122:
			c=c-26
		enstr1+=chr(c)
	enstr2+=str2[0]
	for i in range(1,n2-1):
		c=ord(str2[i])
		c=c+10
		if c > 122:
			c=c-26
		enstr2+=chr(c)
	enstr2+=str2[n2-1]
	print(enstr1,enstr2)
def main():
	try:
		str1=input()
		str2=input()
		encode(str1,str2)
	except:
		print('invalid input')
main()
