def compare(str1,str2):
	for i in range(len(str2)):
		str1+=str2[i]
	print(str1)
def main():
	try:
		s1=input()
		s2=input()
		compare(s1,s2)
	except:
		print('nvalid')
main()
